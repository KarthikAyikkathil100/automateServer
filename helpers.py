import boto3
import logging
logging.basicConfig(level=logging.INFO)
from concurrent.futures import ThreadPoolExecutor, as_completed
import psutil
import time
import subprocess
import itertools
import time

# Initialize DynamoDB resource using boto3
dynamodb = boto3.resource('dynamodb')
table_name = 'Routes'



def chunked(iterable, size):
    it = iter(iterable)
    while True:
        chunk = list(itertools.islice(it, size))
        if not chunk:
            break
        yield chunk


def build_projection_expression(attributes):
    """
    Converts ["id", "name", "status"] into:
    ProjectionExpression: "#attr0, #attr1, #attr2"
    ExpressionAttributeNames: {"#attr0": "id", ...}
    """
    if not attributes:
        return None, None

    expr_names = {}
    expr_parts = []

    for i, attr in enumerate(attributes):
        placeholder = f"#attr{i}"
        expr_parts.append(placeholder)
        expr_names[placeholder] = attr

    projection_expression = ", ".join(expr_parts)
    return projection_expression, expr_names

def batch_get_items(
    table,
    keys,
    attributes,
    env='dev',
    batch_size=100,
    max_retries=5,
    backoff_base=0.2,
):
    try:
        table_name = f'{env}-{table}'
        if batch_size > 100:
            raise ValueError("DynamoDB batch_get_item max batch size is 100")

        projection_expression, expression_attribute_names = (
            build_projection_expression(attributes)
        )

        all_items = []

        for key_batch in chunked(keys, batch_size):
            request_items = {
                table_name: {
                    "Keys": key_batch
                }
            }

            if projection_expression:
                request_items[table_name]["ProjectionExpression"] = projection_expression
                request_items[table_name]["ExpressionAttributeNames"] = expression_attribute_names

            retries = 0
            while request_items:
                response = dynamodb.batch_get_item(RequestItems=request_items)

                items = response.get("Responses", {}).get(table_name, [])
                all_items.extend(items)

                request_items = response.get("UnprocessedKeys")

                if request_items:
                    if retries >= max_retries:
                        raise RuntimeError("Max retries exceeded for UnprocessedKeys")

                    time.sleep(backoff_base * (2 ** retries))
                    retries += 1

        return all_items
    except Exception as e:
        print(e)
        raise e



def get_route_data(item_id, env = 'dev'):
    try:
        target_table = f'{env}-{table_name}'
        table = dynamodb.Table(target_table)
        # Fetch the item from DynamoDB by id
        response = table.get_item(Key={'id': item_id})

        if 'Item' not in response:
            return None

        item = response['Item']
        return item

    except ClientError as e:
        logging.info('Error while fetching route data')
        return None


def get_record(table_name, key, attributes, env = 'dev'):
    try: 
        target_table = f'{env}-{table_name}'
        print(f'target_table --> {target_table}')
        table = dynamodb.Table(target_table)
        attributeMap = {}
        attributePlaceholders = []
        for idx, attribute in enumerate(attributes):
            placeholder = f'#attr{idx}'
            attributePlaceholders.append(placeholder)
            attributeMap[placeholder] = attribute
        attributeStr = ', '.join(attributePlaceholders)
        
        print(f'attributeStr --> {attributeStr}')
        print(f'attributeMap --> {attributeMap}')
        print(f'key --> {key}')
        response = table.get_item(
            Key=key,
            ProjectionExpression=attributeStr,
            ExpressionAttributeNames=attributeMap
        )   
        if 'Item' not in response:
            return None

        item = response['Item']
        return item
    except Exception as e:
        logging.info(e)
        logging.info('Error while fetching record from Dynamo DB')
        return None



def store_detected_directions(data, key, env = 'dev'):
    try:
        target_table = f'{env}-{table_name}'
        table = dynamodb.Table(target_table)
        table.update_item(
            Key={
                'id': key
            },
            UpdateExpression="set newSourceCaption = :r",
            ExpressionAttributeValues={
                ':r': data,
            },
        )
        return True
    except Exception as e:
        logging.info(e)
        logging.info('Error while storing detected directions in Dynamo DB')
        return None

def update_route_field(key, field, value, env = 'dev'):
    try:
        target_table = f'{env}-{table_name}'
        table = dynamodb.Table(target_table)
        table.update_item(
            Key={
                'id': key
            },
            UpdateExpression="set #field = :r",
            ExpressionAttributeValues= {
                ':r': value,
            },
            ExpressionAttributeNames= {
                '#field': field
            }
        )
        return True
    except Exception as e:
        logging.info('Error while storing detected directions in Dynamo DB')
        return False


def update_record(table_name, key, data: dict, env='dev'):
    """
    Update multiple fields in a DynamoDB item.
    
    :param key: Partition key of the item
    :param data: dict of { field_name: field_value }
    :param env: environment prefix
    :return: True/False
    """
    try:
        target_table = f'{env}-{table_name}'
        table = dynamodb.Table(target_table)

        # Build ExpressionAttributeNames and Values
        expression_attribute_names = {}
        expression_attribute_values = {}
        update_expr_parts = []

        for idx, (field, value) in enumerate(data.items()):
            placeholder_name = f"#f{idx}"
            placeholder_value = f":v{idx}"

            expression_attribute_names[placeholder_name] = field
            expression_attribute_values[placeholder_value] = value
            update_expr_parts.append(f"{placeholder_name} = {placeholder_value}")

        update_expression = "SET " + ", ".join(update_expr_parts)

        table.update_item(
            Key=key,
            UpdateExpression=update_expression,
            ExpressionAttributeNames=expression_attribute_names,
            ExpressionAttributeValues=expression_attribute_values
        )

        return True
    except Exception as e:
        logging.info(f"Error while updating fields in DynamoDB: {e}")
        return False




def download_file_from_s3(bucket_name, object_key, download_path):
    # Create an S3 client using Boto3
    s3 = boto3.client('s3')
    try:
        # Download the file from S3 to the specified local path
        s3.download_file(bucket_name, object_key, download_path)
        logging.info(f"Download successful: {object_key} has been downloaded to {download_path}")
        return True
    except Exception as e:
        logging.info(f"Error downloading file: {e}")
        return False

def s3_file_exists(bucket_name, object_key):
    s3 = boto3.client('s3')
    try:
        s3.head_object(Bucket=bucket_name, Key=object_key)
        return True
    except Exception as e:
        return False
    

def check_exists(bucket, key):
    s3 = boto3.client('s3')
    try:
        s3.head_object(Bucket=bucket, Key=key)
        return key, True
    except Exception as e:
        return key, False

def check_multiple_objects(bucket, keys, max_workers=10):
    results = {}
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(check_exists, bucket, key): key for key in keys}
        for future in futures:
            key, exists = future.result()
            results[key] = exists
    return results

def download_multiple_files(bucket_name, files_to_download, download_dir, route_id = None, max_workers=10):
    """
    :param bucket_name: S3 bucket name
    :param files_to_download: List of object keys (file names in S3)
    :param download_dir: Local directory to save downloaded files
    :param max_workers: Number of parallel threads
    :return: Dict of {file_name: True/False}
    """
    results = {}

    def download_wrapper(object_key):
        file_name = object_key.split('/')[-1] if route_id == None else f"{route_id}-{object_key.split('/')[-1]}"
        local_path = f"{download_dir}/{file_name}"  # Customize as needed
        success = download_file_from_s3(bucket_name, object_key, local_path)
        return object_key, success

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(download_wrapper, key) for key in files_to_download]
        for future in as_completed(futures):
            key, success = future.result()
            results[key] = success

    return results


def upload_video_to_s3(file_path, bucket_name, object_name=None, env='dev', path= 'routes'):
    """
    Upload a video file to an S3 bucket.

    :param file_path: Path to the video file to upload
    :param bucket_name: S3 bucket name
    :param object_name: S3 object name (can be the same as file_name or a custom name)
    """
    # Create an S3 client using Boto3
    s3 = boto3.client('s3')
    if object_name is None:
        object_name = file_path.split('/')[-1]  # Use the file name as the S3 object name

    try:
        # Upload the file to S3
        s3.upload_file(file_path, bucket_name, f'{env}/{path}/{object_name}')
        logging.info(f"Upload Successful: {file_path} to {bucket_name}/{env}/{path}/{object_name}")
        return True
    except FileNotFoundError as e:
        print(e)
        logging.info(f"Error: The file {file_path} was not found.")
        return False
    except NoCredentialsError as e:
        print(e)
        logging.info("Error: No AWS credentials found.")
        return False
    except PartialCredentialsError as e:
        print(e)
        logging.info("Error: Incomplete AWS credentials.")
        return False
    except Exception as e:
        logging.info(f"Error uploading file: {e}")
        return False


def upload_file_to_s3(file_path, bucket_name, object_name):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_path, bucket_name, object_name)
        logging.info(f"Uploaded: {file_path} → s3://{bucket_name}/{object_name}")
        return True
    except Exception as e:
        logging.error(f"Error uploading {file_path}: {e}")
        return False

def upload_multiple_files(file_object_pairs, bucket_name, max_workers=10):
    """
    :param file_object_pairs: List of tuples: (local_path, s3_object_key)
    :param bucket_name: Target S3 bucket
    :param max_workers: Number of parallel uploads
    """
    results = {}

    def upload_wrapper(file_path, object_key):
        success = upload_file_to_s3(file_path, bucket_name, object_key)
        return file_path, success

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(upload_wrapper, file_path, object_key)
            for file_path, object_key in file_object_pairs
        ]
        for future in as_completed(futures):
            file_path, success = future.result()
            results[file_path] = success

    return results

def get_average_cpu_utilization(interval=1, times=5):
    cpu_usages = []
    
    # Collect CPU usage over the specified times
    for _ in range(times):
        # Get CPU usage percentage for the system over the interval
        cpu_usage = psutil.cpu_percent(interval=interval)
        cpu_usages.append(cpu_usage)
        
    # Calculate and return the average CPU usage
    average_cpu_usage = sum(cpu_usages) / len(cpu_usages)
    return average_cpu_usage


def update_automation_time(route_id, env='dev'):
    try:
        current_time = int(time.time())*1000
        update_route_field(route_id, 'automationUpdateAt', current_time, env)
    except Exception as e:
        print('Error while storing time')
        return None


def get_location_data(item_id, env='dev', fields=['id']):
    try:
        target_table = f'{env}-Locations'
        table = dynamodb.Table(target_table)

        params = {
            'Key': {'id': item_id}
        }

        if fields:
            expression_attribute_names = {}
            projection_expression_parts = []

            for field in fields:
                alias = f'#{field}'
                expression_attribute_names[alias] = field
                projection_expression_parts.append(alias)

            params['ProjectionExpression'] = ', '.join(projection_expression_parts)
            params['ExpressionAttributeNames'] = expression_attribute_names

        response = table.get_item(**params)

        if 'Item' not in response:
            return None

        return response['Item']

    except Exception as e:
        logging.info(f'Error while fetching route data: {e}')
        return None


def get_video_duration(path):
    result = subprocess.run(
        [
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            path
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    return float(result.stdout.strip())

