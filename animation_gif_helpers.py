
from copy import copy


all_turns = ['RIGHT', 'SLIGHT_RIGHT', 'LEFT', 'SLIGHT_LEFT', 'END']
sharp_turns = ['RIGHT', 'LEFT']




def checkIfTurn(curr_turn_name, sharp_only = False):
    if sharp_only == False:
        return any( direction_name != 'END' and direction_name == curr_turn_name for direction_name in all_turns)
    else:
        return any( direction_name != 'END' and direction_name == curr_turn_name for direction_name in sharp_turns)



def processDirections(master):
    try:
        master = preProcess(master)
        for index, el in enumerate(master):
            t = el.get('startTime')
            tt = type(t)
        total_len = len(master)
        processedDirections = []

        if total_len == 1:
            processedDirections.append(master[0])
        else:
            for index, el in enumerate(master):
                # initialize curr and next pointers
                curr_p = el
                next_p = None
                prev_p = None
                if index+1 <= total_len-1:
                    next_p = master[index+1]
                if index != 0:
                    prev_p = master[index-1]

                
                # process straight directions
                if (curr_p.get('directionIcon') == 'STRAIGHT'):
                    # Current is straight and next is any direction
                    if (next_p != None and checkIfTurn(next_p.get('directionIcon')) == True) or (index > 0 and index != total_len-1 and checkIfTurn(next_p.get('directionIcon')) == True):
                        if checkIfTurn(next_p.get('directionIcon'), True) == True:
                            # Sharp turn
                            temp = copy(curr_p)
                            temp['endTime'] = max(curr_p.get('startTime'), (next_p.get('startTime') - 2))
                            processedDirections.append(temp)
                        else:
                            temp = copy(curr_p)
                            temp['endTime'] = max(curr_p.get('startTime'), (next_p.get('startTime') - 2))
                            processedDirections.append(temp)
                    else:
                        processedDirections.append(curr_p)
                elif checkIfTurn(curr_p.get('directionIcon')) == True:
                    if (index == 0):
                        temp = copy(curr_p)
                        temp['sticky'] = True
                        temp['fadeout'] = True
                        processedDirections.append(temp)
                    elif (index == total_len-1):
                        if checkIfTurn(prev_p.get('directionIcon')) == True:
                            temp = copy(curr_p)
                            temp['sticky'] = True
                            temp['fadeout'] = True
                            processedDirections.append(temp)
                        else:
                            # prev was straight
                            if checkIfTurn(curr_p.get('directionIcon'), True): # current is Sharp left/right
                                temp = copy(curr_p)
                                temp['sticky'] = True
                                temp['fadeout'] = True
                                temp['startTime'] = (processedDirections[-1]).get('endTime')
                                processedDirections.append(temp)
                            else:
                                # Current is Slight left/right

                                # Append pre-slight left/right
                                sticky_temp = copy(curr_p)
                                sticky_temp['sticky'] = True
                                sticky_temp['fadeout'] = True
                                sticky_temp['startTime'] = (processedDirections[-1]).get('endTime')
                                sticky_temp['endTime'] = curr_p.get('startTime')
                                processedDirections.append(sticky_temp)

                                # Append the orignal slight left/right duration
                                temp = copy(curr_p)
                                temp['fadeout'] = True
                                processedDirections.append(temp)
                    elif (index > 0 and index < total_len-1): # somewhere in between
                        if (prev_p != None and checkIfTurn(prev_p.get('directionIcon')) == True):
                            # Current and prev are both turns
                            if checkIfTurn(curr_p.get('directionIcon'), True):
                                temp = copy(curr_p)
                                temp['sticky'] = True
                                temp['fadeout'] = True
                                processedDirections.append(temp)
                            else:
                                temp = copy(curr_p)
                                temp['sticky'] = True
                                temp['fadeout'] = True
                                processedDirections.append(temp)
                        else:
                            # Prev was straight, current is turn
                            if checkIfTurn(curr_p.get('directionIcon'), True): # current is Sharp left/right
                                temp = copy(curr_p)
                                temp['sticky'] = True
                                temp['fadeout'] = True
                                temp['startTime'] = (processedDirections[-1]).get('endTime')
                                processedDirections.append(temp)
                            else:
                                # Current is Slight left/right

                                # Append pre-slight left/right
                                sticky_temp = copy(curr_p)
                                sticky_temp['sticky'] = True
                                sticky_temp['fadeout'] = True
                                sticky_temp['startTime'] = (processedDirections[-1]).get('endTime')
                                sticky_temp['endTime'] = curr_p.get('startTime')
                                processedDirections.append(sticky_temp)

                                # Append the orignal slight left/right duration
                                temp = copy(curr_p)
                                temp['fadeout'] = True
                                processedDirections.append(temp)
                            # sticky_temp = copy(curr_p)
                            # sticky_temp['startTime'] = (processedDirections[-1]).get('endTime')
                            # sticky_temp['sticky'] = True
                            # sticky_temp['endTime'] = curr_p.get('startTime')
                            # # Push the sticky arrow
                            # processedDirections.append(sticky_temp)
                            
                            # temp = copy(curr_p)
                            # processedDirections.append(temp)        

                if len(processedDirections) > 0:
                    temp = copy(processedDirections[-1])
                    temp['startTime'] = int(temp['startTime'])
                    temp['endTime'] = int(temp['endTime'])
                    processedDirections[-1] = temp
        return processedDirections
    except Exception as e:
        print(e)
        return None

def preProcess(data):
    try:
        if len(data) == 0:
            return data
        if (data[0])['startTime'] != 0 and (data[0])['startTime'] != '0':
            # add straight direction at start of video
            if int((data[0])['startTime']) > 1:
                data.insert(0, {
                    "directionIcon": "STRAIGHT",
                    "endTime": int((data[0])['startTime']),
                    "description": "Go straight",
                    "message": "Go straight",
                    "startTime": 0
                })
        # Change directions other than turns, straight to => straight
        for index, el in enumerate(data):
            if any( direction_name == el['directionIcon'] for direction_name in all_turns) == False or el['directionIcon'] == 'END':
                el['directionIcon'] = 'STRAIGHT'
            el['startTime'] = int(el['startTime'])
            el['endTime'] = int(el['endTime'])
        resData = []
        # Fill gaps between directions with 'STRAIGHT' direction
        prev = None
        for index, el in enumerate(data):
            if index-1 >= 0:
                prev = data[index-1]
            
            if prev == None:
                resData.append(el)
                continue
            if prev['endTime'] != el['startTime']:
                if (int(el['startTime']) - int(prev['endTime']) > 1):
                    resData.append({
                        "directionIcon": "STRAIGHT",
                        "endTime": int(el['startTime']),
                        "description": "Go straight",
                        "message": "Go straight",
                        "startTime": int(prev['endTime'])
                    })
                resData.append(el)
            
            else:
                resData.append(el)

        
        return resData
    except Exception as e:
        print(e)
        return None