import os

import uuid
import subprocess

from flask import  jsonify
from animation_gif_helpers import manage_colored_gifs
from blur_automate import blurVideo
from direction_detection import directionDetection
from helpers import create_record, download_file_from_s3, get_video_duration, update_record, upload_video_to_s3, update_route_field, check_multiple_objects, update_automation_time, download_multiple_files, get_location_data, get_record, batch_get_items, get_current_time

from arrow_animations import animate_arrow_gifs
from diy_segment_helpers import join_vids
from text_blur import text_blur_main
from tint_color import tint_image
import logging
logging.basicConfig(level=logging.INFO)
import copy
from constants import Tables, S3_PATHS, Media_Basics, PROCESS_STATUS, ROUTE_ACTION_STATUS
import time
import psutil
from celery_app import app


bucket_name = 'media.rtme.us'


def monitor_system(interval=5):
    psutil.cpu_percent()

    while True:
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        logging.info(
            f"[SYSTEM] CPU:{cpu}% RAM:{ram}% DISK:{disk}%"
        )

        time.sleep(interval)


# Start monitoring in background
# monitor_thread = threading.Thread(target=monitor_system, args=(5,), daemon=True)
# monitor_thread.start()


old_arrow_path = 'old_arrows/'
gif_path = 'newGifs/'
colored_gif_path = 'colored_gifs/'
files = os.listdir(old_arrow_path)
def manageColoredArrows(location_color_hex, env='dev'):
    try:
        if location_color_hex == None: return None
        
        hex_color = location_color_hex.lstrip('#')

        file_paths = [os.path.join('images', f'{hex_color}-{file_name}') for file_name in files]
        all_files_available_locally = True

        for file_path in file_paths:
            if os.path.isfile(file_path) == False:
                all_files_available_locally = False
                break


        if all_files_available_locally == True:
            print('Image found locally')
        else:
            keys = [
                f'{env}/location_arrows/{hex_color}-{file_name}' for file_name in files
            ]
            res = check_multiple_objects(bucket_name, keys)
            all_objects_available = True
            for value in res.values():
                if value == False:
                    all_objects_available = False
                    break
            if all_objects_available == True:
                download_res = download_multiple_files(bucket_name, keys, 'images')
                all_objects_saved = True
                for value in download_res.values():
                    if value == False:
                        all_objects_saved = False
                        break
                print('Image found in S3')
                if all_objects_saved == False:
                    arrow_color_success = tint_image(location_color_hex, env)
                    if arrow_color_success != True:
                        raise Exception('Arrow color error')    
            else:
                print('Arrow file needs to be generated')
                arrow_color_success = tint_image(location_color_hex, env)
                if arrow_color_success != True:
                    raise Exception('Arrow color error')
    except Exception as e:
        raise Exception('Arrow color error')



@app.task()
def arrowAttachAPI(data):
    file_name = None
    route_id = None
    env = 'dev'
    diy_route_key = {
        'stationId': None,
        'id': None
    }
    route_key = {
        'id': None
    }
    diy_segment_key = {
        'id': None,
        'locationId': None
    }
    is_diy_route_req = False
    is_diy_segment_req = False
    try:
        if data['env'] != None:
            env = data['env']

        # ---- Idempotency check ---- 
        idempotency_key = data.get('idempotency_key', None)   
        if idempotency_key == None:
            logging.info('Idempotency key not found')
            return
        create_success = create_record(
            table_name=f'{env}-{Tables.IDEMPOTENCY_KEYS}',
            part_key_name="id",
            part_key_value=idempotency_key,
            attributes={"createdAt": get_current_time()},
            ttl_seconds=86400, # 24 hrs
        )

        if create_success == False:
            # duplicate request
            logging.info('Duplicate request')
            return
        # ---- End Idempotency check ---- 
            

        route_id = data['route_id']

        if data.get('is_diy_route_req', False) == True:
            is_diy_route_req = True
            splits = route_id.split('#')
            diy_route_key['stationId'] = splits[0]
            diy_route_key['id'] = splits[1]
        elif data.get('is_diy_segment_req', False) == True:
            is_diy_segment_req = True
            splits = route_id.split('#')
            diy_segment_key['locationId'] = splits[0]
            diy_segment_key['id'] = splits[1]
        else:
            route_key['id'] = route_id

        req_attributes = [
            'videoURL',
            'locationId' if (is_diy_route_req == True or is_diy_segment_req == True) else 'locId',
            'totalDuration',
        ]

        if (is_diy_route_req == True or is_diy_segment_req == True):
            req_attributes.append('directions')
        else:
            req_attributes.append('sourceCaption')
            req_attributes.append('newSourceCaption')
            req_attributes.append('newLanguageCaptions')
            req_attributes.append('showAnimationsChanged')
            req_attributes.append('reRunArrowAttach')

        route_data = get_record(
            Tables.DIY_ROUTES if is_diy_route_req == True else Tables.DIY_SEGMENTS if is_diy_segment_req == True else Tables.ROUTES, 
            diy_route_key if is_diy_route_req == True else diy_segment_key if is_diy_segment_req == True else route_key, 
            req_attributes, 
            env
        )

        if route_data == None:
            raise Exception('Route not found')
        arrowAttachJob(data, route_data)
        return
    except Exception as e:
        logging.info('Error in arrow attach fn')
        logging.info(e)
        try:
            update_db_success = update_record(
                Tables.DIY_ROUTES if is_diy_route_req == True else Tables.DIY_SEGMENTS if is_diy_segment_req == True else Tables.ROUTES, 
                diy_route_key if is_diy_route_req == True else diy_segment_key if is_diy_segment_req == True else route_key, 
                {
                    'processStatus': PROCESS_STATUS.ARROW_ATTACHMENT_ERROR, 
                    'automationUpdateAt': get_current_time(),
                    'actionStatus': ROUTE_ACTION_STATUS.UPDATE_FAILED,
                }, 
                env
            )
            if update_db_success == False:
                raise Exception('Error while updating route in DB')
        except Exception as e:
            logging.info('Error while updating route in DB')
            logging.info(e)
        raise Exception("Error while processing Arrow animation") 

def arrowAttachJob(data, route_data):
    route_id = None
    file_name = None
    env = 'dev'
    hex_color = None
    diy_route_key = {
        'stationId': None,
        'id': None
    }
    diy_segment_key = {
        'locationId': None,
        'id': None
    }
    route_key = {
        'id': None
    }
    is_diy_route_req = False
    is_diy_segment_req = False
    try:
        route_id = data['route_id']
        if data['env'] != None:
            env = data['env']

        if data.get('is_diy_route_req', False) == True:
            is_diy_route_req = True
            splits = route_id.split('#')
            diy_route_key['stationId'] = splits[0]
            diy_route_key['id'] = splits[1]
        elif data.get('is_diy_segment_req', False) == True:
            is_diy_segment_req = True
            splits = route_id.split('#')
            diy_segment_key['locationId'] = splits[0]
            diy_segment_key['id'] = splits[1]
        else:
            route_key['id'] = route_id

        
        update_db_success = update_record(
            Tables.DIY_ROUTES if is_diy_route_req == True else Tables.DIY_SEGMENTS if is_diy_segment_req == True else Tables.ROUTES, 
            diy_route_key if is_diy_route_req == True else diy_segment_key if is_diy_segment_req == True else route_key, 
            {
                'processStatus': PROCESS_STATUS.ARROW_ATTACHMENT_START, 
                'automationUpdateAt': get_current_time(),
            }, 
            env
        )
        if update_db_success == False:
            raise Exception('Error while updating route in DB')
        new_route = False
        existingSourceCaption = route_data['sourceCaption' if (is_diy_route_req == False and is_diy_segment_req == False) else 'directions']
        showAnimationsChanged = None if (is_diy_route_req == False and is_diy_segment_req == False) else route_data.get('showAnimationsChanged', False)
        reRunArrowAttach = None if (is_diy_route_req == False and is_diy_segment_req == False) else route_data.get('reRunArrowAttach', True)
        total_duration = route_data.get('totalDuration', None)

        if showAnimationsChanged == None:
            showAnimationsChanged = False
        if reRunArrowAttach == None:
            reRunArrowAttach = True

        if existingSourceCaption == None or len(existingSourceCaption) == 0:
            new_route = True

        
        update_db_success = update_record(
            Tables.DIY_ROUTES if is_diy_route_req == True else Tables.DIY_SEGMENTS if is_diy_segment_req == True else Tables.ROUTES, 
            diy_route_key if is_diy_route_req == True else diy_segment_key if is_diy_segment_req == True else route_key, 
            {
                'processStatus': PROCESS_STATUS.ARROW_ATTACHMENT_START, 
                'automationUpdateAt': get_current_time(),
            }, 
            env
        )
        if update_db_success == False:
            raise Exception('Error while updating route in DB')
        video_url = route_data.get('videoURL')
        file_name = video_url.split('/')[-1]
        logging.info('download of video started')
        download_file_from_s3(
            bucket_name, 
            f'{env}/{S3_PATHS.DIY_ROUTES if is_diy_route_req == True else S3_PATHS.DIY_SEGMENTS if is_diy_segment_req == True else S3_PATHS.ROUTES}/{file_name}', 
            f'blurred/{file_name}'
        )
        logging.info('download done')

        video_duration = 0
        if total_duration == None:
            try:
                video_duration = get_video_duration(f'blurred/{file_name}')
            except Exception as e:
                print(e)
        
        final_directions = copy.deepcopy(
            route_data.get('directions') if (is_diy_route_req == True or is_diy_segment_req == True)
            else route_data.get('newSourceCaption') if reRunArrowAttach == True 
            else route_data.get('sourceCaption')
        )
        
        logging.info('Arrow attachment start')
        location_id = route_data.get('locId' if is_diy_route_req == False else 'locationId')
        location_data = get_location_data(location_id, env, ['id', 'locationColor'])
        location_color_hex = None
        if location_data != None:
            color = location_data.get('locationColor')
            if color != None:
                location_color_hex = color

        if location_color_hex != None:    
            hex_color = location_color_hex.lstrip('#')
            manage_colored_gifs(hex_color, route_id, env)

        animate_arrow_gifs(route_id, file_name, final_directions, hex_color)

        # Change the video codec for making the video small in size
        # ffmpeg -i input.mp4 -c:v libx264 -c:a copy output_h264.mp4
        change_codec_command = ["ffmpeg", "-i", f'final/{file_name}', '-c:v', 'libx264', '-c:a', 'copy', f'final/codec_{file_name}']
        result_dim = subprocess.run(change_codec_command, check=True, capture_output=True, text=True)
        logging.info("Command Output codec:", result_dim.stdout)
        logging.info("Command Error Output codec:", result_dim.stderr)

        new_file_name = f'processed_{file_name}'
        new_link = f'https://media.rtme.us/{env}/{S3_PATHS.DIY_ROUTES if is_diy_route_req == True else S3_PATHS.DIY_SEGMENTS if is_diy_segment_req == True else S3_PATHS.ROUTES}/{new_file_name}'
        db_update_success = False
        db_update_success = upload_video_to_s3(
            f'final/codec_{file_name}', 
            bucket_name, 
            new_file_name, 
            env, 
            S3_PATHS.DIY_ROUTES if is_diy_route_req == True else S3_PATHS.DIY_SEGMENTS if is_diy_segment_req == True else S3_PATHS.ROUTES
        )
        if db_update_success == False:
            raise Exception('DB update error')
        if reRunArrowAttach == True:
            update_data = {
                'processedVideoLink': new_link,
                'processStatus': PROCESS_STATUS.ARROW_ATTACHMENT_SUCCESS
            }
            if is_diy_route_req == False and is_diy_segment_req == False:
                update_data['sourceCaption'] = route_data.get('newSourceCaption')
                update_data['languageCaptions'] = route_data.get('newLanguageCaptions')

            if total_duration == None:
                update_data['totalDuration'] = int(video_duration)
            
            db_update_success = update_record(
                Tables.DIY_ROUTES if is_diy_route_req == True else Tables.DIY_SEGMENTS if is_diy_segment_req == True else Tables.ROUTES, 
                diy_route_key if is_diy_route_req == True else diy_segment_key if is_diy_segment_req == True else route_key, 
                update_data, 
                env
            )
            if db_update_success == False:
                raise Exception('DB update error')
        elif reRunArrowAttach == False and showAnimationsChanged == True:
            update_data = {
                'showAnimationsChanged': None,
                'reRunArrowAttach': None,
                'processStatus': PROCESS_STATUS.ARROW_ATTACHMENT_SUCCESS
            }
            if total_duration == None:
                update_data['totalDuration'] = int(video_duration)
            db_update_success = update_record(Tables.ROUTES, {"id": route_id}, update_data, env)
            if db_update_success == False:
                raise Exception('DB update error')
    except Exception as e:
        logging.info('Error while processing arrow attachment')
        print(e)
        try:
            db_update_success = update_record(
                Tables.DIY_ROUTES if is_diy_route_req == True else Tables.DIY_SEGMENTS if is_diy_segment_req == True else Tables.ROUTES, 
                diy_route_key if is_diy_route_req == True else diy_segment_key if is_diy_segment_req == True else route_key, 
                {
                    'processStatus': PROCESS_STATUS.ARROW_ATTACHMENT_ERROR,
                    'automationUpdateAt': get_current_time()
                }, 
                env
            )
            if db_update_success == False:
                raise Exception('DB update error')
        except Exception as e:
            logging.info('Error while updating DB')
            print(e)
    finally:
        try:
            os.remove(f'blurred/{file_name}')
        except Exception as e:
            print('Error removing file')
        try:
            os.remove(f'final/{file_name}')
        except Exception as e:
            print('Error removing file')
        try:
            os.remove(f'final/codec_{file_name}')
        except Exception as e:
            print('Error removing file')

        if hex_color != None:
            # remove the colored gifs
            colored_gif_files = os.listdir(gif_path)
            for file in colored_gif_files:
                try:
                    file_name = f'{route_id}-{hex_color}-{file}'
                    os.remove(f'{colored_gif_path}{file_name}')
                except Exception as e:
                    print(e)
    

@app.task()
def textBlurAPI(data):
    file_name = None
    route_id = None
    env = 'dev'
    diy_route_key = {
        'stationId': None,
        'id': None
    }
    route_key = {
        'id': None
    }
    diy_segment_key = {
        'id': None,
        'locationId': None
    }
    is_diy_route_req = False
    is_diy_segment_req = False
    try:
        if data['env'] != None:
            env = data['env']
        route_id = data['route_id']

        if data.get('is_diy_route_req', False) == True:
            is_diy_route_req = True
            splits = route_id.split('#')
            diy_route_key['stationId'] = splits[0]
            diy_route_key['id'] = splits[1]
        elif data.get('is_diy_segment_req', False) == True:
            is_diy_segment_req = True
            splits = route_id.split('#')
            diy_segment_key['locationId'] = splits[0]
            diy_segment_key['id'] = splits[1]
        else:
            route_key['id'] = route_id
        
        # ---- Idempotency check ---- 
        idempotency_key = data.get('idempotency_key', None)   
        if idempotency_key == None:
            logging.info('Idempotency key not found')
            return
        create_success = create_record(
            table_name=f'{env}-{Tables.IDEMPOTENCY_KEYS}',
            part_key_name="id",
            part_key_value=idempotency_key,
            attributes={"createdAt": get_current_time()},
            ttl_seconds=86400, # 24 hrs
        )

        if create_success == False:
            # duplicate request
            logging.info('Duplicate request')
            return
        # ---- End Idempotency check ---- 
        
        req_attributes = ['textBlurJsonFileName', 'videoURL']
        route_data = get_record(
            Tables.DIY_ROUTES if is_diy_route_req == True else Tables.DIY_SEGMENTS if is_diy_segment_req == True else Tables.ROUTES, 
            diy_route_key if is_diy_route_req == True else diy_segment_key if is_diy_segment_req == True else route_key, 
            req_attributes, 
            env
        )
        if route_data == None:
            data = {
                "message": "Route not found"
            }
            return jsonify(data), 404 

        update_db_success = update_record(
            Tables.DIY_ROUTES if is_diy_route_req == True else Tables.DIY_SEGMENTS if is_diy_segment_req == True else Tables.ROUTES, 
            diy_route_key if is_diy_route_req == True else diy_segment_key if is_diy_segment_req == True else route_key, 
            {
                'processStatus': PROCESS_STATUS.TEXT_BLUR_START, 
                'automationUpdateAt': get_current_time(),
            }, 
            env
        )
        if update_db_success == False:
            raise Exception('Error while updating route in DB')

        textBlurJob(data, route_data)
        return 
    except Exception as e:
        update_route_field(route_id, 'processStatus', 'TEXT_BLUR_ERROR', env)
        update_automation_time(route_id, env)
        print('Error in text blur')
        print(e)
        raise Exception("Error while processing json file for text blur")



def textBlurJob(data, route_data):
    route_id = None
    file_name = None
    env = 'dev'
    hex_color = None
    diy_route_key = {
        'stationId': None,
        'id': None
    }
    diy_segment_key = {
        'locationId': None,
        'id': None
    }
    route_key = {
        'id': None
    }
    is_diy_route_req = False
    is_diy_segment_req = False
    try:
        if data['env'] != None:
            env = data['env']
        db_update_success = False
        route_id = data['route_id']

        route_id = data['route_id']
        if data['env'] != None:
            env = data['env']

        if data.get('is_diy_route_req', False) == True:
            is_diy_route_req = True
            splits = route_id.split('#')
            diy_route_key['stationId'] = splits[0]
            diy_route_key['id'] = splits[1]
        elif data.get('is_diy_segment_req', False) == True:
            is_diy_segment_req = True
            splits = route_id.split('#')
            diy_segment_key['locationId'] = splits[0]
            diy_segment_key['id'] = splits[1]
        else:
            route_key['id'] = route_id
        
        json_file_path = route_data['textBlurJsonFileName']
        if json_file_path == None:
            raise Exception('Text blur file not found')
        
        video_url = route_data.get('videoURL')
        if video_url == None:
            raise Exception('Route Video not found')
            print('Route Video not found')
        file_name = video_url.split('/')[-1]
        print('Started downloading the Video File to be processed')
        download_s3_path = S3_PATHS.DIY_ROUTES if is_diy_route_req == True else S3_PATHS.DIY_SEGMENTS if is_diy_segment_req == True else S3_PATHS.ROUTES 
        db_update_success = download_file_from_s3(
            bucket_name, 
            f'{env}/{download_s3_path}/{file_name}', 
            f'inputs/{file_name}'
        )
        
        # Download the Google's Video Intelligence text-blur output stored in the AWS-S3
        json_file_name = json_file_path.split('/')[-1]
        db_update_success = download_file_from_s3(bucket_name, f'{env}/{json_file_path}', f'text_json/{json_file_name}')
        if db_update_success == False:
            raise Exception('DB update failed')

        # Start the text blur script
        blur_success = text_blur_main(file_name, json_file_name)

        if blur_success == False:
            print('Error while blurrig text')
            raise Exception('Error while blurrig text')
            return
        else:
            # Upload the text-blurred video to S3
            change_codec_command = ["ffmpeg", "-i", f'final/{file_name}', '-c:v', 'libx264', '-c:a', 'copy', f'final/codec_{file_name}']
            result_dim = subprocess.run(change_codec_command, check=True, capture_output=True, text=True)    
            db_update_success = upload_video_to_s3(
                f'final/codec_{file_name}', 
                bucket_name, 
                file_name, 
                env,
                S3_PATHS.DIY_ROUTES if is_diy_route_req == True else S3_PATHS.DIY_SEGMENTS if is_diy_segment_req == True else S3_PATHS.ROUTES
            )
            if db_update_success == False:
               raise Exception('DB update failed')
            # Remove file from local
            os.remove(f'final/{file_name}')
            os.remove(f'final/codec_{file_name}')
            update_db_success = update_record(
                Tables.DIY_ROUTES if is_diy_route_req == True else Tables.DIY_SEGMENTS if is_diy_segment_req == True else Tables.ROUTES, 
                diy_route_key if is_diy_route_req == True else diy_segment_key if is_diy_segment_req == True else route_key, 
                {
                    'processStatus': PROCESS_STATUS.TEXT_BLUR_SUCCESS, 
                    'automationUpdateAt': get_current_time(),
                }, 
                env
            )
            if db_update_success == False:
                raise Exception('DB update failed')
            return
    except Exception as e:
        try:
            update_db_success = update_record(
                Tables.DIY_ROUTES if is_diy_route_req == True else Tables.DIY_SEGMENTS if is_diy_segment_req == True else Tables.ROUTES, 
                diy_route_key if is_diy_route_req == True else diy_segment_key if is_diy_segment_req == True else route_key, 
                {
                    'processStatus': PROCESS_STATUS.TEXT_BLUR_ERROR, 
                    'automationUpdateAt': get_current_time(),
                }, 
                env
            )
            if db_update_success == False:
                raise Exception('DB update failed')
        except Exception as e:
            print('Error while updating route in DB')
            
        print('Error in text blur')
        print(e)
        return "Error while processing json file", 500


# @app.route('/check-health')
# def cpuCheck():
#     return "[Updated again 12] Server says hii", 200
    # avg_cpu = get_average_cpu_utilization(interval=1, times=2)
    # logging.info(f'Average CPU => {avg_cpu}')
    # if avg_cpu > 80:
    #     return "", 500
    # else:    
    #     return "", 200

@app.task()
def faceBlurAPI(data):
    route_id = None
    env = 'dev'
    diy_route_key = {
        'stationId': None,
        'id': None
    }
    route_key = {
        'id': None
    }
    diy_segment_key = {
        'id': None,
        'locationId': None
    }
    is_diy_route_req = False
    is_diy_segment_req = False
    try:
        if data['env'] != None:
            env = data['env']
        route_id = data['route_id']

        if data.get('is_diy_route_req', False) == True:
            is_diy_route_req = True
            splits = route_id.split('#')
            diy_route_key['stationId'] = splits[0]
            diy_route_key['id'] = splits[1]
        elif data.get('is_diy_segment_req', False) == True:
            is_diy_segment_req = True
            splits = route_id.split('#')
            diy_segment_key['locationId'] = splits[0]
            diy_segment_key['id'] = splits[1]
        else:
            route_key['id'] = route_id

        # ---- Idempotency check ---- 
        idempotency_key = data.get('idempotency_key', None)   
        if idempotency_key == None:
            logging.info('Idempotency key not found')
            return
        create_success = create_record(
            table_name=f'{env}-{Tables.IDEMPOTENCY_KEYS}',
            part_key_name="id",
            part_key_value=idempotency_key,
            attributes={"createdAt": get_current_time()},
            ttl_seconds=86400, # 24 hrs
        )

        if create_success == False:
            # duplicate request
            logging.info('Duplicate request')
            return
        # ---- End Idempotency check ---- 

        route_data = get_record(
            Tables.DIY_ROUTES if is_diy_route_req == True else Tables.DIY_SEGMENTS if is_diy_segment_req == True else Tables.ROUTES, 
            diy_route_key if is_diy_route_req == True else diy_segment_key if is_diy_segment_req == True else route_key, 
            ['videoURL'], 
            env
        )
        if route_data == None:
            raise Exception('Route not found')
        
        faceBlurJob(data, route_data)
        return
    except Exception as e:
        print('Error in face blur')
        print(e)
        # TODO: update here
        update_route_field(route_id, 'processStatus', 'FACE_BLUR_ERROR', env)
        # update_automation_time(route_id, env)
        raise Exception("Error while processing face blur")



def faceBlurJob(data, route_data):
    route_id = None
    file_name = None
    env = 'dev'
    
    diy_route_key = {
        'stationId': None,
        'id': None
    }
    route_key = {
        'id': None
    }
    diy_segment_key = {
        'id': None,
        'locationId': None
    }
    is_diy_route_req = False
    is_diy_segment_req = False
    try:
        route_id = data['route_id']
        blur = data.get('blur')
        if data['env'] != None:
            env = data['env']
        update_field_success = False

        if data.get('is_diy_route_req', False) == True:
            is_diy_route_req = True
            splits = route_id.split('#')
            diy_route_key['stationId'] = splits[0]
            diy_route_key['id'] = splits[1]
        elif data.get('is_diy_segment_req', False) == True:
            is_diy_segment_req = True
            splits = route_id.split('#')
            diy_segment_key['locationId'] = splits[0]
            diy_segment_key['id'] = splits[1]
        else:
            route_key['id'] = route_id

        # Need to run blur script, direction detection script and submit to route DB
        # 1) Download the video from s3 and save in local
        logging.info('Blurring start')
        update_field_success = update_record(
            Tables.DIY_ROUTES if is_diy_route_req == True else Tables.DIY_SEGMENTS if is_diy_segment_req == True else Tables.ROUTES, 
            diy_route_key if is_diy_route_req == True else diy_segment_key if is_diy_segment_req == True else route_key, 
            {
                'processStatus': PROCESS_STATUS.FACE_BLUR_START, 
                'automationUpdateAt': get_current_time()
            }, 
            env
        )
        
        if update_field_success == False:
            raise Exception('Update DB failed')
        video_url = route_data['videoURL']
        file_name = video_url.split('/')[-1]
        download_success = download_file_from_s3(
            bucket_name, 
            f'{env}/{S3_PATHS.DIY_ROUTES if is_diy_route_req == True else S3_PATHS.DIY_SEGMENTS if is_diy_segment_req == True else S3_PATHS.ROUTES}/{file_name}', 
            f'inputs/{file_name}'
        )
        if download_success == False:
            raise Exception('download failed')

        # 2) Blur the video
        blur_success = blurVideo(file_name)
        
        if blur_success != True:
            raise 'Blur error'
        logging.info('blur complete')

        update_record(
            Tables.DIY_ROUTES if is_diy_route_req == True else Tables.DIY_SEGMENTS if is_diy_segment_req == True else Tables.ROUTES, 
            diy_route_key if is_diy_route_req == True else diy_segment_key if is_diy_segment_req == True else route_key, 
            {
                'automationUpdateAt': get_current_time()
            }, 
            env
        )

        # 3) Upload blurred video to S3
        upload_success = upload_video_to_s3(
            f'blurred/{file_name}', 
            bucket_name, 
            None, 
            env, 
            S3_PATHS.DIY_ROUTES if is_diy_route_req == True else S3_PATHS.DIY_SEGMENTS if is_diy_segment_req == True else S3_PATHS.ROUTES
        )
        if upload_success == False:
            raise Exception('Upload failed')


        update_field_success = False
        update_field_success = update_record(
            Tables.DIY_ROUTES if is_diy_route_req == True else Tables.DIY_SEGMENTS if is_diy_segment_req == True else Tables.ROUTES, 
            diy_route_key if is_diy_route_req == True else diy_segment_key if is_diy_segment_req == True else route_key, 
            {
                'processStatus': PROCESS_STATUS.FACE_BLUR_SUCCESS, 
                'automationUpdateAt': get_current_time()
            }, 
            env
        )
        if update_field_success == False:
            raise Exception('Update DB failed')
    except Exception as e:
        update_field_success = False
        update_field_success = update_record(
            Tables.DIY_ROUTES if is_diy_route_req == True else Tables.DIY_SEGMENTS if is_diy_segment_req == True else Tables.ROUTES, 
            diy_route_key if is_diy_route_req == True else diy_segment_key if is_diy_segment_req == True else route_key, 
            {
                'processStatus': PROCESS_STATUS.FACE_BLUR_ERROR, 
                'automationUpdateAt': get_current_time()
            }, 
            env
        )
        if update_field_success == False:
            print('Update DB failed')
        print(e)
    finally:
        try:
            os.remove(f'blurred/{file_name}')
        except Exception as e:
            print('Error while removing blurred file from local')

@app.task()
def createRouteAPI(data):
    route_id = None
    env = 'dev'
    diy_route_key = {
        'stationId': None,
        'id': None
    }
    local_file_name = None
    try:
        if data['env'] != None:
            env = data['env']
        route_id = data['route_id']
        [station_id, diy_route_id] = route_id.split('#')
        diy_route_key['stationId'] = station_id
        diy_route_key['id'] = diy_route_id


        # ---- Idempotency check ---- 
        idempotency_key = data.get('idempotency_key', None)   
        if idempotency_key == None:
            logging.info('Idempotency key not found')
            return
        create_success = create_record(
            table_name=f'{env}-{Tables.IDEMPOTENCY_KEYS}',
            part_key_name="id",
            part_key_value=idempotency_key,
            attributes={"createdAt": get_current_time()},
            ttl_seconds=86400, # 24 hrs
        )

        if create_success == False:
            # duplicate request
            logging.info('Duplicate request')
            return
        # ---- End Idempotency check ---- 
        
        
        route_data = get_record(Tables.DIY_ROUTES, diy_route_key, ['stationId', 'id', 'status', 'segmentIds'], env)
        if route_data == None:
            raise Exception('Route not found')

        if (route_data.get('status', None) != 'SUBMITTED'):
            raise Exception('Route not submitted')

        update_record(Tables.DIY_ROUTES, diy_route_key, {'processStatus': 'ROUTE_CREATION_START'}, env)
        update_automation_time(route_id, env)

        segmentIds = route_data.get('segmentIds', [])
        segment_keys = []
        for segmentId in segmentIds:
            [location_id, id] = segmentId.split('#')
            segment_keys.append({'locationId': location_id, 'id': id})

        segment_data = batch_get_items(Tables.DIY_SEGMENTS, segment_keys, ['locationId', 'id', 'status', 'processedVideoLink'], env)
        video_urls = [x.get('processedVideoLink', None) for x in segment_data]
        
        new_id = str(uuid.uuid4())

        createRouteJob(diy_route_key, video_urls, new_id, env)
        
        return
    except Exception as e:
        print('Error in create route API')
        print(e)
        try:
            update_record(Tables.DIY_ROUTES, diy_route_key, {'processStatus': 'ROUTE_CREATION_ERROR'}, env)
        except Exception as e:
            print("Error while updating route status")
        raise Exception("Error while processing request")
    finally:
        # Remove the file from local storage
        try:
            os.remove(f'final/{local_file_name}')
        except Exception as e:
            print("Error while removing file from local storage")

def createRouteJob(diy_route_key, video_urls, new_id, env = 'dev'):
    try:
        local_file_name = f'{new_id}.mp4'

        # 1) Join the segments
        join_vids(video_urls, f'final/{local_file_name}')

        # 2) Upload video to S3
        upload_success = upload_video_to_s3(f'final/{local_file_name}', bucket_name, None, env, S3_PATHS.DIY_ROUTES)
        if upload_success == False:
            raise Exception('Upload failed')
        
        # 3) Update the route status
        video_url = f'{Media_Basics.MediaUrlPrefix}/{env}/{S3_PATHS.DIY_ROUTES}/{new_id}.mp4'
        update_record(
            Tables.DIY_ROUTES, 
            diy_route_key, 
            {'processStatus': PROCESS_STATUS.ROUTE_CREATION_SUCCESS, 'videoURL': video_url, 'actionStatus': ROUTE_ACTION_STATUS.CREATED}, 
            env
        )
    except Exception as e:
        print('Error in create route API')
        print(e)
        try:
            update_record(Tables.DIY_ROUTES, diy_route_key, {'processStatus': 'ROUTE_CREATION_ERROR'}, env)
        except Exception as e:
            print("Error while updating route status")
        return "Error while processing request", 500



@app.task()
def directionDetectionAPI(data):
    route_id = None
    env = 'dev'
    diy_route_key = {
        'stationId': None,
        'id': None
    }
    route_key = {
        'id': None
    }
    diy_segment_key = {
        'id': None,
        'locationId': None
    }
    is_diy_route_req = False
    is_diy_segment_req = False
    try:
        if data['env'] != None:
            env = data['env']
        route_id = data['route_id']

        if data.get('is_diy_route_req', False) == True:
            is_diy_route_req = True
            splits = route_id.split('#')
            diy_route_key['stationId'] = splits[0]
            diy_route_key['id'] = splits[1]
        elif data.get('is_diy_segment_req', False) == True:
            is_diy_segment_req = True
            splits = route_id.split('#')
            diy_segment_key['locationId'] = splits[0]
            diy_segment_key['id'] = splits[1]
        else:
            route_key['id'] = route_id


        # ---- Idempotency check ---- 
        idempotency_key = data.get('idempotency_key', None)   
        if idempotency_key == None:
            logging.info('Idempotency key not found')
            return
        create_success = create_record(
            table_name=f'{env}-{Tables.IDEMPOTENCY_KEYS}',
            part_key_name="id",
            part_key_value=idempotency_key,
            attributes={"createdAt": get_current_time()},
            ttl_seconds=86400, # 24 hrs
        )

        if create_success == False:
            # duplicate request
            logging.info('Duplicate request')
            return
        # ---- End Idempotency check ---- 

        route_data = get_record(
            Tables.DIY_ROUTES if is_diy_route_req == True else Tables.DIY_SEGMENTS if is_diy_segment_req == True else Tables.ROUTES, 
            diy_route_key if is_diy_route_req == True else diy_segment_key if is_diy_segment_req == True else route_key, 
            ['videoURL'], 
            env
        )

        if route_data == None:
            raise Exception('Route not found')

        directionDetectionJob(data, route_data)
        return
    except Exception as e:
        print('Error in direction detection')
        print(e)
        try:
            update_db_success = update_record(
                Tables.DIY_ROUTES if is_diy_route_req == True else Tables.DIY_SEGMENTS if is_diy_segment_req == True else Tables.ROUTES, 
                diy_route_key if is_diy_route_req == True else diy_segment_key if is_diy_segment_req == True else route_key, 
                {
                    'processStatus': PROCESS_STATUS.DIRECTION_DETECTION_ERROR, 
                    'automationUpdateAt': get_current_time(),
                    'actionStatus': ROUTE_ACTION_STATUS.UPDATE_FAILED,
                }, 
                env
            )
            if update_db_success == False:
                raise Exception('Error while updating route in DB')
        except Exception as e:
            print('Error while updating route in DB')
            print(e)
        raise Exception("Error while processing direction detection")

def directionDetectionJob(data, route_data):
    route_id = None
    file_name = None
    env = 'dev'
    diy_route_key = {
        'stationId': None,
        'id': None
    }
    route_key = {
        'id': None
    }
    diy_segment_key = {
        'id': None,
        'locationId': None
    }
    is_diy_route_req = False
    is_diy_segment_req = False
    try:
        if data['env'] != None:
            env = data['env']
        route_id = data['route_id']


        if data.get('is_diy_route_req', False) == True:
            is_diy_route_req = True
            splits = route_id.split('#')
            diy_route_key['stationId'] = splits[0]
            diy_route_key['id'] = splits[1]
        elif data.get('is_diy_segment_req', False) == True:
            is_diy_segment_req = True
            splits = route_id.split('#')
            diy_segment_key['locationId'] = splits[0]
            diy_segment_key['id'] = splits[1]
        else:
            route_key['id'] = route_id

        update_db_success = update_record(
            Tables.DIY_ROUTES if is_diy_route_req == True else Tables.DIY_SEGMENTS if is_diy_segment_req == True else Tables.ROUTES, 
            diy_route_key if is_diy_route_req == True else diy_segment_key if is_diy_segment_req == True else route_key, 
            {
                'processStatus': PROCESS_STATUS.DIRECTION_DETECTION_START, 
                'automationUpdateAt': get_current_time(),
            }, 
            env
        )
        if update_db_success == False:
            raise Exception('Error while updating route in DB')


        video_url = route_data['videoURL']
        file_name = video_url.split('/')[-1]
        download_success = download_file_from_s3(
            bucket_name, 
            f'{env}/{S3_PATHS.DIY_ROUTES if is_diy_route_req == True else S3_PATHS.DIY_SEGMENTS if is_diy_segment_req == True else S3_PATHS.ROUTES}/{file_name}', 
            f'blurred/{file_name}'
        )
        if download_success == False:
            raise Exception('download failed')
        logging.info('Starting the direction detection')
        final_directions = directionDetection(file_name)
        if final_directions == False:
            raise Exception('Error while generating directions')
        # Store these directions in dynamo table
        
        update_db_success = update_record(
            Tables.DIY_ROUTES if is_diy_route_req == True else Tables.DIY_SEGMENTS if is_diy_segment_req == True else Tables.ROUTES, 
            diy_route_key if is_diy_route_req == True else diy_segment_key if is_diy_segment_req == True else route_key, 
            {
                'processStatus': PROCESS_STATUS.DIRECTION_DETECTION_SUCCESS, 
                'automationUpdateAt': get_current_time(),
                'actionStatus': ROUTE_ACTION_STATUS.UPDATED,
                f'{"newSourceCaption" if is_diy_route_req == False and is_diy_segment_req == False else "directions"}': final_directions
            }, 
            env
        )

        if update_db_success == False:
            raise Exception('Error while updating route in DB')
        
        logging.info('Done :+1')
    except Exception as e:
        try:
            update_db_success = update_record(
                Tables.DIY_ROUTES if is_diy_route_req == True else Tables.DIY_SEGMENTS if is_diy_segment_req == True else Tables.ROUTES, 
                diy_route_key if is_diy_route_req == True else diy_segment_key if is_diy_segment_req == True else route_key, 
                {
                    'processStatus': PROCESS_STATUS.DIRECTION_DETECTION_ERROR, 
                    'automationUpdateAt': get_current_time(),
                    'actionStatus': ROUTE_ACTION_STATUS.UPDATE_FAILED,
                }, 
                env
            )
            if update_db_success == False:
                raise Exception('Error while updating route in DB')
        except Exception as e:
            print('Error while updating route in DB')
            print(e)
        print(e)
    finally:
        try:
            os.remove(f'blurred/{file_name}')
        except Exception as e:
            print('Error while removing blurred file from local')


