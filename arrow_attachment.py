import cv2
import numpy as np
import os
import logging
from helpers import  update_route_field
logging.basicConfig(level=logging.INFO)

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

        # Define the codec and create VideoWriter object to save the output video
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(f'final/{file_name}', fourcc, fps, (frame_width, frame_height))

        arrows = []
        for el in master:
            icon = get_direction_icon(el['direction'])
            arrows.append((el['start'], el['end'], icon))
        
        
        # Define sticky arrows
        sticky_arrows = [arrow_left, arrow_right]  # Add your sticky arrow images here
        sticky_position = (frame_width // 2, int(frame_height * 0.7))  # Fixed position for sticky arrows

        # Process the video frame by frame
        frame_number = 0
        current_arrow = None
        arrow_start_time = 0  # Tracks when the current arrow starts
        duration = 3  # Duration for each arrow approach effect (3 seconds)

        # Add a flag to track if the arrow image changed
        arrow_changed = False
        while cap.isOpened():
            # logging.info(f'frame process => {frame_number}')
            ret, frame = cap.read()
            if not ret:
                break
            # Get the current time in seconds
            current_time = frame_number / fps

            
            # Determine which arrow to display based on the time intervals
            new_arrow = None
            for start_time, end_time, arrow_image in arrows:
                if start_time <= current_time < end_time:
                    new_arrow = arrow_image
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
            frame = animate_arrow_approach(frame, current_arrow, current_time, sticky_arrows, sticky_position, duration, arrow_start_time)

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
        cv2.destroyAllWindows()
    except Exception as e:
        logging.info('Error in Arrow attachment')
        logging.info(e)
        try:
            update_route_field(route_id, 'processStatus', 'ARROW_ATTACHMENT_ERROR')
        except Exception as e:
            logging.info('Error while updating DB')
        

# Function to overlay an image on the video frame
def overlay_arrow(frame, arrow_image, position, scale=1.0, opacity=1.0):
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
    if center_x < 0:
        center_x = 0
    if center_y < 0:
        center_y = 0
    if center_x + new_arrow_w > width:
        new_arrow_w = width - center_x
    if center_y + new_arrow_h > height:
        new_arrow_h = height - center_y

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



# Function to animate arrow moving towards the viewer with fade-in effect and reset on switch
def animate_arrow_approach(frame, arrow_image, current_time, sticky_arrows, sticky_position, duration=3, arrow_start_time=0):
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



# main('mia_3_hd.mp4')