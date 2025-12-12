import os
from copy import copy
from PIL import Image
import numpy as np
from helpers import upload_multiple_files, check_multiple_objects, download_multiple_files


gif_path = 'newGifs/'
new_gif_directory_path = 'colored_gifs/'
bucket_name = 'media.rtme.us'
files = os.listdir(gif_path)


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


def tint_gif_with_shading(input_path, output_path, hex_color, min_brightness=0.3):
    """
    min_brightness controls darkness floor:
    - 0.0 = full shading (like Script 1)
    - 0.3 = slightly boosted shadows
    - 0.5 = Script 2 default
    """
    try:
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        tint = np.array([r, g, b], dtype=float)

        img = Image.open(input_path)
        frames = []

        for f in range(img.n_frames):
            img.seek(f)
            frame = img.convert("RGBA")
            arr = np.array(frame).astype(float)

            rgb = arr[..., :3]
            alpha = arr[..., 3]

            # luminance 0–1
            lum = (0.299*rgb[...,0] + 0.587*rgb[...,1] + 0.114*rgb[...,2]) / 255.0

            # Adjustable brightness floor
            brightness_factor = min_brightness + (lum * (1 - min_brightness))

            rgb_tinted = (tint * brightness_factor[..., None]).clip(0, 255)

            new_arr = np.dstack([rgb_tinted, alpha]).astype(np.uint8)
            frames.append(Image.fromarray(new_arr, "RGBA"))

        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            loop=0,
            disposal=2
        )
        return True
    except Exception as e:
        print(e)
        return None


def generate_colored_animations(hexColor, routeId):
    try:
        for file_name in files:
            new_file_name = f'{routeId}-{hexColor}-{file_name}'
            result = tint_gif_with_shading(f'{gif_path}{file_name}', f'{new_gif_directory_path}{new_file_name}', hexColor)
            if result != True:
                raise Exception('Gif tinting error')
        return True
    except Exception as e:
        print(e)
        return None

def upload_colored_gifs(hexColor, routeId, env):
    try:    
        upload_keys = []
        for gif_name in files:
            local_path = f'colored_gifs/{routeId}-{hexColor}-{gif_name}'
            s3_path = f'{env}/location_gifs/{hexColor}-{gif_name}'
            upload_keys.append((local_path, s3_path))
        upload_multiple_files(upload_keys, bucket_name)
        return True
    except Exception as e:
        print(e)
        return None
        

def generate_color_gifs_and_upload(hexColor, routeId, env = 'dev'):
    try:
        color_result = generate_colored_animations(hexColor, routeId)
        if color_result != True:
            raise Exception('Color generation error')
        print(f'Color generation successful for {hexColor}')

        # now save this file to S3
        uploaded_color_gif_res = upload_colored_gifs(hexColor, routeId, env)
        if uploaded_color_gif_res != True:
            print('Color gif upload error')
        
        return True
    except Exception as e:
        print(e)
        return None


def manage_colored_gifs(location_color_hex, routeId, env='dev'):
    try:
        if location_color_hex == None: return None
        
        hex_color = location_color_hex.lstrip('#')

        keys = [
            f'{env}/location_gifs/{hex_color}-{file_name}' for file_name in files
        ]
        res = check_multiple_objects(bucket_name, keys)
        all_objects_available_in_s3 = True
        for value in res.values():
            if value == False:
                all_objects_available_in_s3 = False
                break
        
        if all_objects_available_in_s3 == True:
            download_res = download_multiple_files(bucket_name, keys, 'colored_gifs', routeId)
            all_objects_saved = True
            for value in download_res.values():
                if value == False:
                    all_objects_saved = False
                    break
            print('Image found in S3')
            if all_objects_saved == False:
                arrow_color_success = generate_color_gifs_and_upload(location_color_hex, routeId, env)
                if arrow_color_success != True:
                    raise Exception('Arrow color error')    
        else:
            print('Arrow file needs to be generated')
            arrow_color_success = generate_color_gifs_and_upload(location_color_hex, routeId, env)
            if arrow_color_success != True:
                raise Exception('Arrow color error')
    except Exception as e:
        print(e)
        raise Exception('Arrow color error')