import os
import boto3
import subprocess
import threading
from datetime import datetime
from flask import Flask, request, jsonify
from blur_automate import blurVideo
from direction_detection import directionDetection
from botocore.exceptions import ClientError
from helpers import download_file_from_s3, get_route_data, upload_video_to_s3, store_detected_directions, update_route_field, check_multiple_objects, update_automation_time, download_multiple_files, get_location_data
from arrow_attachment import arrow_attachment_main
from arrow_animations import animate_arrow_gifs
import threading
from text_blur import text_blur_main
from tint_color import tint_image
import logging
logging.basicConfig(level=logging.INFO)
import copy



bucket_name = 'media.rtme.us'
app = Flask(__name__)
logging.info('Inside the server')


def manageColoredArrows(location_color_hex, env='dev'):
    try:
        if location_color_hex == None: return None
        
        hex_color = location_color_hex.lstrip('#')
        file_path = os.path.join('images', f'{hex_color}-left-arrow.png')
        if os.path.isfile(file_path):
            print('Image found locally')
        else:
            keys = [
                f'{env}/location_arrows/{hex_color}-left-arrow.png',
                f'{env}/location_arrows/{hex_color}-right-arrow.png',
                f'{env}/location_arrows/{hex_color}-straight-arrow.png',
                f'{env}/location_arrows/{hex_color}-slight-left-arrow.png',
                f'{env}/location_arrows/{hex_color}-slight-right-arrow.png',
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


@app.route('/arrow-attach', methods=['POST'])
def arrowAttachAPI():
    file_name = None
    route_id = None
    env = 'dev'
    try:
        data = request.get_json()
        if data['env'] != None:
            env = data['env']
        route_id = data['route_id']
        route_data = get_route_data(route_id, env)
        if route_data == None:
            data = {
                "message": "Route not found"
            }
            return jsonify(data), 404 
        update_route_field(route_id, 'processStatus', 'ARROW_ATTACHMENT_START', env)
        update_automation_time(route_id, env)
        thread = threading.Thread(target=arrowAttachJob, args=(data, route_data))
        thread.daemon = True  # This ensures the thread will be killed when the main program exits
        thread.start()
        res_data = {
            "message": "Route submitted for arrow-attach process"
        }
        return jsonify(res_data), 200 
    except Exception as e:
        update_route_field(route_id, 'processStatus', 'ARROW_ATTACHMENT_ERROR', env)
        print('Error in arrow attach fn')
        print(e)
        return "Error while processing json file", 500

def arrowAttachJob(data, route_data):
    route_id = None
    file_name = None
    env = 'dev'
    try:
        route_id = route_data['id']
        if data['env'] != None:
            env = data['env']
        new_route = False
        existingSourceCaption = route_data['sourceCaption']
        if existingSourceCaption == None or len(existingSourceCaption) == 0:
            new_route = True
        update_route_field(route_id, 'processStatus', 'ARROW_ATTACHMENT_START', env)
        update_automation_time(route_id, env)
        video_url = route_data.get('videoURL')
        file_name = video_url.split('/')[-1]
        logging.info('download of video started')
        download_file_from_s3(bucket_name, f'{env}/routes/{file_name}', f'blurred/{file_name}')
        logging.info('download done')
        final_directions = copy.deepcopy(route_data.get('newSourceCaption'))
        print('final_directions => ', final_directions)
        logging.info('Arrow attachment start')
        location_id = route_data.get('locId')
        location_data = get_location_data(location_id, env, ['id', 'locationColor'])
        location_color_hex = None
        if location_data != None:
            color = location_data.get('locationColor')
            if color != None:
                location_color_hex = color

        hex_color = None
        if location_color_hex != None:
            hex_color = location_color_hex.lstrip('#')
            manageColoredArrows(location_color_hex, env)

        if env == 'dev' or env == 'staging':
            animate_arrow_gifs(route_id, file_name, final_directions)
        else:
            arrow_attachment_main(file_name, final_directions, hex_color)

        # Change the video codec for making the video small in size
        # ffmpeg -i input.mp4 -c:v libx264 -c:a copy output_h264.mp4
        change_codec_command = ["ffmpeg", "-i", f'final/{file_name}', '-c:v', 'libx264', '-c:a', 'copy', f'final/codec_{file_name}']
        result_dim = subprocess.run(change_codec_command, check=True, capture_output=True, text=True)
        logging.info("Command Output codec:", result_dim.stdout)
        logging.info("Command Error Output codec:", result_dim.stderr)
        update_automation_time(route_id, env)

        new_file_name = f'processed_{file_name}'
        new_link = f'https://media.rtme.us/{env}/routes/{new_file_name}'
        db_update_success = False
        db_update_success = upload_video_to_s3(f'final/codec_{file_name}', bucket_name, new_file_name, env)
        if db_update_success == False:
            raise Exception('DB update error')

        db_update_success = update_route_field(route_id, 'processedVideoLink', new_link, env)
        if db_update_success == False:
            raise Exception('DB update error')

        db_update_success = update_route_field(route_id, 'sourceCaption', route_data.get('newSourceCaption'), env)
        if db_update_success == False:
            raise Exception('DB update error')
        db_update_success = update_route_field(route_id, 'languageCaptions', route_data.get('newLanguageCaptions'), env)
        if db_update_success == False:
            raise Exception('DB update error')
        db_update_success = update_route_field(route_id, 'processStatus', 'ARROW_ATTACHMENT_SUCCESS', env)
        if db_update_success == False:
            raise Exception('DB update error')
    except Exception as e:
        logging.info('Error while processing arrow attachment')
        print(e)
        try:
            update_route_field(route_id, 'processStatus', 'ARROW_ATTACHMENT_ERROR', env)
            update_automation_time(route_id, env)
        except:
            logging.info('Error while updating DB')
    finally:
        try:
            os.remove(f'final/{file_name}')
        except Exception as e:
            print('Error removing file')
        try:
            os.remove(f'final/codec_{file_name}')
        except Exception as e:
            print('Error removing file')



# @app.route('/test/direction-change', methods = ['POST'])
# def processArrowStick():
#     route_id = None
#     file_name = None
#     try:
#         logging.info('Arrow attachment part')
#         data = request.get_json()
#         route_id = data['route_id']
#         route_data = get_route_data(route_id)
#         if route_data == None:
#             logging.info('Route not found')
#             res_dat = {
#                 'error': True,
#                 'message': 'Route not found'
#             }
#             return jsonify(res_dat), 404

#         update_route_field(route_id, 'processStatus', 'ARROW_ATTACHMENT_START')
#         video_url = route_data.get('videoURL')
#         if video_url == None:
#             update_route_field(route_id, 'processStatus', 'ARROW_ATTACHMENT_ERROR')
#             res_dat = {
#                 'error': True,
#                 'message': 'Route video not found'
#             }
#             return jsonify(res_dat), 404
#         file_name = video_url.split('/')[-1]
#         logging.info('download of video started')
#         download_file_from_s3(bucket_name, f'{file_name}', f'blurred/{file_name}')
#         logging.info('download done')
#         final_directions = route_data.get('detectedDirections')
#         if final_directions == None:
#             logging.info('no directions found')
#             update_route_field(route_id, 'processStatus', 'ARROW_ATTACHMENT_ERROR')
#             res_dat = {
#                 'error': True,
#                 'message': 'Direction data not found'
#             }
#             return jsonify(res_dat), 404    
#         logging.info('Arrow attachment start')
#         arrow_attachment_main(file_name, final_directions)

#         # Change the video codec for making the video small in size
#         # ffmpeg -i input.mp4 -c:v libx264 -c:a copy output_h264.mp4
#         change_codec_command = ["ffmpeg", "-i", f'final/{file_name}', '-c:v', 'libx264', '-c:a', 'copy', f'final/codec_{file_name}']
#         result_dim = subprocess.run(change_codec_command, check=True, capture_output=True, text=True)
#         logging.info("Command Output codec:", result_dim.stdout)
#         logging.info("Command Error Output codec:", result_dim.stderr)

#         new_file_name = f'new_{file_name}'
#         new_link = f'https://s3.ap-south-1.amazonaws.com/media.demo.test/{new_file_name}'
#         upload_video_to_s3(f'final/codec_{file_name}', bucket_name, new_file_name)
#         update_route_field(route_id, 'processedVideoURL', new_link)
#         update_route_field(route_id, 'processStatus', 'ARROW_ATTACHMENT_SUCCESS')

#         res_dat = {
#             'error': False,
#             'message': 'Arrow attachment done'
#         }
#         return jsonify(res_dat), 200
#     except Exception as e:
#         logging.info('Error while processing arrow attachment')
#         try:
#             update_route_field(route_id, 'processStatus', 'ARROW_ATTACHMENT_ERROR')
#         except:
#             logging.info('Error while updating DB')
        
#         res_dat = {
#             'error': True,
#             'message': 'Error while processing'
#         }
#         return jsonify(res_dat), 200
#     finally:
#         try:
#             os.remove(f'final/{file_name}')
#         except Exception as e:
#             print('Error removing file')
#         try:
#             os.remove(f'final/codec_{file_name}')
#         except Exception as e:
#             print('Error removing file')
    

@app.route('/test/text-blur', methods=['POST'])
def testTextBlur():
    file_name = None
    route_id = None
    env = 'dev'
    try:
        data = request.get_json()
        if data['env'] != None:
            env = data['env']
        route_id = data['route_id']
        route_data = get_route_data(route_id, env)
        if route_data == None:
            data = {
                "message": "Route not found"
            }
            return jsonify(data), 404 
        update_route_field(route_id, 'processStatus', 'TEXT_BLUR_START', env)
        update_automation_time(route_id, env)
        thread = threading.Thread(target=textBlurJob, args=(data, route_data))
        thread.daemon = True  # This ensures the thread will be killed when the main program exits
        thread.start()
        res_data = {
            "message": "Route submitted for text-blur process"
        }
        return jsonify(res_data), 200 
    except Exception as e:
        update_route_field(route_id, 'processStatus', 'TEXT_BLUR_ERROR', env)
        update_automation_time(route_id, env)
        print('Error in text blur')
        print(e)
        return "Error while processing json file", 500



def textBlurJob(data, route_data):
    route_id = None
    env = 'dev'
    try:
        if data['env'] != None:
            env = data['env']
        db_update_success = False
        route_id = data['route_id']
        # route_data = get_route_data(route_id)
        json_file_path = route_data['textBlurJsonFileName']
        if json_file_path == None:
            raise Exception('Text blur file not found')
        
        video_url = route_data.get('videoURL')
        if video_url == None:
            raise Exception('Route Video not found')
            print('Route Video not found')
        file_name = video_url.split('/')[-1]
        print('Started downloading the Video File to be processed')
        db_update_success = download_file_from_s3(bucket_name, f'{env}/routes/{file_name}', f'inputs/{file_name}')
        update_automation_time(route_id, env)
        if db_update_success == False:
           raise Exception('Download failed')
        
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
            db_update_success = upload_video_to_s3(f'final/codec_{file_name}', bucket_name, file_name, env)
            if db_update_success == False:
               raise Exception('DB update failed')
            # Remove file from local
            os.remove(f'final/{file_name}')
            os.remove(f'final/codec_{file_name}')
            db_update_success = update_route_field(route_id, 'processStatus', 'TEXT_BLUR_SUCCESS', env)
            update_automation_time(route_id, env)
            if db_update_success == False:
                raise Exception('DB update failed')
            return
        update_automation_time(route_id, env)
    except Exception as e:
        update_route_field(route_id, 'processStatus', 'TEXT_BLUR_ERROR', env)
        print('Error in text blur')
        print(e)
        return "Error while processing json file", 500


@app.route('/check-health')
def cpuCheck():
    return "[Updated again 12] Server says hii", 200
    # avg_cpu = get_average_cpu_utilization(interval=1, times=2)
    # logging.info(f'Average CPU => {avg_cpu}')
    # if avg_cpu > 80:
    #     return "", 500
    # else:    
    #     return "", 200

@app.route('/face-blur', methods = ['POST'])
def faceBlurAPI():
    route_id = None
    data = request.get_json()
    env = 'dev'
    try:
        if data['env'] != None:
            env = data['env']
        route_id = data['route_id']
        route_data = get_route_data(route_id, env)
        if route_data == None:
            data = {
                "message": "Route not found"
            }
            return jsonify(data), 404
        update_route_field(route_id, 'processStatus', 'FACE_BLUR_START', env)
        update_automation_time(route_id, env)
        thread = threading.Thread(target=faceBlurJob, args=(data, route_data))
        thread.daemon = True  # This ensures the thread will be killed when the main program exits
        thread.start()
        res_data = {
            "message": "Route submitted for text-blur process"
        }
        return jsonify(res_data), 200 
    except Exception as e:
        print('Error in face blur')
        print(e)
        update_route_field(route_id, 'processStatus', 'FACE_BLUR_ERROR', env)
        update_automation_time(route_id, env)
        return "Error while processing json file", 500



def faceBlurJob(data, route_data):
    route_id = None
    file_name = None
    env = 'dev'
    try:
        route_id = data['route_id']
        blur = data.get('blur')
        if data['env'] != None:
            env = data['env']
        update_field_success = False

        # Need to run blur script, direction detection script and submit to route DB
        # 1) Download the video from s3 and save in local
        logging.info('Blurring start')
        update_field_success = update_route_field(route_id, 'processStatus', 'FACE_BLUR_START', env)
        update_automation_time(route_id, env)
        if update_field_success == False:
            raise Exception('Update DB failed')
        video_url = route_data['videoURL']
        file_name = video_url.split('/')[-1]
        download_success = download_file_from_s3(bucket_name, f'{env}/routes/{file_name}', f'inputs/{file_name}')
        if download_success == False:
            raise Exception('download failed')

        # 2) Blur the video
        blur_success = blurVideo(file_name)
        update_automation_time(route_id, env)
        if blur_success != True:
            raise 'Blur error'
        logging.info('blur complete')

        # 3) Upload blurred video to S3
        update_field_success = upload_video_to_s3(f'blurred/{file_name}', bucket_name, None, env)
        if update_field_success == False:
            raise Exception('Update DB failed')

        update_route_field(route_id, 'processStatus', 'FACE_BLUR_SUCCESS', env)
        update_automation_time(route_id, env)
    except Exception as e:
        update_route_field(route_id, 'processStatus', 'FACE_BLUR_ERROR', env)
        update_automation_time(route_id, env)
        print(e)
    finally:
        try:
            os.remove(f'blurred/{file_name}')
        except Exception as e:
            print('Error while removing blurred file from local')


@app.route('/direction-detection', methods = ['POST'])
def directionDetectionAPI():
    route_id = None
    env = 'dev'
    data = request.get_json()
    try:
        if data['env'] != None:
            env = data['env']
        route_id = data['route_id']
        route_data = get_route_data(route_id, env)
        if route_data == None:
            raise Exception('Route not found')
        update_route_field(route_id, 'processStatus', 'DIRECTION_DETECTION_START', env)
        update_automation_time(route_id, env)
        thread = threading.Thread(target=directionDetectionJob, args=(data, route_data))
        thread.daemon = True  # This ensures the thread will be killed when the main program exits
        thread.start()
        res_data = {
            "message": "Route submitted for direction-detection process"
        }
        return jsonify(res_data), 200 
    except Exception as e:
        print('Error in face blur')
        print(e)
        update_route_field(route_id, 'processStatus', 'DIRECTION_DETECTION_ERROR', env)
        return "Error while processing json file", 500

def directionDetectionJob(data, route_data):
    route_id = None
    file_name = None
    env = 'dev'
    try:
        if data['env'] != None:
            env = data['env']
        route_id = route_data['id']
        video_url = route_data['videoURL']
        file_name = video_url.split('/')[-1]
        download_success = download_file_from_s3(bucket_name, f'{env}/routes/{file_name}', f'blurred/{file_name}')
        if download_success == False:
            raise Exception('download failed')
        logging.info('Starting the direction detection')
        final_directions = directionDetection(file_name)
        if final_directions == False:
            raise Exception('Error while generating directions')
        # Store these directions in dynamo table
        store_detected_directions(final_directions, route_id, env)
        update_db_success = update_route_field(route_id, 'processStatus', 'DIRECTION_DETECTION_SUCCESS', env)
        update_automation_time(route_id, env)
        if update_db_success == False:
            raise Exception('DB update failed')
        update_db_success = update_route_field(route_id, 'actionStatus', 'Updated', env)
        update_automation_time(route_id, env)
        if update_db_success == False:
            raise Exception('DB update failed')
        logging.info('Done :+1')
    except Exception as e:
        update_route_field(route_id, 'processStatus', 'DIRECTION_DETECTION_ERROR', env)
        update_automation_time(route_id, env)
        print(e)
    finally:
        try:
            os.remove(f'blurred/{file_name}')
        except Exception as e:
            print('Error while removing blurred file from local')


# The expected body of the request
# {'route_id': '', 'blur': '', 'direction_detect': True/False, 'arrow_attachment': True/False, 'file_name': ''}
# TODO: Add Validation here
# @app.route('/process-routes', methods = ['POST'])
def processRouteAPI():
    route_id = None
    env = 'dev'
    try:
        data = request.get_json()
        if data['env'] != None:
            env = data['env']
        route_id = data['route_id']
        blur = data.get('blur')
        # file_name = data['file_name']
        direction_detect = data.get('direction_detect')
        arrow_attachment = data.get('arrow_attachment')

        if blur == True:
            # Need to run blur script, direction detection script and submit to route DB
            # 1) Download the video from s3 and save in local
            logging.info('Blurring start')
            route_data = get_route_data(route_id, env)
            if route_data == None:
                logging.info('Route not found')
                res_dat = {
                    'error': True,
                    'message': 'Route not found'
                }
                return jsonify(res_dat), 404
            video_url = route_data['videoURL']
            file_name = video_url.split('/')[-1]
            download_file_from_s3(bucket_name, f'{file_name}', f'inputs/{file_name}')

            # 2) Blur the video
            blurSuccess = blurVideo(file_name)
            logging.info('blur complete')

            # 3) Upload blurred video to S3
            upload_video_to_s3(f'blurred/{file_name}', bucket_name, None, env)

            # 4) Remove file from local
            os.remove(f'blurred/{file_name}')
        elif direction_detect == True:
            # Get directions from route DB, use arrow attachment script
            route_data = get_route_data(route_id, env)
            if route_data == None:
                logging.info('Route not found')
                res_dat = {
                    'error': True,
                    'message': 'Route not found'
                }
                return jsonify(res_dat), 404
            video_url = route_data['videoURL']
            file_name = video_url.split('/')[-1]
            download_file_from_s3(bucket_name, f'{file_name}', f'blurred/{file_name}')
            logging.info('Starting the direction detection')
            final_directions = directionDetection(file_name)
            # Store these directions in dynamo table
            store_detected_directions(final_directions, route_id, env)
            logging.info('Done :+1')
        elif arrow_attachment == True:
            logging.info('Arrow attachment part')
            route_data = get_route_data(route_id, env)
            if route_data == None:
                logging.info('Route not found')
                res_dat = {
                    'error': True,
                    'message': 'Route not found'
                }
                return jsonify(res_dat), 404
            video_url = route_data['videoURL']
            file_name = video_url.split('/')[-1]
            logging.info('download of video started')
            download_file_from_s3(bucket_name, f'{file_name}', f'blurred/{file_name}')
            logging.info('download done')
            final_directions = route_data.get('detectedDirections')
            logging.info('got directions')
            if final_directions == None:
                logging.info('no directions found')
                res_dat = {
                    'error': True,
                    'message': 'Direction data not found'
                }
                return jsonify(res_dat), 404    
            logging.info('Arrow attachment start')
            arrow_attachment_main(file_name, final_directions)

            # Change the video codec for making the video small in size
            # ffmpeg -i input.mp4 -c:v libx264 -c:a copy output_h264.mp4
            change_codec_command = ["ffmpeg", "-i", f'final/{file_name}', '-c:v', 'libx264', '-c:a', 'copy', f'final/codec_{file_name}']
            result_dim = subprocess.run(change_codec_command, check=True, capture_output=True, text=True)
            logging.info("Command Output codec:", result_dim.stdout)
            logging.info("Command Error Output codec:", result_dim.stderr)

            upload_video_to_s3(f'final/codec_{file_name}', bucket_name, file_name, env)
            # upload_video_to_s3(f'final/codec_{file_name}', bucket_name)
        else:
            res_dat = {
                'error': True,
                'message': 'Route not found'
            }
            return jsonify(res_dat), 404
        res_success = {
                'error': False,
                'message': 'Process completed successfully'
            }
        return jsonify(res_success), 200
    except Exception as e:
        logging.info('Error while processing route')
        logging.info(e)
        logging.info(f'Error while processing route => {route_id}')
        try:
            update_route_field(route_id, 'videoProcessError', True, env)
        except Exception as e: 
            logging.info('Error while updating DB about the video process error')
        res_dat = {
            'error': True,
            'message': 'Error while processing'
        }
        return jsonify(res_dat), 500


def processRoute():
    try:
        route_id = data['route_id']
        blur = data['blur']
        file_name = data['file_name']
        direction_detect = data['direction_detect']
        arrow_attachment = data['arrow_attachment']

        if blur == True:
            # Need to run blur script, direction detection script and submit to route DB
            # 1) Download the video from s3 and save in local
            s3_err = download_file_from_s3(bucket_name, f'{file_name}', f'inputs/{file_name}')
            if s3_success == False:
                return False, 'Error while downloading route file'

            # 2) Blur the video
            blur_success = blurVideo(file_name)
            if blur_success == False:
                return False, 'Error while processing blur on video'
            logging.info('blur complete')

            # 4) Direction detection
            logging.info('Direction automation start')
            final_directions = directionDetection(file_name)

            # 5) TODO: Save this direction route in Route DB
        elif blur == False and arrow_attachment == True:
            # Get directions from route DB, use arrow attachment script
            route_data = get_route_data(route_id, env)
            if route_data == None:
                logging.info('Route not found')
                return False, 'Route not found'
    except Exception as e:
        return None, 'Error while processing route'
logging.info(f'__name__ => {__name__}')

if __name__ == '__main__':
    try:
        logging.info('Server starting ...')
        app.run(host="0.0.0.0", port=5000, debug=True)
        logging.info('Server started ...')
    except Exception as e:
        logging.info('Error while starting server')
        logging.info(e)
else:
    logging.info('not going in main')
