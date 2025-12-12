from operator import is_
from moviepy.editor import VideoFileClip, CompositeVideoClip
from animation_gif_helpers import processDirections, all_turns, preProcess
from PIL import Image
from moviepy.editor import concatenate_videoclips
import numpy as np
from moviepy.video.fx.loop import loop

# Each animation/gif duration is 5 sec
animation_duration = 12
turn_animation_duration = 14
start_height = 20
end_height = 700
straight_arrow_end_height = 400
gif_width_scale_factor = 1.1
second_animation_gap = 5
short_anim_max_scale = 0.5
pure_turns_directions = [x for x in all_turns if x != 'END']


def get_gif_name(direction: str, route_id, hexColor = None):
    direction_map = {
        'STRAIGHT': 'straight-25slow.gif',
        'LEFT': 'left-25speed.gif',
        'RIGHT': 'right-25speed.gif',
        'SLIGHT_LEFT': 'left-25speed.gif',
        'SLIGHT_RIGHT': 'right-25speed.gif',
    }
    res = direction_map[direction] if direction_map[direction] != None else direction_map['STRAIGHT']
    if hexColor != None:
        res = f"{route_id}-{hexColor}-{res}"
    return res


def get_moving_postion(start_time, end_time, vid_height, speed_factor=0.48):
    """
    speed_factor < 1 → slower movement
    speed_factor > 1 → faster movement
    """
    duration = end_time - start_time
    def moving_position(t):
        progress = (t / duration) * speed_factor
        progress = min(progress, 1)  # cap at  
        y = vid_height * (0.46 + 0.54 * progress)
        return ("center", y)
    return moving_position


def get_constant_speed_position(start_time, end_time, vid_height):
    total_time = end_time - start_time
    total_distance = vid_height * (0.95 - 0.55)  # from 55% → 95%
    speed = total_distance / total_time          # pixels per second

    def moving_position(t):
        elapsed = t
        y = vid_height * 0.55 + speed * elapsed
        return ("center", y)

    return moving_position


def get_moving_position_dynamic_old(start_time, end_time, vid_width, vid_height, gif_width, gif_height, direction, start_frac=0.5, speed_factor=0.44):
    duration = end_time - start_time

    # if direction == 'STRAIGHT':
    #     return get_constant_speed_position(start_time, end_time, vid_height)

    def moving_position(t):
        progress = (t / duration)
    
        if direction not in pure_turns_directions:
            progress = progress * speed_factor
        progress = min(progress, 1)

        if direction not in pure_turns_directions:
            if duration < animation_duration:
                y = vid_height * (0.55 + 0.03 * progress)
            else:
                y = vid_height * (0.55 + 0.50 * progress)
            return ("center", y)

        y = vid_height * (start_frac + (0.8 - start_frac) * progress)

        if direction == 'STRAIGHT':
            current_height = start_height + (straight_arrow_end_height - start_height) * progress
        else:
            current_height = start_height + (end_height - start_height) * progress
            
        current_width = int(gif_width * (current_height / gif_height) * gif_width_scale_factor)  # same as scale factor

        # X movement (center path moving right)
        if (progress < 0.4 and duration >= animation_duration):
            x_center = vid_width / 2
        else:
            # curve_progress = (progress - 0.4) / 0.6
            curve_progress = max(0, min(1, (progress - 0.4) / 0.6))

            # curve_progress *= (0.55 * 2)
            # x_center = (vid_width / 2) + curve_progress * (vid_width / 2 + current_width/2) 

            if direction in ['LEFT', 'SLIGHT_LEFT']:
                x_center = (vid_width / 2) + curve_progress * (vid_width / 2 + current_width/2)
            elif direction in ['RIGHT', 'SLIGHT_RIGHT']:
                x_center = (vid_width / 2) - curve_progress * (vid_width / 2 + current_width/2)

        # Convert center to top-left for MoviePy
        x_top_left = x_center - current_width / 2

        return (x_top_left, vid_height/2)
    return moving_position

def get_moving_position_dynamic(start_time, end_time, vid_width, vid_height, gif_width, gif_height, direction, start_frac=0.5, speed_factor=0.44):
    duration = end_time - start_time

    def moving_position(t):
        progress = (t / duration)
    
        if direction in ['STRAIGHT',]:
            progress = progress * speed_factor
        progress = min(progress, 1)

        if direction in ['STRAIGHT',]:
            if duration < animation_duration:
                # y = vid_height * (0.55 + 0.03 * progress)
                y = vid_height * (0.55 + (0.50 * (duration / animation_duration)) * progress)
            else:
                y = vid_height * (0.55 + 0.50 * progress)
            return ("center", y)

        y = vid_height * (start_frac + (0.8 - start_frac) * progress)

        # if direction == 'STRAIGHT':
        #     current_height = start_height + (straight_arrow_end_height - start_height) * progress
        # else:

        # Apply the same scaling logic as in scale_frame_wrapper
        if duration < animation_duration:
            scale_ratio = duration / animation_duration
            height_change = (end_height - start_height) * scale_ratio
            current_height = start_height + height_change * progress
            effective_width_factor = 1 + (gif_width_scale_factor - 1) * scale_ratio
        else:
            current_height = start_height + (end_height - start_height) * progress
            effective_width_factor = gif_width_scale_factor
            
        current_width = int(gif_width * (current_height / gif_height) * effective_width_factor)

        # X movement (center path moving right)
        if (progress < 0.4 and duration >= animation_duration):
            x_center = vid_width / 2
        else:
            curve_progress = max(0, min(1, (progress - 0.4) / 0.6))

            if direction in ['LEFT', 'SLIGHT_LEFT']:
                x_center = (vid_width / 2) + curve_progress * (vid_width / 2 + current_width/2)
            elif direction in ['RIGHT', 'SLIGHT_RIGHT']:
                x_center = (vid_width / 2) - curve_progress * (vid_width / 2 + current_width/2)

        # Convert center to top-left for MoviePy
        x_top_left = x_center - current_width / 2

        return (x_top_left, vid_height/2)
    return moving_position


def fix_white_halo(frame):
    rgb = frame[..., :3].astype(float)
    # detect very bright pixels
    brightness = np.mean(rgb, axis=2, keepdims=True)
    # reduce brightness in near-white areas, preserving dark shadows
    # rgb = np.where(brightness > 220, rgb * 0.3, rgb)
    rgb = np.where(brightness > 200, rgb * 0.01, rgb)

    return rgb.astype(np.uint8)

def ensure_rgb_frame_with_time(get_frame, t):
    """Ensure frame is always RGB with time parameter"""
    frame = get_frame(t)
    if len(frame.shape) == 3 and frame.shape[-1] == 4:  # RGBA
        return frame[:, :, :3]
    return frame

def scale_frame_wrapper(duration, direction, width_factor=gif_width_scale_factor):
    """
    width_factor > 1 → increase width along with height
    If duration < animation_duration, scale less aggressively
    """
    def scale_frame(get_frame, t):
        progress = max(0, min(1, t / duration))
        
        # Reduce scaling when duration is shorter
        if duration < animation_duration:
            scale_ratio = duration / animation_duration
            height_change = (end_height - start_height) * scale_ratio
            current_height = start_height + height_change * progress
            effective_width_factor = 1 + (width_factor - 1) * scale_ratio
        else:
            current_height = start_height + (end_height - start_height) * progress
            effective_width_factor = width_factor

        frame = get_frame(t)
        rgb = frame[:, :, :3]

        img = Image.fromarray(rgb)
        w, h = img.size
        new_h = int(current_height)
        new_w = int(new_h * (w / h) * effective_width_factor)
        resized_rgb = img.resize((new_w, new_h), Image.LANCZOS)

        return np.array(resized_rgb)
    
    return scale_frame

def scale_mask_wrapper(duration, direction, width_factor=gif_width_scale_factor):
    """
    Resize the alpha mask (1 channel) over time.
    Must match the RGB scaling exactly!
    """
    def scale_mask(get_frame, t):
        progress = max(0, min(1, t / duration))
        
        # Reduce scaling when duration is shorter (same as frame scaling)
        if duration < animation_duration:
            scale_ratio = duration / animation_duration
            height_change = (end_height - start_height) * scale_ratio
            current_height = start_height + height_change * progress
            effective_width_factor = 1 + (width_factor - 1) * scale_ratio
        else:
            current_height = start_height + (end_height - start_height) * progress
            effective_width_factor = width_factor

        frame = get_frame(t)
        img = Image.fromarray(frame)
        w, h = img.size
        new_h = int(current_height)
        new_w = int(new_h * (w / h) * effective_width_factor)
        resized = img.resize((new_w, new_h), Image.BILINEAR)

        return np.array(resized)

    return scale_mask



# get_anmimation_duration_chunks function will return something like -- 
"""
    [
        [1, 2],
        [3, 4]
    ]
"""
def get_anmimation_duration_chunks(start_duration, end_duration, gif_duration = turn_animation_duration):
    # print(f"------------- start = {start_duration}  ----  end = {end_duration}")
    chunks = []
    if end_duration-start_duration <= gif_duration:
        chunks.append([start_duration, end_duration])
    else:
        start_instance = start_duration
        end_instance = start_instance + gif_duration

        while end_instance <= end_duration:
            chunks.append([start_instance, end_instance])
            start_instance += gif_duration

            end_instance += gif_duration
        
        # print("At end -- ", end_instance)
        if end_instance != end_duration:
            chunks.append([start_instance, end_duration])
    
    return chunks


def get_anmimation_duration_chunks_v2(start_duration, end_duration, is_last, gif_duration = animation_duration):
    # print(f"------------- start = {start_duration}  ----  end = {end_duration}")
    chunks = []
    if end_duration-start_duration <= gif_duration:
        if end_duration-start_duration <= 5:
            chunk_intermediate = start_duration + int(gif_duration/2)
            if chunk_intermediate < end_duration:
                chunks.append([start_duration, chunk_intermediate])
                chunks.append([max(start_duration, chunk_intermediate-2), end_duration])
            else:
                chunks.append([start_duration, end_duration])
        else:
            chunks.append([start_duration, end_duration])
    else:
        start_instance = start_duration
        end_instance = start_instance + gif_duration

        is_first_iter = True
        while end_instance <= end_duration:
            if is_first_iter == True:
                # First iteration
                is_first_iter = False
                chunks.append([start_instance, end_instance])
            else:
                end_instance = end_instance - second_animation_gap
                chunks.append([end_instance, min(end_instance + gif_duration, end_duration)])
                end_instance = end_instance + gif_duration

    if is_last == True:
        last = chunks[len(chunks)-1]
        last_start = last[0]
        last_end = last[1]
        if last_end-last_start != animation_duration:
            chunks[len(chunks)-1] = [last_start, last_end+animation_duration]
            
    
    return chunks



def animate_arrow_gifs(route_id, vid_name, source_caption, hex_color = None):
    try:
        gif_dir = "newGifs" if hex_color == None else "colored_gifs"

        output_name = f"{vid_name}"

        input_dir = 'blurred'
        output_dir = 'final'

        captions = processDirections(source_caption)
        

        base_video = VideoFileClip(f"{input_dir}/{vid_name}")
        base_vid_width, base_vid_height = base_video.size
        base_vid_duration = base_video.duration

        all_gifs = []

        # Loop over the captions
        for i, x in enumerate(captions):
            start_time = x.get("startTime", 0)
            end_time = x.get("endTime", 0)
            direction = x.get('directionIcon', 'STRAIGHT')

            if end_time-start_time == 0:
                continue

            if direction == "STRAIGHT":
                animation_chunks = get_anmimation_duration_chunks_v2(start_time, end_time, i == len(captions)-1)
            else:
                animation_chunks = get_anmimation_duration_chunks(start_time, end_time)


            for chunk in animation_chunks:
                chunk_start, chunk_end = chunk
                
                if chunk_end-chunk_start == 0:
                    continue
                
                gif_name = get_gif_name(direction, route_id, hex_color)
                gif_path = f"{gif_dir}/{gif_name}"
                gif_instance = VideoFileClip(gif_path, has_mask=True)
                # gif_instance = gif_instance.fl(ensure_rgb_frame_with_time)
                gif_instance = gif_instance.fl_image(fix_white_halo)

                # Get the actual duration of the GIF
                gif_duration = gif_instance.duration
                target_duration = chunk_end - chunk_start  # ← FIX: Use chunk duration, not total duration

                # Calculate number of loops needed
                num_loops = int(np.ceil(target_duration / gif_duration))

                # Create a looped version by concatenating
                gif_instance = concatenate_videoclips([gif_instance] * num_loops)

                # Trim to exact duration needed
                gif_instance = gif_instance.subclip(0, min(target_duration, gif_instance.duration))

                # NOW apply scaling - USE CHUNK DURATION HERE
                scaled_gif = gif_instance.fl(scale_frame_wrapper(chunk_end - chunk_start, direction))  # ← FIX
                scaled_mask = gif_instance.mask.fl(scale_mask_wrapper(chunk_end - chunk_start, direction))  # ← FIX
                scaled_gif.mask = scaled_mask

                gif_instance = scaled_gif

                gif_instance_width, gif_instance_height = gif_instance.size

                gif_instance = gif_instance.set_position(get_moving_position_dynamic(chunk_start, chunk_end, base_vid_width, base_vid_height, gif_instance_width, gif_instance_height, direction))

                gif_instance = gif_instance.set_start(chunk_start).set_end(min(chunk_end, base_vid_duration))

                all_gifs.append(gif_instance)
        # ------------------------
        # Combine everything
        # ------------------------
        all_clips = [base_video]
        for x in all_gifs:
            all_clips.append(x)
        final = CompositeVideoClip(all_clips)

        # Export
        final.write_videofile(
            f"{output_dir}/{output_name}",
            codec="libx264",
            audio_codec="aac",
            temp_audiofile="temp-audio.m4a",
            remove_temp=True
        )
    except Exception as e:
        print(e)
        try:
            update_route_field(route_id, 'processStatus', 'ARROW_ATTACHMENT_ERROR')
        except Exception as e:
            logging.info('Error while updating DB')
