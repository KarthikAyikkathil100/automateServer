from copy import copy
from typing import List, Dict, Any
import random


threshold = 90
directionTypes = {
    'STRAIGHT': 'STRAIGHT',
    'LEFT': 'LEFT',
    'S_LEFT': 'SLIGHT_LEFT',
    'RIGHT': 'RIGHT',
    'S_RIGHT': 'SLIGHT_RIGHT',
}

directionMessages = {
    'STRAIGHT': ['Continue forward', 'Keep going straight', 'Proceed forward', 'Walk straight ahead', 'Head forward'],
    'LEFT': ['Turn left', 'Take a left', 'Make a left turn', 'Turn to your left', 'Head left', 'Move left'],
    'S_LEFT': ['Turn slight left', 'Take a slight left', 'Make a gentle left turn', 'Drift left slightly', 'Lean a little left', 'Gradually turn left'],
    'RIGHT': ['Turn right', 'Take a right', 'Make a right turn', 'Turn to your right', 'Head right', 'Move right'],
    'S_RIGHT': ['Turn slight right', 'Take a slight right', 'Make a gentle right turn', 'Drift right slightly', 'Lean a little right', 'Gradually turn right'],
    'END': ['Destination arrived', 'You\'ve arrived', 'Destination reached', 'You\'re at your destination'],
}

distantDirectionMessages = {
    'STRAIGHT': ['Continue forward for approximately :{distance}', 'Keep going straight for approximately :{distance}', 'Proceed forward for approximately :{distance}', 'Walk straight ahead for approximately :{distance}', 'Head forward for approximately :{distance}'],
    'LEFT': ['In approximately :{distance} turn left', 'In approximately :{distance} take a left', 'In approximately :{distance} make a left turn', 'In approximately :{distance} turn to your left', 'In approximately :{distance} head left', 'In approximately :{distance} move left'],
    'S_LEFT': ['In approximately :{distance} turn slight left', 'In approximately :{distance} take a slight left', 'In approximately :{distance} make a gentle left turn', 'In approximately :{distance} drift left slightly', 'In approximately :{distance} lean a little left', 'In approximately :{distance} gradually turn left'],
    'RIGHT': ['In approximately :{distance} turn right', 'In approximately :{distance} take a right', 'In approximately :{distance} make a right turn', 'In approximately :{distance} turn to your right', 'In approximately :{distance} head right', 'In approximately :{distance} move right'],
    'S_RIGHT': ['Turn slight right for approximately :{distance}', 'Take a slight right for approximately :{distance}', 'Make a gentle right turn for approximately :{distance}', 'Drift right slightly for approximately :{distance}', 'Lean a little right for approximately :{distance}', 'Gradually turn right for approximately :{distance}'],
    'END': ['In approximately :{distance} destination arrived', 'In approximately :{distance} you\'ve arrived', 'In approximately :{distance} destination reached', 'In approximately :{distance} you\'re at your destination'],
}


def getDirectionMessage(direction: str, getDistantMsg: bool = False) -> str:
    try:
        normalized_direction = {
            directionTypes['S_LEFT']: 'S_LEFT',
            directionTypes['S_RIGHT']: 'S_RIGHT',
        }.get(direction, direction)

        validDirections = list((distantDirectionMessages if getDistantMsg else directionMessages).keys())
        if normalized_direction not in validDirections:
            return 'Unknown direction'
        
        validMessages = (distantDirectionMessages if getDistantMsg else directionMessages).get(normalized_direction)
        randomIndex = random.randrange(0, len(validMessages))
        return validMessages[randomIndex]
    except Exception as e:
        print(e)


# finalData = []
fps = 30

# def get_chunks(xs: List[Any], size) -> List[List[Any]]:
#     n = int(size)
#     return [xs] if len(xs) <= n else [xs[:n]] + get_chunks(xs[n:], n)

def get_chunks(xs: List[Any], size: int) -> List[List[Any]]:
    return [xs[i:i + size] for i in range(0, len(xs), size)]


def get_verdict(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    try:
        direction_meta = {}
        for item in data:
            direction = item.get('directionIcon', '').lower()
            direction_meta[direction] = direction_meta.get(direction, 0) + 1
        
        total = sum(direction_meta.values()) or 1
        direction_counts = sorted([
            {
                'directionIcon': dir,
                'count': count,
                'percent': (count / total) * 100
            }
            for dir, count in direction_meta.items()
        ], key=lambda x: x['percent'], reverse=True)

        verdict = None
        if direction_counts:
            if len(direction_counts) > 2:
                if (
                    (direction_counts[0]['directionIcon'].lower() == directionTypes['LEFT'] and direction_counts[1]['directionIcon'].lower() == directionTypes['S_LEFT']) or
                    (direction_counts[1]['directionIcon'].lower() == directionTypes['LEFT'] and direction_counts[0]['directionIcon'].lower() == directionTypes['S_LEFT']) or
                    (direction_counts[0]['directionIcon'].lower() == directionTypes['RIGHT'] and direction_counts[1]['directionIcon'].lower() == directionTypes['S_RIGHT']) or
                    (direction_counts[1]['directionIcon'].lower() == directionTypes['RIGHT'] and direction_counts[0]['directionIcon'].lower() == directionTypes['S_RIGHT'])
                ):
                    if (direction_counts[1]['percent'] + direction_counts[0]['percent']) >= threshold:
                        if directionTypes['LEFT'] in direction_counts[0]['directionIcon'].lower():
                            verdict = directionTypes['S_LEFT']
                        elif directionTypes['RIGHT'] in direction_counts[0]['directionIcon'].lower():
                            verdict = directionTypes['S_RIGHT']
                elif direction_counts[0]['percent'] >= threshold:
                    verdict = direction_counts[0]['directionIcon']
            else:
                if direction_counts[0]['percent'] >= threshold:
                    verdict = direction_counts[0]['directionIcon']

        time_gap = {
            'tStart': data[0]['timestamp'] if data else None,
            'tEnd': data[-1]['timestamp'] if data else None
        }

        return {'verdict': verdict, 'directionCounts': direction_counts, 'timeGap': time_gap}
    except Exception as e:
        print('Error in get_verdict fn')
        print(e)
        return None
    

def process_verdict_old(data: List[Dict[str, Any]], verdict_meta: Dict[str, Any]):
    if check_time_validity(data[0]['timestamp']):
        seconds = data[0]['timestamp']
        target_min = seconds // 60
        target_sec = seconds % 60
        return {
            'directionIcon': verdict_meta.get('verdict'),
            'seconds': seconds,
            'format': f"{target_min} min {target_sec} sec",
        }
    else:
        return None

def process_verdict(data: List[Dict[str, Any]], verdict_meta: Dict[str, Any]):
    try:
        seconds = data[0]['timestamp']
        target_min = seconds // 60
        target_sec = seconds % 60
        return {
            'directionIcon': verdict_meta.get('verdict'),
            'seconds': seconds,
            'format': f"{target_min} min {target_sec} sec",
        }
    except Exception as e:
        print('Error while processing verdict')
        print(e)
        return None

def format_seconds(seconds: int) -> str:
    target_min = seconds // 60
    target_sec = seconds % 60
    return f"{target_min} min {target_sec} sec"

def check_time_validity(time: int) -> bool:
    return not any(el['directionTime'] == time for el in finalData)

def sliding_window(data, fps):
    try:
        chunks = get_chunks(data, int(fps * 1))
        final_data = []
        for chunk in chunks:
            verdict_meta = get_verdict(chunk)
            if verdict_meta.get('verdict'):
                pv = process_verdict(chunk, verdict_meta) # TODO: We need to pass finalData as 3rd parameter
                if pv != None:
                    final_data.append(pv)
        return final_data
    except Exception as e:
        print('Error in sliding_window')
        print(e)

def sliding_window_main(master, file_name, fps, total_frames):
    try:
        data = copy(master)
        finalData = sliding_window(data, fps)
        # with open(f'multithread-res/{file_name}.txt', 'w', encoding='utf-8') as f:
        #     json.dump({'data': finalData}, f)
        outputData = process_sliding_window_output(finalData)
        prev = None
        straightStubData = []
        if (outputData[0])['directionIcon'] != 'straight' and (outputData[0])['startTime'] != 0:
            straightStubData.append({
                'directionIcon': 'straight',
                'startTime': 0,
                'endTime': (outputData[0])['startTime'],
                # 'startFormat': format_seconds(0),
                # 'endFormat': format_seconds((outputData[0])['startTime']),
                'message': get_direction_mesage('straight'),
            })
        for index, el in enumerate(outputData):
            if prev == None:
                straightStubData.append(el)
            else:
                if (prev['endTime'] != el['startTime']):
                    straightStubData.append({
                        'directionIcon': 'straight',
                        'startTime': prev['endTime'],
                        'endTime': el['startTime'],
                        'message': get_direction_mesage('straight'),
                    })
                    straightStubData.append(el)
                else:
                    straightStubData.append(el)
            prev = el
        
        last_second_in_video = round(total_frames/fps)
        if len(straightStubData) > 0 and (straightStubData[-1])['endTime'] > last_second_in_video:
            # Change the endTime of last detected direction to be => last_second_in_video
            (straightStubData[-1])['endTime'] = last_second_in_video

        # Set the 'END' Direction
        if len(straightStubData) > 0:
            if ((straightStubData[-1])['endTime'] - (straightStubData[-1])['startTime']) == 1:
                if (straightStubData[-1])['endTime'] != last_second_in_video:
                    # Append a new 'END' direction
                    straightStubData.append({
                        'directionIcon': 'END',
                        'message': getDirectionMessage('END'),
                        'startTime': (straightStubData[-1])['endTime'],
                        'endTime': last_second_in_video,
                    })
                else:
                    # Change the last direction to 'END'
                    (straightStubData[-1])['directionIcon'] = 'END'
                # The last direction is of one sec only, replace the direction with 'END'
            elif ((straightStubData[-1])['endTime'] - (straightStubData[-1])['startTime']) > 1:
                # The last detected direction is of more than 1 seconds
                if (straightStubData[-1])['endTime'] != last_second_in_video:
                    # Append a new 'END' direction
                    straightStubData.append({
                        'directionIcon': 'END',
                        'message': getDirectionMessage('END'),
                        'startTime': (straightStubData[-1])['endTime'],
                        'endTime': last_second_in_video,
                    })
                else:
                    # 1) Need to change the existing last detected direction, change the endTime = endTime - 1
                    new_end_time = (straightStubData[-1])['endTime'] - 1
                    (straightStubData[-1])['endTime'] = new_end_time
                    # 2) And then append the 'END' direction
                    straightStubData.append({
                        'directionIcon': 'END',
                        'message': getDirectionMessage('END'),
                        'startTime': new_end_time,
                        'endTime': last_second_in_video,
                    })


        
        if (straightStubData[0]['startTime'] != 0):
            straightStubData.insert(0, {
                'directionIcon': 'straight',
                'message': get_direction_mesage('straight'),
                'startTime': 0,
                'endTime': straightStubData[0]['startTime'],
            })
        # finalDataRes = adjustTime(straightStubData)
        # if finalDataRes == None:
        #     return None
        # with open(f'multithread-res/{file_name}.txt', 'w', encoding='utf-8') as f:
        #     json.dump({'data': straightStubData}, f)
        return straightStubData
    except Exception as e:
        print('Error in sliding_window_main')
        print(e)
        return None

def adjustTime(master):
    try:
        all_turns = ['right', 'slight right', 'left', 'slight left']
        total_len = len(master)
        processesd_master = []
        for index, el in enumerate(master):
            curr_p = el
            next_p = None
            if index+1 <= total_len-1:
                next_p = master[index+1]
            
            if (curr_p.get('directionIcon') == 'straight' and next_p != None and  any( direction_name == next_p.get('directionIcon') for direction_name in all_turns)):
                temp = el
                temp['endTime'] = next_p.get('startTime') - 2
                processesd_master.append(temp)
            elif curr_p.get('directionIcon') == 'straight' and next_p == None:
                processesd_master.append(el)
            elif any( direction_name == curr_p.get('directionIcon') for direction_name in all_turns):
                if len(processesd_master) == 0:
                    processesd_master.append(el)
                else:
                    temp = processesd_master[-1]
                    el['startTime'] = temp.get('endTime')
                    processesd_master.append(el)
            else:
                processesd_master.append(el)
        return processesd_master
    except Exception as e:
        print('Error while adjusting time')
        print(e)
        return None

# def check_same_group(current_group_data: Dict[str, Any], data: Dict[str, Any]) -> bool:
#     data_direction_is_left = directionTypes['LEFT'] in data['directionIcon'].lower()
#     same_direction = (
#         directionTypes['LEFT'] in current_group_data['directionIcon']
#         if data_direction_is_left
#         else directionTypes['RIGHT'] in current_group_data['directionIcon']
#     )
#     if not same_direction:
#         return False
#     return data['seconds'] - current_group_data['seconds'] <= 2.5

def check_same_group(current_group_data: Dict[str, Any], data: Dict[str, Any]) -> bool:
    data_direction = data['directionIcon']
    current_direction = current_group_data['directionIcon']
    

    # Check if directions match, including STRAIGHT
    same_direction = (
        (directionTypes['LEFT'].lower() in current_direction.lower() and directionTypes['LEFT'].lower() in data_direction.lower()) or
        (directionTypes['RIGHT'].lower() in current_direction.lower() and directionTypes['RIGHT'].lower() in data_direction.lower()) or
        (directionTypes['STRAIGHT'].lower() in current_direction.lower() and directionTypes['STRAIGHT'].lower() in data_direction.lower())
    )
    return same_direction
    

# def check_same_group(current_group_data: Dict[str, Any], data: Dict[str, Any]) -> bool:
#     data_direction = data['directionIcon']
#     current_direction = current_group_data['directionIcon']

#     # Check if directions match, including STRAIGHT
#     same_direction = (
#         (directionTypes['LEFT'] in current_direction and directionTypes['LEFT'] in data_direction) or
#         (directionTypes['RIGHT'] in current_direction and directionTypes['RIGHT'] in data_direction) or
#         (directionTypes['STRAIGHT'] in current_direction and directionTypes['STRAIGHT'] in data_direction)
#     )
    
#     # Return False if directions do not match
#     if not same_direction:
#         return False
    
#     # Check if the time difference is within 2.5 seconds
#     return data['seconds'] - current_group_data['seconds'] <= 2.5


def process_sliding_window_output(data):
    try:
        current_group_lead = None
        group = []
        grouped_data = []
        final_data = []

        def clear():
            nonlocal current_group_lead, group
            current_group_lead = None
            group = []

        def make_new_group_lead(curr_data):
            nonlocal current_group_lead, group
            current_group_lead = {
                'directionIcon': curr_data['directionIcon'],
                'seconds': curr_data['seconds'],
            }
            group.append(current_group_lead)

        # direction_data = [el for el in data if el['directionIcon'] != directionTypes['STRAIGHT']]
        direction_data = [el for el in data ]
        
        if len(direction_data) == 0 and len(data) > 0:
            # This will be the case when all the direction are straight
            final_data.append({
                'startTime': round(((data[0])['seconds'])),
                'endTime': round(((data[-1])['seconds'])),
                'directionIcon': directionTypes['STRAIGHT'],
                'message': get_direction_mesage(directionTypes['STRAIGHT']),
                # 'startFormat': format_seconds(int(start)),
                # 'endFormat': format_seconds(int(end)),
            })
        else:
            if direction_data == None:
                direction_data = []

            for current in direction_data:
                if current_group_lead is None:
                    make_new_group_lead(current)
                    continue

                if check_same_group(current_group_lead, current):
                    group.append(current)
                else:
                    if group:
                        grouped_data.append(group)
                    clear()
                    make_new_group_lead(current)

            if group:
                grouped_data.append(group)
                clear()

            for group in grouped_data:
                start = group[0]['seconds']
                end = group[-1]['seconds'] + 1 if len(group) > 1 else start + 1
                final_data.append({
                    'startTime': round(start),
                    'endTime': round(end),
                    'directionIcon': group[0]['directionIcon'],
                    'message': get_direction_mesage(group[0]['directionIcon']),
                    # 'startFormat': format_seconds(int(start)),
                    # 'endFormat': format_seconds(int(end)),
                })
        return final_data
    except Exception as e:
        print('Error while processing sliding window output')
        print(e)
        return None

def get_direction_mesage(direction):
    try:    
        message = ""
        if direction.lower() == directionTypes['STRAIGHT'].lower():
            message = "Go straight"
        elif direction.lower() == directionTypes['LEFT'].lower():
            message = "Turn left"
        elif direction.lower() == directionTypes['S_LEFT'].lower():
            message = "Turn slight left"
        elif direction.lower() == directionTypes['RIGHT'].lower():
            message = "Turn right"
        elif direction.lower() == directionTypes['S_RIGHT'].lower():
            message = "Turn slight right"
        
        return message
    except Exception as e:
        print('Error in get_direction_mesage fn')

