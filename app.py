import os
import boto3
import subprocess
import threading
from datetime import datetime
from flask import Flask, request, jsonify
from blur_automate import blurVideo
from direction_detection import directionDetection
from botocore.exceptions import ClientError
from helpers import download_video_from_s3, get_route_data, upload_video_to_s3, store_detected_directions, update_route_field, get_average_cpu_utilization
from arrow_attachment import arrow_attachment_main
import threading
from text_blur import text_blur_main
import logging
logging.basicConfig(level=logging.INFO)


bucket_name = 'media.demo.test'
app = Flask(__name__)
logging.info('Inside the server')

@app.route('/test/v1')
def testServerV1():
    data = {
        "message": "Hello from server"
    }
    return jsonify(data), 200

# @app.route('/test')
def testServer():
    try:
        start_time = datetime.now()
        # 1) Download the video from s3 and save in local
        file_name = 'dubai_small_dim.mp4'
        # download_video_from_s3('media.demo.test', f'{file_name}', f'inputs/{file_name}')

        # 2) Blur the video
        blurVideo(file_name)
        # logging.info('blur complete')

        # 3) Now remove the input folder
        # os.remove('inputs/potrait_sample_down.mp4')

        # 4) Direction detection
        logging.info('Direction automation start')
        directionDetection(file_name)
        end_time = datetime.now()
        logging.info('API start => ', start_time)
        logging.info('API end => ', end_time)
        data = {
            "message": "Hello from server"
        }
        return jsonify(data), 200
    except Exception as e:
        logging.info(e)
        data = {
            "message": "Error from server"
        }
        return jsonify(data), 500

mas = {"data": [{"start": 407, "end": 408, "direction": "right", "startFormat": "6 min 47 sec", "endFormat": "6 min 48 sec"}, {"direction": "straight", "start": 408, "end": 410, "startFormat": "6 min 48 sec", "endFormat": "6 min 50 sec"}, {"start": 410, "end": 411, "direction": "right", "startFormat": "6 min 50 sec", "endFormat": "6 min 51 sec"}, {"direction": "straight", "start": 411, "end": 412, "startFormat": "6 min 51 sec", "endFormat": "6 min 52 sec"}, {"start": 412, "end": 413, "direction": "right", "startFormat": "6 min 52 sec", "endFormat": "6 min 53 sec"}, {"direction": "straight", "start": 413, "end": 430, "startFormat": "6 min 53 sec", "endFormat": "7 min 10 sec"}, {"start": 430, "end": 431, "direction": "left", "startFormat": "7 min 10 sec", "endFormat": "7 min 11 sec"}, {"direction": "straight", "start": 431, "end": 460, "startFormat": "7 min 11 sec", "endFormat": "7 min 40 sec"}, {"start": 460, "end": 461, "direction": "left", "startFormat": "7 min 40 sec", "endFormat": "7 min 41 sec"}, {"direction": "straight", "start": 461, "end": 463, "startFormat": "7 min 41 sec", "endFormat": "7 min 43 sec"}, {"start": 463, "end": 464, "direction": "left", "startFormat": "7 min 43 sec", "endFormat": "7 min 44 sec"}, {"direction": "straight", "start": 464, "end": 502, "startFormat": "7 min 44 sec", "endFormat": "8 min 22 sec"}, {"start": 502, "end": 503, "direction": "slight right", "startFormat": "8 min 22 sec", "endFormat": "8 min 23 sec"}, {"direction": "straight", "start": 503, "end": 505, "startFormat": "8 min 23 sec", "endFormat": "8 min 25 sec"}, {"start": 505, "end": 506, "direction": "right", "startFormat": "8 min 25 sec", "endFormat": "8 min 26 sec"}, {"direction": "straight", "start": 506, "end": 549, "startFormat": "8 min 26 sec", "endFormat": "9 min 9 sec"}, {"start": 549, "end": 550, "direction": "right", "startFormat": "9 min 9 sec", "endFormat": "9 min 10 sec"}, {"direction": "straight", "start": 550, "end": 552, "startFormat": "9 min 10 sec", "endFormat": "9 min 12 sec"}, {"start": 552, "end": 553, "direction": "slight right", "startFormat": "9 min 12 sec", "endFormat": "9 min 13 sec"}, {"direction": "straight", "start": 553, "end": 576, "startFormat": "9 min 13 sec", "endFormat": "9 min 36 sec"}, {"start": 576, "end": 577, "direction": "slight left", "startFormat": "9 min 36 sec", "endFormat": "9 min 37 sec"}]}

@app.route('/test/automation-start', methods=['POST'])
def testPost():
    file_name = None
    try:
        data = request.get_json()
        route_id = data['route_id']
        route_data = get_route_data(route_id)
        if route_data == None:
            data = {
                "message": "Route not found"
            }
            return jsonify(data), 404 
        
        video_url = route_data.get('videoURL')
        if video_url == None:
            data = {
                "message": "Route Video not found"
            }
            return jsonify(data), 404 
        file_name = video_url.split('/')[-1]
        download_video_from_s3('media.demo.test', f'{file_name}', f'inputs/{file_name}')
        
        # 2) Blur the video
        update_route_field(route_id, 'processStatus', 'BLUR_START')
        blurVideo(file_name)
        logging.info('blur complete')
        upload_video_to_s3(f'blurred/{file_name}', bucket_name) # This will become the base version
        update_route_field(route_id, 'processStatus', 'BLUR_COMPLETE')
        # 3) Direction detection
        update_route_field(route_id, 'processStatus', 'DIRECTION_DETECTION_START')
        final_directions = directionDetection(file_name)
        if final_directions == None:
            update_route_field(route_id, 'processStatus', 'DIRECTION_DETECTION_ERROR')
        else:
            store_detected_directions(final_directions, route_id)
            logging.info('Direction detection complete')
            update_route_field(route_id, 'processStatus', 'DIRECTION_DETECTION_SUCCESS')
            data = {
                "message": "Done processing..."
            }
            return jsonify(data), 200
    except Exception as e:
        logging.info('Error while processintg video')
        data = {
            "message": 'Error while processintg video'
        }
        return jsonify(data), 500
    finally:
        try:
            os.remove(f'blurred/{file_name}')
        except Exception as e:
            print('Error removing file')


@app.route('/test/direction-change', methods = ['POST'])
def processArrowStick():
    route_id = None
    file_name = None
    try:
        logging.info('Arrow attachment part')
        data = request.get_json()
        route_id = data['route_id']
        route_data = get_route_data(route_id)
        if route_data == None:
            logging.info('Route not found')
            res_dat = {
                'error': True,
                'message': 'Route not found'
            }
            return jsonify(res_dat), 404

        update_route_field(route_id, 'processStatus', 'ARROW_ATTACHMENT_START')
        video_url = route_data.get('videoURL')
        if video_url == None:
            update_route_field(route_id, 'processStatus', 'ARROW_ATTACHMENT_ERROR')
            res_dat = {
                'error': True,
                'message': 'Route video not found'
            }
            return jsonify(res_dat), 404
        file_name = video_url.split('/')[-1]
        logging.info('download of video started')
        download_video_from_s3('media.demo.test', f'{file_name}', f'blurred/{file_name}')
        logging.info('download done')
        final_directions = route_data.get('detectedDirections')
        if final_directions == None:
            logging.info('no directions found')
            update_route_field(route_id, 'processStatus', 'ARROW_ATTACHMENT_ERROR')
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

        new_file_name = f'new_{file_name}'
        new_link = f'https://s3.ap-south-1.amazonaws.com/media.demo.test/{new_file_name}'
        upload_video_to_s3(f'final/codec_{file_name}', bucket_name, new_file_name)
        update_route_field(route_id, 'processedVideoURL', new_link)
        update_route_field(route_id, 'processStatus', 'ARROW_ATTACHMENT_SUCCESS')

        res_dat = {
            'error': False,
            'message': 'Arrow attachment done'
        }
        return jsonify(res_dat), 200
    except Exception as e:
        logging.info('Error while processing arrow attachment')
        try:
            update_route_field(route_id, 'processStatus', 'ARROW_ATTACHMENT_ERROR')
        except:
            logging.info('Error while updating DB')
        
        res_dat = {
            'error': True,
            'message': 'Error while processing'
        }
        return jsonify(res_dat), 200
    finally:
        try:
            os.remove(f'final/{file_name}')
        except Exception as e:
            print('Error removing file')
        try:
            os.remove(f'final/codec_{file_name}')
        except Exception as e:
            print('Error removing file')
    

@app.route('/test/text-blur', methods=['POST'])
def testTextBlur():
    file_name = None
    try:
        data = request.get_json()
        route_id = data['route_id']
        route_data = get_route_data(route_id)
        if route_data == None:
            data = {
                "message": "Route not found"
            }
            return jsonify(data), 404 
        thread = threading.Thread(target=textBlurJob, args=(data, route_data))
        thread.daemon = True  # This ensures the thread will be killed when the main program exits
        thread.start()
        res_data = {
            "message": "Route submitted for text-blur process"
        }
        return jsonify(res_data), 200 
    except Exception as e:
        update_route_field(route_id, 'processStatus', 'TEXT_BLUR_ERROR')
        print('Error in text blur')
        print(e)
        return "Error while processing json file", 500



def textBlurJob(data, route_data):
    try:
        route_id = data['route_id']
        # route_data = get_route_data(route_id)
        
        json_file_path = route_data['textBlurJsonFileName']
        if json_file_path == None:
            update_route_field(route_id, 'processStatus', 'TEXT_BLUR_ERROR')
            print('Text blur file not found')
            return
        
        video_url = route_data.get('videoURL')
        if video_url == None:
            update_route_field(route_id, 'processStatus', 'TEXT_BLUR_ERROR')
            print('Route Video not found')
            return
        file_name = video_url.split('/')[-1]
        print('Started downloading the Video File to be processed')
        download_video_from_s3('media.demo.test', f'{file_name}', f'inputs/{file_name}')

        print('Started downloading the JSON File to be processed')
        # Download the Google's Video Intelligence text-blur output stored in the AWS-S3
        json_file_name = json_file_path.split('/')[-1]
        download_video_from_s3('media.demo.test', json_file_path, f'text_json/{json_file_name}')

        # Start the text blur script
        blur_success = text_blur_main(file_name, json_file_name)

        if blur_success == False:
            print('Error while blurrig text')
            update_route_field(route_id, 'processStatus', 'TEXT_BLUR_ERROR')
            return
        else:
            # Upload the text-blurred video to S3
            upload_video_to_s3(f'final/{file_name}', 'media.demo.test')
            # Remove file from local
            os.remove(f'final/{file_name}')
            update_route_field(route_id, 'processStatus', 'TEXT_BLUR_SUCCESS')
            return
    except Exception as e:
        update_route_field(route_id, 'processStatus', 'TEXT_BLUR_ERROR')
        print('Error in text blur')
        print(e)
        return "Error while processing json file", 500


@app.route('/check-health')
def cpuCheck():
    return "[Updated again] Server says hii", 200
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
    try:
        route_id = data['route_id']
        route_data = get_route_data(route_id)
        if route_data == None:
            data = {
                "message": "Route not found"
            }
            return jsonify(data), 404
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
        update_route_field(route_id, 'processStatus', 'FACE_BLUR_ERROR')
        return "Error while processing json file", 500



def faceBlurJob(data, route_data):
    route_id = None
    file_name = None
    try:

        route_id = data['route_id']
        blur = data.get('blur')
        # file_name = data['file_name']
        direction_detect = data.get('direction_detect')
        arrow_attachment = data.get('arrow_attachment')

        # Need to run blur script, direction detection script and submit to route DB
        # 1) Download the video from s3 and save in local
        logging.info('Blurring start')
        update_route_field(route_id, 'processStatus', 'FACE_BLUR_START')
        video_url = route_data['videoURL']
        file_name = video_url.split('/')[-1]
        download_video_from_s3('media.demo.test', f'{file_name}', f'inputs/{file_name}')

        # 2) Blur the video
        blurVideo(file_name)
        logging.info('blur complete')

        # 3) Upload blurred video to S3
        upload_video_to_s3(f'blurred/{file_name}', bucket_name)

        update_route_field(route_id, 'processStatus', 'FACE_BLUR_SUCCESS')
    except Exception as e:
        update_route_field(route_id, 'processStatus', 'FACE_BLUR_ERROR')
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
    try:
        data = request.get_json()

        route_id = data['route_id']
        blur = data.get('blur')
        # file_name = data['file_name']
        direction_detect = data.get('direction_detect')
        arrow_attachment = data.get('arrow_attachment')

        if blur == True:
            # Need to run blur script, direction detection script and submit to route DB
            # 1) Download the video from s3 and save in local
            logging.info('Blurring start')
            route_data = get_route_data(route_id)
            if route_data == None:
                logging.info('Route not found')
                res_dat = {
                    'error': True,
                    'message': 'Route not found'
                }
                return jsonify(res_dat), 404
            video_url = route_data['videoURL']
            file_name = video_url.split('/')[-1]
            download_video_from_s3('media.demo.test', f'{file_name}', f'inputs/{file_name}')

            # 2) Blur the video
            blurVideo(file_name)
            logging.info('blur complete')

            # 3) Upload blurred video to S3
            upload_video_to_s3(f'blurred/{file_name}', bucket_name)

            # 4) Remove file from local
            os.remove(f'blurred/{file_name}')
        elif direction_detect == True:
            # Get directions from route DB, use arrow attachment script
            route_data = get_route_data(route_id)
            if route_data == None:
                logging.info('Route not found')
                res_dat = {
                    'error': True,
                    'message': 'Route not found'
                }
                return jsonify(res_dat), 404
            video_url = route_data['videoURL']
            file_name = video_url.split('/')[-1]
            download_video_from_s3('media.demo.test', f'{file_name}', f'blurred/{file_name}')
            logging.info('Starting the direction detection')
            final_directions = directionDetection(file_name)
            # Store these directions in dynamo table
            store_detected_directions(final_directions, route_id)
            logging.info('Done :+1')
        elif arrow_attachment == True:
            logging.info('Arrow attachment part')
            route_data = get_route_data(route_id)
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
            download_video_from_s3('media.demo.test', f'{file_name}', f'blurred/{file_name}')
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

            upload_video_to_s3(f'final/codec_{file_name}', bucket_name, file_name)
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
            update_route_field(route_id, 'videoProcessError', True)
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
            s3_err = download_video_from_s3('media.demo.test', f'{file_name}', f'inputs/{file_name}')
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
            route_data = get_route_data(route_id)
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

