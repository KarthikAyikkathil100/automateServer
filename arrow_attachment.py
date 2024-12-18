import cv2
import numpy as np
import os
import logging
from copy import copy
from helpers import  update_route_field
logging.basicConfig(level=logging.INFO)

master  = [
  {
    "direction": "straight",
    "start": 0,
    "end": 18,
    "message": "Go straight"
  },
  {
    "start": 18,
    "end": 20,
    "direction": "left",
    "message": "Turn left",
    "sticky": True
  },
  {
    "start": 20,
    "end": 24,
    "direction": "left",
    "message": "Turn left"
  },
  {
    "start": 24,
    "end": 27,
    "direction": "slight right",
    "message": "Turn slight right"
  },
  {
    "direction": "straight",
    "message": "Go straight",
    "start": 27,
    "end": 28
  }
]

# master = [
#   {
#     "direction": "straight",
#     "start": 0,
#     "end": 14,
#     "message": "Go straight"
#   },
#   {
#     "start": 14,
#     "end": 16,
#     "direction": "left",
#     "message": "Turn left",
#     "sticky": True
#   },
#   {
#     "start": 16,
#     "end": 21,
#     "direction": "left",
#     "message": "Turn left"
#   },
#   {
#     "direction": "straight",
#     "start": 21,
#     "end": 33,
#     "message": "Go straight"
#   },
#   {
#     "start": 33,
#     "end": 35,
#     "direction": "left",
#     "message": "Turn left",
#     "sticky": True
#   },
#   {
#     "start": 35,
#     "end": 40,
#     "direction": "left",
#     "message": "Turn left"
#   },
#   {
#     "direction": "straight",
#     "start": 40,
#     "end": 40,
#     "message": "Go straight"
#   },
#   {
#     "start": 40,
#     "end": 40,
#     "direction": "left",
#     "message": "Turn left",
#     "sticky": True
#   },
#   {
#     "start": 40,
#     "end": 45,
#     "direction": "left",
#     "message": "Turn left"
#   },
#   {
#     "direction": "straight",
#     "start": 45,
#     "end": 65,
#     "message": "Go straight"
#   },
#   {
#     "start": 65,
#     "end": 67,
#     "direction": "slight right",
#     "message": "Turn slight right",
#     "sticky": True
#   },
#   {
#     "start": 67,
#     "end": 70,
#     "direction": "slight right",
#     "message": "Turn slight right"
#   },
#   {
#     "direction": "straight",
#     "start": 70,
#     "end": 107,
#     "message": "Go straight"
#   },
#   {
#     "start": 107,
#     "end": 109,
#     "direction": "right",
#     "message": "Turn right",
#     "sticky": True
#   },
#   {
#     "start": 109,
#     "end": 113,
#     "direction": "right",
#     "message": "Turn right"
#   },
#   {
#     "direction": "straight",
#     "start": 113,
#     "end": 116,
#     "message": "Go straight"
#   },
#   {
#     "start": 116,
#     "end": 118,
#     "direction": "left",
#     "message": "Turn left",
#     "sticky": True
#   },
#   {
#     "start": 118,
#     "end": 123,
#     "direction": "left",
#     "message": "Turn left"
#   },
#   {
#     "direction": "straight",
#     "start": 123,
#     "end": 124,
#     "message": "Go straight"
#   },
#   {
#     "start": 124,
#     "end": 126,
#     "direction": "right",
#     "message": "Turn right",
#     "sticky": True
#   },
#   {
#     "start": 126,
#     "end": 131,
#     "direction": "right",
#     "message": "Turn right"
#   },
#   {
#     "direction": "straight",
#     "start": 131,
#     "end": 149,
#     "message": "Go straight"
#   },
#   {
#     "start": 149,
#     "end": 151,
#     "direction": "left",
#     "message": "Turn left",
#     "sticky": True
#   },
#   {
#     "start": 151,
#     "end": 154,
#     "direction": "left",
#     "message": "Turn left"
#   },
#   {
#     "direction": "straight",
#     "start": 154,
#     "end": 154,
#     "message": "Go straight"
#   },
#   {
#     "start": 154,
#     "end": 155,
#     "direction": "left",
#     "message": "Turn left",
#     "sticky": True
#   },
#   {
#     "start": 155,
#     "end": 160,
#     "direction": "left",
#     "message": "Turn left"
#   },
#   {
#     "direction": "straight",
#     "start": 160,
#     "end": 178,
#     "message": "Go straight"
#   },
#   {
#     "start": 178,
#     "end": 180,
#     "direction": "left",
#     "message": "Turn left",
#     "sticky": True
#   },
#   {
#     "start": 180,
#     "end": 185,
#     "direction": "left",
#     "message": "Turn left"
#   },
#   {
#     "start": 185,
#     "end": 186,
#     "direction": "left",
#     "message": "Turn left"
#   },
#   {
#     "direction": "straight",
#     "start": 186,
#     "end": 208,
#     "message": "Go straight"
#   },
#   {
#     "start": 208,
#     "end": 210,
#     "direction": "right",
#     "message": "Turn right",
#     "sticky": True
#   },
#   {
#     "start": 210,
#     "end": 214,
#     "direction": "right",
#     "message": "Turn right"
#   },
#   {
#     "direction": "straight",
#     "start": 214,
#     "end": 214,
#     "message": "Go straight"
#   },
#   {
#     "start": 214,
#     "end": 213,
#     "direction": "right",
#     "message": "Turn right",
#     "sticky": True
#   },
#   {
#     "start": 213,
#     "end": 217,
#     "direction": "right",
#     "message": "Turn right"
#   },
#   {
#     "direction": "straight",
#     "start": 217,
#     "end": 217,
#     "message": "Go straight"
#   },
#   {
#     "start": 217,
#     "end": 216,
#     "direction": "left",
#     "message": "Turn left",
#     "sticky": True
#   },
#   {
#     "start": 216,
#     "end": 221,
#     "direction": "left",
#     "message": "Turn left"
#   },
#   {
#     "start": 221,
#     "end": 223,
#     "direction": "left",
#     "message": "Turn left"
#   },
#   {
#     "direction": "straight",
#     "start": 223,
#     "end": 223,
#     "message": "Go straight"
#   },
#   {
#     "start": 223,
#     "end": 223,
#     "direction": "slight right",
#     "message": "Turn slight right",
#     "sticky": True
#   },
#   {
#     "start": 223,
#     "end": 226,
#     "direction": "slight right",
#     "message": "Turn slight right"
#   },
#   {
#     "direction": "straight",
#     "message": "Go straight",
#     "start": 226,
#     "end": 240
#   }
# ]

all_turns = ['right', 'slight right', 'left', 'slight left']

def checkIfTurn(curr_turn_name):
    return any( direction_name == curr_turn_name for direction_name in all_turns)


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
                    if (index == 0 and next_p != None and checkIfTurn(next_p.get('direction')) == True) or (index > 0 and index != total_len-1):
                        temp = copy(curr_p)
                        temp['end'] = max(curr_p.get('start'), (next_p.get('start') - 2))
                        processedDirections.append(temp)
                    else:
                        processedDirections.append(curr_p)
                elif checkIfTurn(curr_p.get('direction')) == True:
                    if (index == 0):
                        processedDirections.append(curr_p)
                    elif (index == total_len-1):
                        if checkIfTurn(prev_p.get('direction')) == True:
                            processedDirections.append(curr_p)
                        else:
                            # prev was straight
                            sticky_temp = copy(curr_p)
                            sticky_temp['sticky'] = True
                            sticky_temp['start'] = (processedDirections[-1]).get('end')
                            sticky_temp['end'] = curr_p.get('start')
                            # Push the sticky arrow
                            processedDirections.append(sticky_temp)

                            temp = copy(curr_p)
                            processedDirections.append(temp)
                    elif (index > 0 and index < total_len-1): # somewhere in between
                        if (prev_p != None and checkIfTurn(prev_p.get('direction')) == True):
                            processedDirections.append(curr_p)
                        else:
                            sticky_temp = copy(curr_p)
                            sticky_temp['start'] = (processedDirections[-1]).get('end')
                            sticky_temp['sticky'] = True
                            sticky_temp['end'] = curr_p.get('start')
                            # Push the sticky arrow
                            processedDirections.append(sticky_temp)
                            
                            temp = copy(curr_p)
                            processedDirections.append(temp)        
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

def arrow_attachment_main(file_name, master):
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
            arrows.append((el['start'], el['end'], icon, has_sticky))
        
        
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

        # Add a flag to track if the arrow image changed
        arrow_changed = False
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
            for start_time, end_time, arrow_image, sticky in arrows:
                if start_time <= current_time < end_time:
                    new_arrow = arrow_image
                    if sticky == True:
                        is_sticky = True
                    break
            # If the arrow changes, reset the animation
            if new_arrow is not None:
                if current_arrow is None or not np.array_equal(current_arrow, new_arrow):
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

            # Reset animation cycle if current animation completes
            if (current_time - arrow_start_time) >= duration:
                arrow_start_time = current_time  # Reset the animation cycle for continuous movement

            # Animate the current arrow (reset if changed, continue if not)
            frame = animate_arrow_approach(frame, current_arrow, current_time, sticky_arrows, sticky_position, duration, arrow_start_time, is_sticky)

            # Write the frame to the output video
            out.write(frame)
            
            
            # Display the video frame (optional)
            # cv2.imshow('Video with Arrows', frame)
            
            # # Break the loop on 'q' key press
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break
            
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


# Assuming other variables (like current_time, sticky_arrows, etc.) are defined elsewhere in your code

def animate_arrow_approach(frame, arrow_image, current_time, sticky_arrows, sticky_position, duration=2, arrow_start_time=0, is_sticky = False):
    """Animate arrow moving left with fade-in effect over the first 0.6 seconds, reset position on switch."""
    if arrow_image is None:
        return frame
    
    # Check if the arrow is sticky
    if is_sticky == True:
        scale = 0.4  # Sticky scale
        current_position = sticky_position  # Sticky position
        opacity_progress = 1.0  # Fully opaque for sticky arrows
    else:
        # Define start and end scale values (moderate scaling)
        start_scale = 0.2  # Arrow appears smaller (far away)
        end_scale = 0.6   # Arrow appears at a reasonable size (closer)
        # Calculate progress for non-sticky arrows
        elapsed_time = current_time - arrow_start_time
        progress = min(1.0, elapsed_time / duration)  # Progress capped at 1.0
        
        # Define start and end positions (start from 70% of the screen width, moving to the left)
        height, width, _ = frame.shape
        if any(np.array_equal(arrow_image, lft_arrow) for lft_arrow in left_turns):
            # Left turns
            start_position = (int(width * 0.3), height // 2)  
            end_position = (int(width + 300), height // 2)  
        elif any(np.array_equal(arrow_image, rht_arrow) for  rht_arrow in right_turns):
            # Right turns
            start_position = (int(width * 1), height // 2)  
            end_position = (-300, height // 2)  
        else:
            # Straight way
            start_position = (width // 2, int(height * 0.6)) 
            end_position = (width // 2, height + 130)  

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
        arrow_attachment_main('Staples_bl.mov', master)
    except Exception as e:
        logging.info('Error while starting server')
        logging.info(e)
else:
    logging.info('not going in main')
