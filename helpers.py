import boto3
import logging
logging.basicConfig(level=logging.INFO)

# Initialize DynamoDB resource using boto3
dynamodb = boto3.resource('dynamodb')
table_name = 'dev-Routes'

# Define a DynamoDB table (You can create the table manually in AWS or use boto3 to create it)
table = dynamodb.Table(table_name)


def get_route_data(item_id):
    try:
        # Fetch the item from DynamoDB by id
        response = table.get_item(Key={'id': item_id})

        if 'Item' not in response:
            return None

        item = response['Item']
        return item

    except ClientError as e:
        logging.info('Error while fetching route data')
        return None


def store_detected_directions(data, key):
    try:
        table.update_item(
            Key={
                'id': key
            },
            UpdateExpression="set detectedDirections = :r",
            ExpressionAttributeValues={
                ':r': data,
            },
        )
        return True
    except Exception as e:
        logging.info('Error while storing detected directions in Dynamo DB')
        return None

def update_route_field(key, field, value):
    try:
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
        return None




def download_video_from_s3(bucket_name, object_key, download_path):
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

def upload_video_to_s3(file_path, bucket_name, object_name=None):
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
        s3.upload_file(file_path, bucket_name, object_name)
        logging.info(f"Upload Successful: {file_path} to {bucket_name}/{object_name}")
    except FileNotFoundError:
        logging.info(f"Error: The file {file_path} was not found.")
    except NoCredentialsError:
        logging.info("Error: No AWS credentials found.")
    except PartialCredentialsError:
        logging.info("Error: Incomplete AWS credentials.")
    except Exception as e:
        logging.info(f"Error uploading file: {e}")