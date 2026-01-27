import subprocess
import json

def get_video_duration(video_path):
    """
    Get the duration of a video using ffprobe.
    
    Args:
        video_path: URL or file path to video
        
    Returns:
        float: Duration in seconds
    """
    command = [
        'ffprobe',
        '-v', 'error',
        '-show_entries', 'format=duration',
        '-of', 'json',
        video_path
    ]
    
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        data = json.loads(result.stdout)
        duration = float(data['format']['duration'])
        return duration
    except (subprocess.CalledProcessError, KeyError, ValueError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Failed to get duration for {video_path}: {e}")


def get_all_video_durations(video_urls):
    """
    Get durations for a list of videos.
    
    Args:
        video_urls: List of video URLs or file paths
        
    Returns:
        list: List of durations in seconds
    """
    durations = []
    for url in video_urls:
        duration = get_video_duration(url)
        durations.append(duration)
        print(f"Video: {url}")
        print(f"Duration: {duration:.2f} seconds\n")
    return durations


def create_crossfade_video(video_urls, video_durations, output_file='output.mp4', transition_duration=1, 
                          width=None, height=None, scale_mode='fit'):
    """
    Create a video with cross dissolve transitions between multiple videos.
    
    Args:
        video_urls: List of video URLs or file paths
        video_durations: List of video durations in seconds (must match video_urls length)
        output_file: Output filename
        transition_duration: Duration of cross dissolve in seconds (default: 1)
        width: Output width in pixels (None = use original)
        height: Output height in pixels (None = use original)
        scale_mode: How to scale videos - 'fit' (preserve aspect ratio, add padding), 
                   'stretch' (ignore aspect ratio), 'crop' (fill frame, crop excess)
    """
    
    if len(video_urls) != len(video_durations):
        raise ValueError("video_urls and video_durations must have the same length")
    
    if len(video_urls) < 1:
        raise ValueError("Need at least 1 video")
    
    # Build FFmpeg command
    command = ['ffmpeg']
    
    # Add all input videos
    for url in video_urls:
        command.extend(['-i', url])
    
    # Handle single video case (no transitions needed)
    if len(video_urls) == 1:
        filter_parts = []
        
        # Determine scaling filter if dimensions are specified
        if width and height:
            if scale_mode == 'fit':
                filter_parts.append(f"[0:v]scale={width}:{height}:force_original_aspect_ratio=decrease,pad={width}:{height}:(ow-iw)/2:(oh-ih)/2[v]")
            elif scale_mode == 'crop':
                filter_parts.append(f"[0:v]scale={width}:{height}:force_original_aspect_ratio=increase,crop={width}:{height}[v]")
            elif scale_mode == 'stretch':
                filter_parts.append(f"[0:v]scale={width}:{height}[v]")
        elif width:
            filter_parts.append(f"[0:v]scale={width}:-2[v]")
        elif height:
            filter_parts.append(f"[0:v]scale=-2:{height}[v]")
        else:
            # No scaling, just copy
            filter_parts.append(f"[0:v]copy[v]")
        
        filter_complex = ';'.join(filter_parts)
        command.extend([
            '-filter_complex', filter_complex,
            '-map', '[v]',
            '-pix_fmt', 'yuv420p',
            '-y',
            output_file
        ])
        
        return command
    
    # Build filter_complex
    filter_parts = []
    segment_labels = []
    
    # Determine scaling filter if dimensions are specified
    scale_filter = ""
    if width and height:
        if scale_mode == 'fit':
            # Scale to fit within dimensions, preserve aspect ratio, add black padding
            scale_filter = f"scale={width}:{height}:force_original_aspect_ratio=decrease,pad={width}:{height}:(ow-iw)/2:(oh-ih)/2"
        elif scale_mode == 'crop':
            # Scale to fill dimensions, preserve aspect ratio, crop excess
            scale_filter = f"scale={width}:{height}:force_original_aspect_ratio=increase,crop={width}:{height}"
        elif scale_mode == 'stretch':
            # Scale to exact dimensions, ignore aspect ratio
            scale_filter = f"scale={width}:{height}"
    elif width:
        # Only width specified, preserve aspect ratio
        scale_filter = f"scale={width}:-2"
    elif height:
        # Only height specified, preserve aspect ratio
        scale_filter = f"scale=-2:{height}"
    
    for i in range(len(video_urls)):
        duration = video_durations[i]
        
        if i == 0:
            # First video: all but last second
            before_transition = duration - transition_duration
            base_filter = f"[{i}:v]"
            if scale_filter:
                base_filter += f"{scale_filter},"
            
            filter_parts.append(
                f"{base_filter}trim=0:{before_transition},setpts=PTS-STARTPTS[v{i}_main]"
            )
            segment_labels.append(f"[v{i}_main]")
            
            # Last second of first video (fade out)
            base_filter = f"[{i}:v]"
            if scale_filter:
                base_filter += f"{scale_filter},"
            
            filter_parts.append(
                f"{base_filter}trim={before_transition}:{duration},setpts=PTS-STARTPTS,"
                f"format=yuva420p,fade=t=out:st=0:d={transition_duration}:alpha=1[v{i}_fade]"
            )
        
        elif i == len(video_urls) - 1:
            # Last video: first second (fade in) + rest
            base_filter = f"[{i}:v]"
            if scale_filter:
                base_filter += f"{scale_filter},"
            
            filter_parts.append(
                f"{base_filter}trim=0:{transition_duration},setpts=PTS-STARTPTS,"
                f"format=yuva420p,fade=t=in:st=0:d={transition_duration}:alpha=1[v{i}_fade]"
            )
            
            # Overlay previous fade out with current fade in
            prev_idx = i - 1
            filter_parts.append(
                f"[v{prev_idx}_fade][v{i}_fade]overlay[transition{i}]"
            )
            segment_labels.append(f"[transition{i}]")
            
            # Rest of last video
            base_filter = f"[{i}:v]"
            if scale_filter:
                base_filter += f"{scale_filter},"
            
            filter_parts.append(
                f"{base_filter}trim={transition_duration}:{duration},setpts=PTS-STARTPTS[v{i}_rest]"
            )
            segment_labels.append(f"[v{i}_rest]")
        
        else:
            # Middle videos: fade in + middle part + fade out
            before_transition = duration - transition_duration
            base_filter = f"[{i}:v]"
            if scale_filter:
                base_filter += f"{scale_filter},"
            
            # Fade in (first second)
            filter_parts.append(
                f"{base_filter}trim=0:{transition_duration},setpts=PTS-STARTPTS,"
                f"format=yuva420p,fade=t=in:st=0:d={transition_duration}:alpha=1[v{i}_fade_in]"
            )
            
            # Overlay previous fade out with current fade in
            prev_idx = i - 1
            filter_parts.append(
                f"[v{prev_idx}_fade][v{i}_fade_in]overlay[transition{i}]"
            )
            segment_labels.append(f"[transition{i}]")
            
            # Middle part (no fade)
            filter_parts.append(
                f"{base_filter}trim={transition_duration}:{before_transition},setpts=PTS-STARTPTS[v{i}_main]"
            )
            segment_labels.append(f"[v{i}_main]")
            
            # Fade out (last second)
            filter_parts.append(
                f"{base_filter}trim={before_transition}:{duration},setpts=PTS-STARTPTS,"
                f"format=yuva420p,fade=t=out:st=0:d={transition_duration}:alpha=1[v{i}_fade]"
            )
    
    # Concatenate all segments
    concat_inputs = ''.join(segment_labels)
    num_segments = len(segment_labels)
    filter_parts.append(f"{concat_inputs}concat=n={num_segments}:v=1:a=0[v]")
    
    # Join all filter parts
    filter_complex = ';'.join(filter_parts)
    
    # Add filter_complex and output options
    command.extend([
        '-filter_complex', filter_complex,
        '-map', '[v]',
        '-pix_fmt', 'yuv420p',
        '-y',  # Overwrite output file
        output_file
    ])
    
    return command


def join_vids(urls, output_path):
    success = False
    try:
        video_durations = get_all_video_durations(urls)
        # Generate command
        command = create_crossfade_video(
            video_urls=urls,
            video_durations=video_durations,
            output_file=output_path,
            transition_duration=1,
            width=608,      # Set output width
            height=1088,     # Set output height
            scale_mode='fit' # 'fit', 'crop', or 'stretch'
        )

        # Execute
        try:
            subprocess.run(command, check=True, capture_output=True, text=True)
            success = True
        except subprocess.CalledProcessError as e:
            print("Error occurred:")
            print(e.stderr)
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)
    
    return success
        


