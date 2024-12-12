import cv2
import numpy as np
import os
import logging
from copy import copy
from helpers import  update_route_field
logging.basicConfig(level=logging.INFO)


all_turns = ['right', 'slight right', 'left', 'slight left']
sharp_turns = ['right', 'left']
master = [
  {
    "direction": "straight",
    "end": 20,
    "message": "Go straight",
    "start": 0
  },
  {
    "direction": "left",
    "end": 23,
    "message": "Turn left",
    "start": 20,
    "sticky": True,
    "fadeout": True
  },
  {
    "direction": "straight",
    "end": 23,
    "message": "Go straight",
    "start": 23
  },
  {
    "direction": "right",
    "end": 27,
    "message": "Turn right",
    "start": 23,
    "sticky": True,
    "fadeout": True
  },
  {
    "direction": "straight",
    "end": 28,
    "message": "Go straight",
    "start": 27
  }
]
def checkIfTurn(curr_turn_name, sharp_only = False):
    if sharp_only == False:
        return any( direction_name == curr_turn_name for direction_name in all_turns)
    else:
        return any( direction_name == curr_turn_name for direction_name in sharp_turns)


def processDirections(master):
    try:
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
                if (curr_p.get('direction') == 'straight'):
                    # Current is straight and next is any direction
                    if (next_p != None and checkIfTurn(next_p.get('direction')) == True) or (index > 0 and index != total_len-1 and checkIfTurn(next_p.get('direction')) == True):
                        if checkIfTurn(next_p.get('direction'), True) == True:
                            # Sharp turn
                            temp = copy(curr_p)
                            temp['end'] = max(curr_p.get('start'), (next_p.get('start') - 2))
                            processedDirections.append(temp)
                        else:
                            temp = copy(curr_p)
                            temp['end'] = max(curr_p.get('start'), (next_p.get('start') - 2))
                            processedDirections.append(temp)
                    else:
                        processedDirections.append(curr_p)
                elif checkIfTurn(curr_p.get('direction')) == True:
                    if (index == 0):
                        temp = copy(curr_p)
                        temp['sticky'] = True
                        temp['fadeout'] = True
                        processedDirections.append(temp)
                    elif (index == total_len-1):
                        if checkIfTurn(prev_p.get('direction')) == True:
                            temp = copy(curr_p)
                            temp['sticky'] = True
                            temp['fadeout'] = True
                            processedDirections.append(temp)
                        else:
                            # prev was straight
                            if checkIfTurn(curr_p.get('direction'), True): # current is Sharp left/right
                                temp = copy(curr_p)
                                temp['sticky'] = True
                                temp['fadeout'] = True
                                temp['start'] = (processedDirections[-1]).get('end')
                                processedDirections.append(temp)
                            else:
                                # Current is Slight left/right

                                # Append pre-slight left/right
                                sticky_temp = copy(curr_p)
                                sticky_temp['sticky'] = True
                                sticky_temp['fadeout'] = True
                                sticky_temp['start'] = (processedDirections[-1]).get('end')
                                sticky_temp['end'] = curr_p.get('start')
                                processedDirections.append(sticky_temp)

                                # Append the orignal slight left/right duration
                                temp = copy(curr_p)
                                temp['fadeout'] = True
                                processedDirections.append(temp)
                    elif (index > 0 and index < total_len-1): # somewhere in between
                        if (prev_p != None and checkIfTurn(prev_p.get('direction')) == True):
                            # Current and prev are both turns
                            if checkIfTurn(curr_p.get('direction'), True):
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
                            if checkIfTurn(curr_p.get('direction'), True): # current is Sharp left/right
                                temp = copy(curr_p)
                                temp['sticky'] = True
                                temp['fadeout'] = True
                                temp['start'] = (processedDirections[-1]).get('end')
                                processedDirections.append(temp)
                            else:
                                # Current is Slight left/right

                                # Append pre-slight left/right
                                sticky_temp = copy(curr_p)
                                sticky_temp['sticky'] = True
                                sticky_temp['fadeout'] = True
                                sticky_temp['start'] = (processedDirections[-1]).get('end')
                                sticky_temp['end'] = curr_p.get('start')
                                processedDirections.append(sticky_temp)

                                # Append the orignal slight left/right duration
                                temp = copy(curr_p)
                                temp['fadeout'] = True
                                processedDirections.append(temp)
                            # sticky_temp = copy(curr_p)
                            # sticky_temp['start'] = (processedDirections[-1]).get('end')
                            # sticky_temp['sticky'] = True
                            # sticky_temp['end'] = curr_p.get('start')
                            # # Push the sticky arrow
                            # processedDirections.append(sticky_temp)
                            
                            # temp = copy(curr_p)
                            # processedDirections.append(temp)        

                if len(processedDirections) > 0:
                    print('casting..')
                    temp = copy(processedDirections[-1])
                    temp['start'] = int(temp['start'])
                    temp['end'] = int(temp['end'])
                    processedDirections[-1] = temp
        return processedDirections
    except Exception as e:
        print(e)
        return None

# Load arrow images
def load_image(path):
    if os.path.exists(path):
        image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        if image is None:
            logging.info(f"Error: Could not load image at {path}")
        return image
    else:
        logging.info(f"Error: File not found at {path}")
        return None

# Load arrow images
arrow_right = load_image('images/right-arrow.png')
arrow_left = load_image('images/left-arrow.png')
arrow_straight = load_image('images/straight-arrow.png')
arrow_slight_right = load_image('images/slight-right-arrow.png')
arrow_slight_left = load_image('images/slight-left-arrow.png')


left_turns = [arrow_left, arrow_slight_left]
right_turns = [arrow_right, arrow_slight_right]


def get_direction_icon(direction):
    if (direction == 'left'):
        return arrow_left
    elif direction == 'slight left':
        return arrow_slight_left
    elif direction == 'right':
        return arrow_right
    elif direction == 'slight right':
        return arrow_slight_right
    else:
        return arrow_straight 

def arrow_attachment_main_v1(file_name, master):
    try: 
        # Load the video
        cap = cv2.VideoCapture(f'blurred/{file_name}')
        # Get video properties
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        print(f'frame_width => {frame_width}')
        print(f'frame_height => {frame_height}')
        # Define the codec and create VideoWriter object to save the output video
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(f'final/{file_name}', fourcc, fps, (frame_width, frame_height))

        arrows = []
        for el in master:
            icon = get_direction_icon(el['direction'])
            has_sticky = False
            if el.get('sticky') == True:
                has_sticky = True
            arrows.append((el['start'], el['end'], icon, has_sticky, el['direction']))
        
        
        # Define sticky arrows
        # sticky_arrows = [arrow_left, arrow_right]  # Add your sticky arrow images here
        sticky_arrows = []
        # sticky_position = (frame_width // 2, int(frame_height * 0.7))  # Fixed position for sticky arrows
        sticky_position = (frame_width * 0.5, int(frame_height // 2))  # Fixed position for sticky arrows

        # Process the video frame by frame
        frame_number = 0
        current_arrow = None
        arrow_start_time = 0  # Tracks when the current arrow starts
        duration = 3  # Duration for each arrow approach effect (3 seconds)
        turn_duration = 3

        # Add a flag to track if the arrow image changed
        arrow_changed = False
        prev_direction = None
        prev_sticky = None

        prev_start_time = None
        prev_end_time = None
        while cap.isOpened():
            # print(f'frame_number => {frame_number}')
            # logging.info(f'frame process => {frame_number}')
            ret, frame = cap.read()
            if not ret:
                break
            # Get the current time in seconds
            current_time = frame_number / fps

            
            # Determine which arrow to display based on the time intervals
            new_arrow = None
            is_sticky = False
            direction_string = None
            current_start_time = None
            current_end_time = None
            for start_time, end_time, arrow_image, sticky, direction_name in arrows:
                if start_time <= current_time < end_time:
                    current_start_time = start_time
                    current_end_time = end_time
                    new_arrow = arrow_image
                    direction_string = direction_name
                    if direction_name == 'left' or direction_name == 'right' or direction_name == 'slight left' or direction_name == 'slight right': 
                        turn_duration = end_time - start_time
                        duration = end_time - start_time
                    if sticky == True:
                        is_sticky = True
                    if direction_name == 'straight': 
                        duration = 3
                    break
            # If the arrow changes, reset the animation
            if new_arrow is not None:
                if current_arrow is None or not np.array_equal(current_arrow, new_arrow) or (prev_direction != None and prev_sticky != None and (prev_sticky != is_sticky or prev_direction != direction_string)) or (current_start_time != prev_start_time):
                    current_arrow = new_arrow
                    arrow_start_time = current_time  # Reset animation start time
                    arrow_changed = True  # Mark that the arrow has changed
                else:
                    arrow_changed = False  # No change in arrow
            # If there's no valid arrow, continue without overlay
            if current_arrow is None:
                out.write(frame)
                frame_number += 1
                continue

            # Reset animation cycle if current animation completes (Only applicable for straight arrow)
            if (current_time - arrow_start_time) >= duration:
                if direction_string != None and direction_string == 'straight':
                    arrow_start_time = current_time  # Reset the animation cycle for continuous movement

            if current_time > 186 and current_time < 208:
               print(f'duration => {duration}, turn_duration => {turn_duration}, direction => {direction_string} ') 
            # Animate the current arrow (reset if changed, continue if not)
            frame = animate_arrow_approach(frame, current_arrow, current_time, sticky_arrows, sticky_position, duration, arrow_start_time, is_sticky, turn_duration, direction_string)

            # Write the frame to the output video
            out.write(frame)
            
            # Display the video frame (optional)
            # cv2.imshow('Video with Arrows', frame)
            
            # # Break the loop on 'q' key press
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break
            prev_direction = direction_string
            prev_sticky = is_sticky
            prev_start_time = current_start_time
            prev_end_time = current_end_time
            frame_number += 1

        # Release resources
        cap.release()
        out.release()
    except Exception as e:
        logging.info('Error in Arrow attachment')
        logging.info(e)
        try:
            update_route_field(route_id, 'processStatus', 'ARROW_ATTACHMENT_ERROR')
        except Exception as e:
            logging.info('Error while updating DB')

def arrow_attachment_main(file_name, master_pre):
    try: 
        print('master_pre -----------')
        print(master_pre)
        master = processDirections(master_pre)
        print('master------------')
        print(master)

        # master = master_pre
        # Load the video
        cap = cv2.VideoCapture(f'blurred/{file_name}')
        # Get video properties
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        print(f'frame_width => {frame_width}')
        print(f'frame_height => {frame_height}')
        # Define the codec and create VideoWriter object to save the output video
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(f'final/{file_name}', fourcc, fps, (frame_width, frame_height))

        arrows = []
        for el in master:
            icon = get_direction_icon(el['direction'])
            has_sticky = False
            fadeout = False
            if el.get('fadeout') == True:
                print('fadeout True --- ')
                fadeout = True
            if el.get('sticky') == True:
                has_sticky = True
            arrows.append((el['start'], el['end'], icon, has_sticky, el['direction'], fadeout))
        
        
        # Define sticky arrows
        # sticky_arrows = [arrow_left, arrow_right]  # Add your sticky arrow images here
        sticky_arrows = []
        # sticky_position = (frame_width // 2, int(frame_height * 0.7))  # Fixed position for sticky arrows
        sticky_position = (frame_width * 0.5, int(frame_height // 2))  # Fixed position for sticky arrows

        # Process the video frame by frame
        frame_number = 0
        current_arrow = None
        arrow_start_time = 0  # Tracks when the current arrow starts
        duration = 3  # Duration for each arrow approach effect (3 seconds)
        turn_duration = 3

        # Add a flag to track if the arrow image changed
        arrow_changed = False
        prev_direction = None
        prev_sticky = None
        prev_fadeout = None

        prev_start_time = None
        prev_end_time = None
        while cap.isOpened():
            # print(f'frame_number => {frame_number}')
            # logging.info(f'frame process => {frame_number}')
            print('------------------------------------------')
            ret, frame = cap.read()
            if not ret:
                break
            # Get the current time in seconds
            current_time = frame_number / fps

            print(f'frame_number => {frame_number}')
            print(f'current_time => {current_time}')

            # Determine which arrow to display based on the time intervals
            new_arrow = None
            is_sticky = False
            direction_string = None
            current_start_time = None
            current_end_time = None
            current_fade_out = None
            for start_time, end_time, arrow_image, sticky, direction_name, fadeout in arrows:
                if start_time <= current_time < end_time:
                    current_start_time = start_time
                    current_end_time = end_time
                    new_arrow = arrow_image
                    direction_string = direction_name
                    current_fade_out = fadeout
                    if direction_name == 'left' or direction_name == 'right' or direction_name == 'slight left' or direction_name == 'slight right': 
                        turn_duration = end_time - start_time
                        duration = end_time - start_time
                    if sticky == True:
                        is_sticky = True
                    if direction_name == 'straight': 
                        duration = 3
                    break
            print(f'current_start_time => {current_start_time}')
            print(f'current_end_time => {current_end_time}')
            print(f'current_fade_out => {current_fade_out}')
            # If the arrow changes, reset the animation
            if new_arrow is not None:
                if current_arrow is None or not np.array_equal(current_arrow, new_arrow) or (prev_direction != None and prev_sticky != None and (prev_sticky != is_sticky or prev_direction != direction_string)) or (current_start_time != prev_start_time):
                    current_arrow = new_arrow
                    arrow_start_time = current_time  # Reset animation start time
                    arrow_changed = True  # Mark that the arrow has changed
                else:
                    arrow_changed = False  # No change in arrow
            print(f'arrow_changed => {arrow_changed}')
            # If there's no valid arrow, continue without overlay
            if current_arrow is None:
                prev_direction = direction_string
                prev_sticky = is_sticky
                prev_start_time = current_start_time
                prev_end_time = current_end_time
                out.write(frame)
                frame_number += 1
                continue

            # Reset animation cycle if current animation completes (Only applicable for straight arrow)
            if (current_time - arrow_start_time) >= duration:
                if direction_string != None and direction_string == 'straight':
                    print('reset')
                    arrow_start_time = current_time  # Reset the animation cycle for continuous movement
            
            print(f'turn_duration => {turn_duration}')
            print(f'duration => {duration}')
            print(f'direction_string => {direction_string}')
            print(f'is_sticky => {is_sticky}')
            # Animate the current arrow (reset if changed, continue if not)
            frame = animate_arrow_approach(frame, current_arrow, current_time, sticky_arrows, sticky_position, duration, arrow_start_time, is_sticky, turn_duration, direction_string, current_fade_out)

            # Write the frame to the output video
            out.write(frame)
            
            # Display the video frame (optional)
            # cv2.imshow('Video with Arrows', frame)
            
            # # Break the loop on 'q' key press
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break
            prev_direction = direction_string
            prev_sticky = is_sticky
            prev_start_time = current_start_time
            prev_end_time = current_end_time
            frame_number += 1

        # Release resources
        cap.release()
        out.release()
    except Exception as e:
        logging.info('Error in Arrow attachment')
        print(e)
        # try:
        #     update_route_field(route_id, 'processStatus', 'ARROW_ATTACHMENT_ERROR')
        # except Exception as e:
        #     logging.info('Error while updating DB')

# Function to overlay an image on the video frame
def overlay_arrow(frame, arrow_image, position, scale=1.0, opacity=1.0):
    try:
        if arrow_image is None:
            return frame
        
        # Ensure the scale and opacity are valid
        if scale <= 0:
            scale = 0.01  # Minimum positive scale
        if opacity < 0:
            opacity = 0
        elif opacity > 1:
            opacity = 1

        # Resize arrow image based on scale
        height, width, _ = frame.shape
        arrow_h, arrow_w, _ = arrow_image.shape
        new_arrow_h, new_arrow_w = max(1, int(arrow_h * scale)), max(1, int(arrow_w * scale))  # Ensure size > 0
        
        resized_arrow = cv2.resize(arrow_image, (new_arrow_w, new_arrow_h))
        
        # Calculate the position for the arrow (scaled dynamically)
        center_x = position[0] - new_arrow_w // 2
        center_y = position[1] - new_arrow_h // 2

        # Ensure the arrow is within the frame boundaries
        if center_x < 0 and any(np.array_equal(arrow_image, rht_arrow) for rht_arrow in right_turns):
            return frame
        elif center_x < 0 and not any(np.array_equal(arrow_image, rht_arrow) for rht_arrow in right_turns):
            center_x = 0
        if center_y < 0:
            center_y = 0
        if center_x + new_arrow_w > width:
            new_arrow_w = width - center_x
        if center_y + new_arrow_h > height:
            new_arrow_h = height - center_y

        center_x = int(center_x)

        # Extract arrow image's alpha channel (for transparency)
        if resized_arrow.shape[2] == 4:
            arrow_alpha = resized_arrow[:new_arrow_h, :new_arrow_w, 3] / 255.0
            overlay_rgb = resized_arrow[:new_arrow_h, :new_arrow_w, :3]
            # Adjust alpha based on the current opacity level (for the fade-in effect)
            arrow_alpha = arrow_alpha * opacity


            # Blend the arrow image with the frame
            for c in range(0, 3):
                frame[center_y:center_y + new_arrow_h, center_x:center_x + new_arrow_w, c] = (
                    arrow_alpha * overlay_rgb[:, :, c] +
                    (1 - arrow_alpha) * frame[center_y:center_y + new_arrow_h, center_x:center_x + new_arrow_w, c]
                )
        else:
            frame[center_y:center_y + new_arrow_h, center_x:center_x + new_arrow_w] = resized_arrow[:new_arrow_h, :new_arrow_w]
        return frame
    except Exception as e:
        print('Error while overlaying the arrow')
        print(e)
        return e



def animate_arrow_approach(frame, arrow_image, current_time, sticky_arrows, sticky_position, duration=2, arrow_start_time=0, is_sticky=False, turn_duration=3, direction_string = 'straight', fadeout = False):
    """Animate arrow moving left with fade-in and fade-out effects over specified time durations."""
    if arrow_image is None:
        return frame

    # Check if the arrow is sticky
    if False:  # Placeholder, adjust if sticky logic is needed
        scale = 0.4  # Sticky scale
        current_position = sticky_position  # Sticky position
        opacity_progress = 1.0  # Fully opaque for sticky arrows
    else:
        # Define start and end scale values (moderate scaling)
        start_scale = 0.2  # Arrow appears smaller (far away)
        end_scale = 0.6   # Arrow appears at a reasonable size (closer)
        elapsed_time = current_time - arrow_start_time  # Time since the arrow started
        print('here ---- E')
        print(f'elapsed_time => {elapsed_time}')
        print(f'duration => {duration}')
        print(f'elapsed_time type => {type(elapsed_time)}')
        print(f'duration type => {type(duration)}')
        
        if elapsed_time == 0:
            print('dilt--')
            progress = 1.0
        else:
            progress = min(1.0, elapsed_time / int(duration))  # Progress capped at 1.0
        print('here ---- F')
        height, width, _ = frame.shape
        
        if is_sticky:
            start_scale = 0.6  # Sticky scale (no change in scale)
            end_scale = 0.6
            if direction_string == 'slight left':
                start_position = (int(width // 2), int(height * 0.8))
                end_position = (int(width // 2), int(height * 0.8))
            elif direction_string == 'slight right':
                start_position = (int(width // 2), int(height * 0.8))
                end_position = (int(width // 2), int(height * 0.8))
            elif any(np.array_equal(arrow_image, lft_arrow) for lft_arrow in left_turns):
                # Left turns
                print('here ==ll')
                start_position = (int(width // 2), int(height * 0.6))
                end_position = (int(width // 2), int(height * 0.8))
            elif any(np.array_equal(arrow_image, rht_arrow) for rht_arrow in right_turns):
                # Right turns
                start_position = (int(width // 2), int(height * 0.6))
                end_position = (int(width // 2), int(height * 0.8))
        else:
            # Define start and end positions for non-sticky arrows
            if direction_string == 'slight left' or direction_string == 'slight right':
                # Slight left/right turns
                if direction_string == 'slight left':
                    start_position = (int(width * 0.3), int(height * 0.7))
                    end_position = (int(width * 0.9), int(height * 0.9))
                elif direction_string == 'slight right':
                    start_position = (int(width * 0.9), int(height * 0.7))
                    end_position = (int(width * 0.3), int(height * 0.9))
            elif any(np.array_equal(arrow_image, lft_arrow) for lft_arrow in left_turns):
                print('In left turn non-stiovky')
                start_position = (int(width * 0.1), int(height * 0.7))  
                end_position = (int(width + 50), int(height * 0.7))  
            elif any(np.array_equal(arrow_image, rht_arrow) for rht_arrow in right_turns):
                start_position = (int(width * 1), int(height * 0.7))  
                end_position = (-100, int(height * 0.7))  
            else:
                start_position = (int(width * 0.5), int(height * 0.8)) 
                end_position = (int(width * 0.5), height + 100)


        print('here--A')
        # Interpolate scale and position based on progress
        scale = start_scale + (end_scale - start_scale) * progress
        current_position = (
            int(start_position[0] + (end_position[0] - start_position[0]) * progress),
            int(start_position[1] + (end_position[1] - start_position[1]) * progress)
        )

        print('here--B')

        opacity_progress = None
        if direction_string == "straight" or fadeout == False: 
            # Fade-in effect: adjust opacity based on time (first 0.6 seconds of the arrow's animation)
            fade_in_duration = 0.6  # Fade-in period (0.6 seconds)
            if elapsed_time < fade_in_duration:  # Only fade during the first 0.6 seconds
                opacity_progress = elapsed_time / fade_in_duration  # Opacity increases from 0 to 1
            else:
                opacity_progress = 1.0  # After 0.6 seconds, the arrow is fully opaque
        else:
            # Fade-in effect (first 0.6 seconds)
            print('here -- C')
            fade_in_duration = max(turn_duration-1, 1)  # Fade-in period (0.6 seconds)s
            print(f'fade_in_duration => {fade_in_duration}')
            print(f'fade_in_duration type => {type(fade_in_duration)}')
            # if elapsed_time < fade_in_duration:
            #     opacity_progress = elapsed_time / fade_in_duration  # Opacity increases from 0 to 1
            # else:
            # Fade-out effect (after the fade-in, the arrow will fade out)
            remaining_time = current_time - (float(arrow_start_time) + float(fade_in_duration))  # Time after fade-in period
            fade_out_duration = float(turn_duration) - float(fade_in_duration)  # Total duration for fade-out
            if fade_out_duration == 0:
                # This will be thee case when the turn duration is exactly 1 second
                # So there won't be any time for the opacity-reduce animation
                opacity_progress = 1 
            else:
                if remaining_time < fade_out_duration:
                    opacity_progress = 1 - (float(remaining_time) / float(fade_out_duration))  # Opacity decreases from 1 to 0
                else:
                    opacity_progress = 0  # Fully transparent after fade-out duration
    print('Here -D')
    # Overlay the arrow on the frame with calculated scale, position, and opacity
    frame = overlay_arrow(frame, arrow_image, current_position, scale=scale, opacity=opacity_progress)
    
    return frame


# Assuming other variables (like current_time, sticky_arrows, etc.) are defined elsewhere in your code
def animate_arrow_approach_v3(frame, arrow_image, current_time, sticky_arrows, sticky_position, duration=2, arrow_start_time=0, is_sticky = False, turn_duration = 3):
    """Animate arrow moving left with fade-in effect over the first 0.6 seconds, reset position on switch."""
    if arrow_image is None:
        return frame
    
    # Check if the arrow is sticky
    # if is_sticky == True:
    if False:
        scale = 0.4  # Sticky scale
        current_position = sticky_position  # Sticky position
        opacity_progress = 1.0  # Fully opaque for sticky arrows
    else:
        # Define start and end scale values (moderate scaling)
        start_scale = 0.2  # Arrow appears smaller (far away)
        end_scale = 0.9   # Arrow appears at a reasonable size (closer)
        # Calculate progress for non-sticky arrows
        elapsed_time = current_time - arrow_start_time
        # print(f'elapsed_time => {elapsed_time}')
        progress = min(1.0, elapsed_time / duration)  # Progress capped at 1.0
        
        # Define start and end positions (start from 70% of the screen width, moving to the left)
        height, width, _ = frame.shape
        # print(f'turn_duration => {turn_duration}')
        if is_sticky == True:
            start_scale = 0.6 
            end_scale = 0.6   
            if any(np.array_equal(arrow_image, lft_arrow) for lft_arrow in left_turns):
                # Left turns
                start_position = (int(width // 2), int(height * 0.4))
                end_position = (int(width // 2), int(height * 0.8))
            elif any(np.array_equal(arrow_image, rht_arrow) for  rht_arrow in right_turns):
                # Right turns
                start_position = (int(width // 2), int(height * 0.4))
                end_position = (int(width // 2), int(height * 0.8))
        else:
            if any(np.array_equal(arrow_image, lft_arrow) for lft_arrow in left_turns):
                # Left turns
                start_position = (int(width * 0.1), int(height * 0.7))  
                end_position = (int(width + 50), int(height * 0.7))  
            elif any(np.array_equal(arrow_image, rht_arrow) for  rht_arrow in right_turns):
                # Right turns
                start_position = (int(width * 1), int(height * 0.7))  
                end_position = (-100, int(height * 0.7))  
            else:
                # Straight way
                start_position = (int(width * 0.5), int(height * 0.5)) 
                end_position = (int(width * 0.5), height + 100)
        # Interpolate scale and position based on progress
        # scale = start_scale + (end_scale - start_scale) * progress  
        # current_position = (
        #     int(start_position[0] - (start_position[0] - end_position[0]) * progress),  # Move left horizontally
        #     start_position[1]  # Keep the same vertical position
        # )

        scale = start_scale + (end_scale - start_scale) * progress
        current_position = (
            int(start_position[0] + (end_position[0] - start_position[0]) * progress),
            int(start_position[1] + (end_position[1] - start_position[1]) * progress)
        )

        # Fade-in effect: adjust opacity based on time (first 0.6 seconds of the arrow's animation)
        fade_in_duration = 0.6  # Fade-in period (0.6 seconds)
        if elapsed_time < fade_in_duration:  # Only fade during the first 0.6 seconds
            opacity_progress = elapsed_time / fade_in_duration  # Opacity increases from 0 to 1
        else:
            opacity_progress = 1.0  # After 0.6 seconds, the arrow is fully opaque

    # Overlay the arrow on the frame with calculated scale, position, and opacity
    frame = overlay_arrow(frame, arrow_image, current_position, scale=scale, opacity=opacity_progress)
    
    return frame

def animate_arrow_approach_v2(frame, arrow_image, current_time, sticky_arrows, sticky_position, duration=3, arrow_start_time=0):
    """Animate arrow moving left with fade-in effect over the first 0.6 seconds, reset position on switch."""
    if arrow_image is None:
        return frame
    
    # Check if the arrow is sticky
    if any(np.array_equal(arrow_image, sticky_arrow) for sticky_arrow in sticky_arrows):
        scale = 0.7  # Sticky scale
        current_position = sticky_position  # Sticky position
        opacity_progress = 1.0  # Fully opaque for sticky arrows
    else:
        # Calculate progress for non-sticky arrows
        elapsed_time = current_time - arrow_start_time
        progress = min(1.0, elapsed_time / duration)  # Progress capped at 1.0
        
        # Define start and end scale values (moderate scaling)
        start_scale = 0.6  # Arrow appears smaller (far away)
        end_scale = 0.9    # Arrow appears at a reasonable size (closer)

        # Set start and end positions (start from 70% of the screen width, moving to the left)
        height, width, _ = frame.shape
        start_position = (int(width * 0.7), height // 2)  # Start from 70% of screen width, centered vertically
        end_position = (int(width + 100), height // 2)  # End at the far left of the screen, vertically centered

        # Interpolate scale and position based on progress
        scale = start_scale + (end_scale - start_scale) * progress
        current_position = (
            int(start_position[0] - (start_position[0] - end_position[0]) * progress),  # Move left horizontally
            start_position[1]  # Keep the same vertical position
        )

        # Fade-in effect: adjust opacity based on time (first 0.6 seconds of the arrow's animation)
        fade_in_duration = 0.6  # Fade-in period (0.6 seconds)
        if elapsed_time < fade_in_duration:  # Only fade during the first 0.6 seconds
            opacity_progress = elapsed_time / fade_in_duration  # Opacity increases from 0 to 1
        else:
            opacity_progress = 1.0  # After 0.6 seconds, the arrow is fully opaque

    # Overlay the arrow on the frame with calculated scale, position, and opacity
    frame = overlay_arrow(frame, arrow_image, current_position, scale=scale, opacity=opacity_progress)
    
    return frame

 
# Function to animate arrow moving towards the viewer with fade-in effect and reset on switch
def animate_arrow_approach_v1(frame, arrow_image, current_time, sticky_arrows, sticky_position, duration=3, arrow_start_time=0):
    """Animate arrow moving closer with fade-in effect over the first 0.6 seconds, reset position on switch."""
    if arrow_image is None:
        return frame
    
    # Check if the arrow is sticky
    if any(np.array_equal(arrow_image, sticky_arrow) for sticky_arrow in sticky_arrows):
        scale = 0.7  # Sticky scale
        current_position = sticky_position  # Sticky position
        opacity_progress = 1.0  # Fully opaque for sticky arrows
    else:
        # Calculate progress for non-sticky arrows
        elapsed_time = current_time - arrow_start_time
        progress = min(1.0, elapsed_time / duration)  # Progress capped at 1.0
        
        # Define start and end scale values (moderate scaling)
        start_scale = 0.6  # Arrow appears smaller (far away)
        end_scale = 1.0    # Arrow appears at a reasonable size (closer)

        # Set start and end positions (start from 70% of the screen height)
        height, width, _ = frame.shape
        start_position = (width // 2, int(height * 0.7))  # Start from 70% of screen height
        end_position = (width // 2, height + 130)  # End off the screen (below)

        # Interpolate scale and position based on progress
        scale = start_scale + (end_scale - start_scale) * progress
        current_position = (
            int(start_position[0] + (end_position[0] - start_position[0]) * progress),
            int(start_position[1] + (end_position[1] - start_position[1]) * progress)
        )

        # Fade-in effect: adjust opacity based on time (first 0.6 seconds of the arrow's animation)
        fade_in_duration = 0.6  # Fade-in period (0.6 seconds)
        if elapsed_time < fade_in_duration:  # Only fade during the first 0.6 seconds
            opacity_progress = elapsed_time / fade_in_duration  # Opacity increases from 0 to 1
        else:
            opacity_progress = 1.0  # After 0.6 seconds, the arrow is fully opaque

    # Overlay the arrow on the frame with calculated scale, position, and opacity
    frame = overlay_arrow(frame, arrow_image, current_position, scale=scale, opacity=opacity_progress)
    
    return frame



if __name__ == '__main__':
    try:
        logging.info('Starting the script')
        arrow_attachment_main('Staples.mov', master)
    except Exception as e:
        logging.info('Error while starting server')
        logging.info(e)
else:
    logging.info('not going in main')
