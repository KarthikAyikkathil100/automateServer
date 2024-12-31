import cv2
from concurrent.futures import ProcessPoolExecutor
import math
import os
import time

import numpy as np
import sys
import video
import json  # Importing the json module
from datetime import datetime
import logging
logging.basicConfig(level=logging.INFO)
from sliding_window import sliding_window_main

from helpers import  update_route_field

cpuCount = os.cpu_count()
logging.info(f'CPUs => {cpuCount}')

frameParallelProcess = 800
directionTypes = {
    'STRAIGHT': 'STRAIGHT',
    'LEFT': 'LEFT',
    'S_LEFT': 'SLIGHT_LEFT',
    'RIGHT': 'RIGHT',
    'S_RIGHT': 'SLIGHT_RIGHT',
}

directionMessages = {
    'STRAIGHT': 'Go straight',
    'LEFT': 'Turn left',
    'SLIGHT_LEFT': 'Turn slight left',
    'RIGHT': 'Turn right',
    'SLIGHT_RIGHT': 'Turn slight right',
}
poolSize = cpuCount
process_pool = ProcessPoolExecutor(poolSize)

def getFrameSplits(nChunks, totalFrames, routeFramesParallelProcess):
    res = []
    init = 1

    for index, x in enumerate(range(nChunks)):
        tempInit = init
        if index != 0:
            tempInit += 1
        res.append({
            'startTime': tempInit,
            'endTime': tempInit + routeFramesParallelProcess -1
        })
        init = tempInit + routeFramesParallelProcess -1
    
    if init != totalFrames:
        res.append({
            'startTime': init+1,
            'endTime': totalFrames
        })
    return res
  

def classify_direction(flow, sensitivity=1.6, slight_threshold=0.8):
    fx, fy = flow[:,:,0], flow[:,:,1]
    avg_fx = np.mean(fx)
    avg_fy = np.mean(fy)

    # if avg_fx > 1.4:
    #     return "Left"
    # elif avg_fx < -1.4:
    #     return "Right"
    # else:
    #     return "Straight"

    if avg_fx > sensitivity:
        return directionTypes.get('LEFT')
    elif avg_fx > slight_threshold:
        return directionTypes.get('S_LEFT')
    elif avg_fx < -sensitivity:
        return directionTypes.get('RIGHT')
    elif avg_fx < -slight_threshold:
        return directionTypes.get('S_RIGHT')
    else:
        return directionTypes.get('STRAIGHT')



def process_vid_segment(meta):
    try:
        frame_start = meta[0]
        frame_end = meta[1]
        fps = meta[2]
        file_path = meta[3]
        cam = video.create_capture(file_path)
        cam.set(cv2.CAP_PROP_POS_FRAMES, frame_start)

        _ret, prev = cam.read()
        prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
        iters = frame_start

        direction_data = {"data": []}  # Dictionary to store the list of timestamp and direction data
        while iters < frame_end:

            iters += 1
            _ret, img = cam.read()
            if not _ret:
                break
            # frame_count += 1
            
            timestamp = iters / fps

            # # Skip every 3rd frame (Need to check the timing of completion and accuracy)
            # if frame_count % 3 == 0:
            #     continue

                
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            window_size = 15 # default was 15
            flow = cv2.calcOpticalFlowFarneback(prevgray, gray, None, 0.5, 3, window_size, 3, 5, 1.2, 0)
            prevgray = gray

            # Classify direction based on flow
            direction = classify_direction(flow)

            # Store the direction with the timestamp as the key
            direction_data["data"].append({"timestamp": round(timestamp, 2), "directionIcon": direction})
            # if iters%100 == 0:
            #     logging.info(f"Frame: {iters} Timestamp : {timestamp:.2f} Direction: {direction}")

        return direction_data
    except Exception as e:
        logging.info('Error in process_vid_segment')
        logging.info(e)



def directionDetection(file_name):
    # try:
    #     fn = sys.argv[1]
    # except IndexError:
    #     fn = 0
    # except Exception as e:
    #     logging.info(e)
    fn = f'blurred/{file_name}'
    file_path = fn
    try:
        start_time = datetime.now()

        cam = video.create_capture(fn)
        fps = cam.get(cv2.CAP_PROP_FPS)
        if fps == 0:
            fps = 30  # Default to 30 if FPS is not defined

        total_frames = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))
        routeFramesParallelProcess = int(total_frames*0.1)
        print(f'routeFramesParallelProcess => {routeFramesParallelProcess}')
        chunks = math.floor(total_frames/routeFramesParallelProcess) + 1 # Total frame segments which will be processed
        frames_split_meta = getFrameSplits(chunks, total_frames, routeFramesParallelProcess)
        input_tuple = []
        i=3
        for frame_meta in frames_split_meta:
            start = frame_meta['startTime']
            end = frame_meta['endTime']
            input_tuple.append((start, end, fps, file_path))
            i +=1
        # logging.info(frames_split_meta)
        # exit()

        # _ret, prev = cam.read()
        # # prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
        # show_hsv = False
        # show_glitch = False
        # cur_glitch = prev.copy()
        # frame_count = 0

        logging.info('Video fps => ', fps)
        # process_pool.map(process_vid_segment, input_tuple)
        results = list(process_pool.map(process_vid_segment, input_tuple))
        # with open(f'multithreaded_ou/{file_name}.json', 'w') as json_file:
        #     json.dump(results, json_file, indent=4)

        
        end_time = datetime.now()

        finalOutput = sliding_window_main(results, file_name, fps, total_frames)
        if finalOutput == None:
            return False
        else:
            # Change the directionIcon value
            for _, el in enumerate(finalOutput):
                resDirection = el['directionIcon'].upper()
                el['directionIcon'] = resDirection
                el['description'] = directionMessages.get(resDirection)

                print(el['directionIcon'])
                print(el['description'])
            return finalOutput
    except Exception as e:
        logging.info('Error in directionDetection fn')
        logging.info(e)
        return False


# def postprocessDirections(directions):
#     try:

#     except Exception as e:
#         print(e)
#         raise e

# if __name__ == '__main__':
#     directionDetection('mia_test.mp4')
