import json
from typing import List, Dict, Any
import os

threshold = 90
directionTypes = {
    'STRAIGHT': 'straight',
    'LEFT': 'left',
    'S_LEFT': 'slight left',
    'RIGHT': 'right',
    'S_RIGHT': 'slight right',
}

directionMessages = {
    'STRAIGHT': 'Go straight',
    'LEFT': 'Turn left',
    'S_LEFT': 'Turn slight left',
    'RIGHT': 'Turn right',
    'S_RIGHT': 'Turn slight right',
}

finalData = []
fps = 30

# def get_chunks(xs: List[Any], size) -> List[List[Any]]:
#     n = int(size)
#     return [xs] if len(xs) <= n else [xs[:n]] + get_chunks(xs[n:], n)

def get_chunks(xs: List[Any], size: int) -> List[List[Any]]:
    return [xs[i:i + size] for i in range(0, len(xs), size)]


def get_verdict(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    direction_meta = {}
    for item in data:
        direction = item.get('direction', '').lower()
        direction_meta[direction] = direction_meta.get(direction, 0) + 1
    
    total = sum(direction_meta.values()) or 1
    direction_counts = sorted([
        {
            'direction': dir,
            'count': count,
            'percent': (count / total) * 100
        }
        for dir, count in direction_meta.items()
    ], key=lambda x: x['percent'], reverse=True)

    verdict = None
    if direction_counts:
        if len(direction_counts) > 2:
            if (
                (direction_counts[0]['direction'].lower() == directionTypes['LEFT'] and direction_counts[1]['direction'].lower() == directionTypes['S_LEFT']) or
                (direction_counts[1]['direction'].lower() == directionTypes['LEFT'] and direction_counts[0]['direction'].lower() == directionTypes['S_LEFT']) or
                (direction_counts[0]['direction'].lower() == directionTypes['RIGHT'] and direction_counts[1]['direction'].lower() == directionTypes['S_RIGHT']) or
                (direction_counts[1]['direction'].lower() == directionTypes['RIGHT'] and direction_counts[0]['direction'].lower() == directionTypes['S_RIGHT'])
            ):
                if (direction_counts[1]['percent'] + direction_counts[0]['percent']) >= threshold:
                    if directionTypes['LEFT'] in direction_counts[0]['direction'].lower():
                        verdict = directionTypes['S_LEFT']
                    elif directionTypes['RIGHT'] in direction_counts[0]['direction'].lower():
                        verdict = directionTypes['S_RIGHT']
            elif direction_counts[0]['percent'] >= threshold:
                verdict = direction_counts[0]['direction']
        else:
            if direction_counts[0]['percent'] >= threshold:
                verdict = direction_counts[0]['direction']

    time_gap = {
        'tStart': data[0]['timestamp'] if data else None,
        'tEnd': data[-1]['timestamp'] if data else None
    }

    return {'verdict': verdict, 'directionCounts': direction_counts, 'timeGap': time_gap}

def process_verdict(data: List[Dict[str, Any]], verdict_meta: Dict[str, Any]):
    if check_time_validity(data[0]['timestamp']):
        seconds = data[0]['timestamp']
        target_min = seconds // 60
        target_sec = seconds % 60
        return {
            'direction': verdict_meta.get('verdict'),
            'seconds': seconds,
            'format': f"{target_min} min {target_sec} sec",
        }
    else:
        return None

def format_seconds(seconds: int) -> str:
    target_min = seconds // 60
    target_sec = seconds % 60
    return f"{target_min} min {target_sec} sec"

def check_time_validity(time: int) -> bool:
    print(finalData)
    return not any(el['directionTime'] == time for el in finalData)

def sliding_window(data, fps):
    try:
        chunks = get_chunks(data, int(fps * 1))
        final_data = []
        for chunk in chunks:
            verdict_meta = get_verdict(chunk)
            if verdict_meta.get('verdict'):
                pv = process_verdict(chunk, verdict_meta)
                # print('pv')
                # print(pv)
                if pv != None:
                    final_data.append(pv)
        return final_data
    except Exception as e:
        print('Error in sliding_window')
        print(e)

def sliding_window_main(master, file_name, fps, total_frames):
    try:
        data = []
        for item in master:
            if item != None and len(item) > 0:
                data.extend(item['data'])
        finalData = sliding_window(data, fps)
        
        outputData = process_sliding_window_output(finalData)
        # with open(f'multithread-res/{file_name}.txt', 'w', encoding='utf-8') as f:
        #     json.dump({'data': outputData}, f)
        prev = None
        straightStubData = []
        if (outputData[0])['direction'] != 'straight' and (outputData[0])['start'] != 0:
            straightStubData.append({
                'direction': 'straight',
                'start': 0,
                'end': (outputData[0])['start'],
                # 'startFormat': format_seconds(0),
                # 'endFormat': format_seconds((outputData[0])['start']),
                'message': get_direction_mesage('straight'),
            })
        for index, el in enumerate(outputData):
            print(prev)
            if prev == None:
                straightStubData.append(el)
            else:
                if (prev['end'] != el['start']):
                    straightStubData.append({
                        'direction': 'straight',
                        'start': prev['end'],
                        'end': el['start'],
                        # 'startFormat': format_seconds(prev['end']),
                        # 'endFormat': format_seconds(el['start']),
                        'message': get_direction_mesage('straight'),
                    })
                    straightStubData.append(el)
                else:
                    straightStubData.append(el)
            prev = el
        
        last_second_in_video = int(total_frames/fps)
        if (straightStubData[-1])['end'] != last_second_in_video:
            straightStubData.append({
                'direction': 'straight',
                'message': get_direction_mesage('straight'),
                'start': (straightStubData[-1])['end'],
                'end': last_second_in_video,
                # 'startFormat': format_seconds((straightStubData[-1])['end']),
                # 'endFormat': format_seconds(last_second_in_video),
            })
        
        if (straightStubData[0]['start'] != 0):
            straightStubData.insert(0, {
                'direction': 'straight',
                'message': get_direction_mesage('straight'),
                'start': 0,
                'end': straightStubData[0]['start'],
                # 'startFormat': format_seconds(0),
                # 'endFormat': format_seconds(straightStubData[0]['start']),
            })
        # finalDataRes = adjustTime(straightStubData)
        # if finalDataRes == None:
        #     return None
        with open(f'multithread-res/{file_name}.txt', 'w', encoding='utf-8') as f:
            json.dump({'data': straightStubData}, f)
        print('File write done!!')
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
            
            if (curr_p.get('direction') == 'straight' and next_p != None and  any( direction_name == next_p.get('direction') for direction_name in all_turns)):
                temp = el
                temp['end'] = next_p.get('start') - 2
                processesd_master.append(temp)
            elif curr_p.get('direction') == 'straight' and next_p == None:
                processesd_master.append(el)
            elif any( direction_name == curr_p.get('direction') for direction_name in all_turns):
                if len(processesd_master) == 0:
                    processesd_master.append(el)
                else:
                    temp = processesd_master[-1]
                    el['start'] = temp.get('end')
                    processesd_master.append(el)
            else:
                processesd_master.append(el)
        return processesd_master
    except Exception as e:
        print('Error while adjusting time')
        print(e)
        return None

def check_same_group(current_group_data: Dict[str, Any], data: Dict[str, Any]) -> bool:
    data_direction_is_left = directionTypes['LEFT'] in data['direction'].lower()
    same_direction = (
        directionTypes['LEFT'] in current_group_data['direction']
        if data_direction_is_left
        else directionTypes['RIGHT'] in current_group_data['direction']
    )
    if not same_direction:
        return False
    return data['seconds'] - current_group_data['seconds'] <= 2.5

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
                'direction': curr_data['direction'],
                'seconds': curr_data['seconds'],
            }
            group.append(current_group_lead)

        direction_data = [el for el in data if el['direction'] != directionTypes['STRAIGHT']]
        
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
                'start': int(start),
                'end': int(end),
                'direction': group[0]['direction'],
                'message': get_direction_mesage(group[0]['direction']),
                # 'startFormat': format_seconds(int(start)),
                # 'endFormat': format_seconds(int(end)),
            })
        print('finall!!!!')
        print(final_data)
        return final_data
    except Exception as e:
        print('Error while processing sliding window output')
        print(e)


def get_direction_mesage(direction):
    try:    
        message = ""
        if direction.lower() == directionTypes['STRAIGHT']:
            message = "Go straight"
        elif direction.lower() == directionTypes['LEFT']:
            message = "Turn left"
        elif direction.lower() == directionTypes['S_LEFT']:
            message = "Turn slight left"
        elif direction.lower() == directionTypes['RIGHT']:
            message = "Turn right"
        elif direction.lower() == directionTypes['S_RIGHT']:
            message = "Turn slight right"
        
        return message
    except Exception as e:
        print('Error in get_direction_mesage fn')

