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
from constants import CalculationMetrics, DirectionDetectionConfig
from sliding_window import sliding_window_main, getDirectionMessage
from decimal import Decimal
from typing import List, TypedDict
from animation_gif_helpers import checkIfTurn
logging.basicConfig(level=logging.INFO)

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
    'STRAIGHT': 'Continue forward',
    'LEFT': 'Turn left',
    'SLIGHT_LEFT': 'Turn slight left',
    'RIGHT': 'Turn right',
    'SLIGHT_RIGHT': 'Turn slight right',
    'END': 'Destination arrived'
}
poolSize = cpuCount
process_pool = ProcessPoolExecutor(poolSize)

FRAME_STRIDE = DirectionDetectionConfig.FRAME_STRIDE
FLOW_MAX_WIDTH = DirectionDetectionConfig.FLOW_MAX_WIDTH


def prepare_gray(frame):
    """Convert to grayscale and downscale for faster Farneback."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    height, width = gray.shape[:2]
    if width > FLOW_MAX_WIDTH:
        scale = FLOW_MAX_WIDTH / float(width)
        gray = cv2.resize(
            gray,
            (FLOW_MAX_WIDTH, max(1, int(round(height * scale)))),
            interpolation=cv2.INTER_AREA,
        )
    return gray


def scaled_flow_thresholds(native_width, flow_width):
    """Scale classification thresholds for downscale + multi-frame stride."""
    resize_scale = flow_width / float(native_width) if native_width else 1.0
    magnitude_scale = resize_scale * FRAME_STRIDE
    return (
        DirectionDetectionConfig.BASE_SENSITIVITY * magnitude_scale,
        DirectionDetectionConfig.BASE_SLIGHT_THRESHOLD * magnitude_scale,
    )

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
        if not _ret or prev is None:
            return {"data": []}

        native_width = prev.shape[1]
        prevgray = prepare_gray(prev)
        flow_width = prevgray.shape[1]
        sensitivity, slight_threshold = scaled_flow_thresholds(native_width, flow_width)
        iters = frame_start

        direction_data = {"data": []}  # Dictionary to store the list of timestamp and direction data
        while iters < frame_end:
            # Advance FRAME_STRIDE frames; grab() skips decode for intermediate frames
            for _ in range(FRAME_STRIDE - 1):
                if iters + 1 > frame_end:
                    return direction_data
                if not cam.grab():
                    return direction_data
                iters += 1

            iters += 1
            _ret, img = cam.read()
            if not _ret:
                break

            timestamp = iters / fps
            gray = prepare_gray(img)
            flow = cv2.calcOpticalFlowFarneback(
                prevgray,
                gray,
                None,
                DirectionDetectionConfig.FARNEBACK_PYR_SCALE,
                DirectionDetectionConfig.FARNEBACK_LEVELS,
                DirectionDetectionConfig.FARNEBACK_WINSIZE,
                DirectionDetectionConfig.FARNEBACK_ITERATIONS,
                DirectionDetectionConfig.FARNEBACK_POLY_N,
                DirectionDetectionConfig.FARNEBACK_POLY_SIGMA,
                0,
            )
            prevgray = gray

            direction = classify_direction(
                flow,
                sensitivity=sensitivity,
                slight_threshold=slight_threshold,
            )
            direction_data["data"].append({
                "timestamp": round(timestamp, 2),
                "directionIcon": direction,
            })

        return direction_data
    except Exception as e:
        logging.info('Error in process_vid_segment')
        logging.info(e)


class DirectionData(TypedDict):
    startTime: int
    endTime: int
    directionIcon: str
    message: str
    description: str
    distance: Decimal

def finalDirectionGrouping(data: List[DirectionData]) -> List[DirectionData]:
    try:
        latestNewDirection = None
        groupedData : List[DirectionData] = []
        for index, directionInstance in enumerate(data):
            if index == 0:
                latestNewDirection = directionInstance
            else:
                if latestNewDirection.get('directionIcon') != directionInstance.get('directionIcon'):
                    prevInstance = data[index-1]
                    groupedData.append({
                        'startTime': latestNewDirection.get('startTime'),
                        'endTime': prevInstance.get('endTime'),
                        'directionIcon': latestNewDirection.get('directionIcon'),
                        'description': latestNewDirection.get('description')
                    })
                    latestNewDirection = directionInstance
        if latestNewDirection != None:
            groupedData.append(latestNewDirection)
        
        return groupedData
    except Exception as e:
        logging.info('Error in finalDirectionGrouping')
        logging.info(e)
        return False

def enhanceDirectionsWithDistance(data: List[DirectionData]) -> List[DirectionData]:
    try:
        newDirections : List[DirectionData] = []
        for index, directionInstance in enumerate(data):
            startTime = directionInstance['startTime']
            endTime = directionInstance['endTime']
            duration = endTime - startTime
            direction = directionInstance['directionIcon']
            if direction == directionTypes.get('STRAIGHT'):
                if duration >= CalculationMetrics.TRIGGER_DISTANCE_CAPTION_ON_DURATION:
                    currentStraightEnd = startTime + CalculationMetrics.DISTANCE_CAPTION_DISPLAY_DUREATION
                    nextIsTurn = False
                    if index + 1 < len(data):
                        nextIsTurn = checkIfTurn(data[index + 1]['directionIcon'])

                    turnNoticeStartTime = endTime - CalculationMetrics.DURATION_BEFORE_TURN_NOTICE
                    distance = (duration) * CalculationMetrics.AVG_DISTANCE_PER_SEC_FT
                    
                    # Message like "Continue straight for x feet/metre"
                    newDirections.append({
                        'startTime': startTime,
                        'endTime': currentStraightEnd,
                        'directionIcon': direction,
                        'description': getDirectionMessage(direction, True),
                        'distance': Decimal(str(round(distance / 10) * 10)),
                    })
                    # normal striaght direction message
                    newDirections.append({
                        'startTime': currentStraightEnd,
                        'endTime': turnNoticeStartTime if nextIsTurn else endTime,
                        'directionIcon': direction,
                        'description': getDirectionMessage(direction),
                    })

                    if nextIsTurn:
                        turnInDistance = CalculationMetrics.DURATION_BEFORE_TURN_NOTICE * CalculationMetrics.AVG_DISTANCE_PER_SEC_FT
                        # Message like "In x ft/mt turn left"
                        newDirections.append({
                            'startTime': turnNoticeStartTime,
                            'endTime': endTime,
                            'directionIcon': direction,
                            'description': getDirectionMessage(data[index + 1]['directionIcon'], True),
                            'distance': Decimal(turnInDistance),
                        })
                else:
                    newDirections.append(directionInstance)
            else:
                newDirections.append(directionInstance)
        return newDirections
    except Exception as e:
        logging.info('Error in enhanceDirectionsWithDistance')
        logging.info(e)
        return False

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

        cam = video.create_capture(fn)
        total_frames = round(cam.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = cam.get(cv2.CAP_PROP_FPS)
        
        logging.info(f'Video FPS => {fps}')
    
        results = process_vid_segment((1, total_frames, fps, file_path))

        # # -------------------- Parallel process part -------------------- 
        # routeFramesParallelProcess = int(total_frames*0.1)
        # chunks = math.floor(total_frames/routeFramesParallelProcess) + 1 # Total frame segments which will be processed
        # frames_split_meta = getFrameSplits(chunks, total_frames, routeFramesParallelProcess)
        # input_tuple = []
        # i=3
        # for frame_meta in frames_split_meta:
        #     start = frame_meta['startTime']
        #     end = frame_meta['endTime']
        #     input_tuple.append((start, end, fps, file_path))
        #     i +=1

        # # logging.info(frames_split_meta)
        # # exit()

        # # _ret, prev = cam.read()
        # # # prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
        # # show_hsv = False
        # # show_glitch = False
        # # cur_glitch = prev.copy()
        # # frame_count = 0

        # logging.info(f'Video fps => {fps}')
        # # process_pool.map(process_vid_segment, input_tuple)
        # results = list(process_pool.map(process_vid_segment, input_tuple))
        # ------------------ Parallel process end --------------------

        # with open(f'multithreaded_ou/{file_name}.json', 'w') as json_file:
        #     json.dump(results, json_file, indent=4)


        finalOutput = sliding_window_main(
            results.get("data", []),
            file_name,
            fps,
            total_frames,
            frame_stride=FRAME_STRIDE,
        )
        if finalOutput == None:
            return False
        else:
            # Change the directionIcon value
            for _, el in enumerate(finalOutput):
                resDirection = el['directionIcon'].upper()
                el['directionIcon'] = resDirection
                el['description'] = getDirectionMessage(resDirection)
            
            finalOutput = finalDirectionGrouping(finalOutput)
            finalOutput = enhanceDirectionsWithDistance(finalOutput)
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
