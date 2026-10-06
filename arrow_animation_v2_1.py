from moviepy.editor import VideoFileClip, CompositeVideoClip, concatenate_videoclips
from animation_gif_helpers import processDirections
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)

KIDS_BUNNY_DIR = "newGifs/kids/bunny"
MASCOT_WIDTH_FRACTION = 0.45
MASCOT_WIDTH_FRACTION_MIN = 0.05
MASCOT_WIDTH_FRACTION_MAX = 1.0
MASCOT_Y_FROM_BOTTOM_FRACTION = 0.20
MASCOT_Y_FROM_BOTTOM_FRACTION_MIN = 0.0
MASCOT_Y_FROM_BOTTOM_FRACTION_MAX = 1.0

DIRECTION_GIF_MAP = {
    'STRAIGHT': 'v6_straight.gif',
    'LEFT': 'v6_left.gif',
    'SLIGHT_LEFT': 'v6_left.gif',
    'RIGHT': 'bunny-right.gif',
    'SLIGHT_RIGHT': 'bunny-right.gif',
}


def get_bunny_gif_path(direction: str) -> str:
    gif_name = DIRECTION_GIF_MAP.get(direction, DIRECTION_GIF_MAP['STRAIGHT'])
    return f"{KIDS_BUNNY_DIR}/{gif_name}"


def resolve_mascot_width_fraction(mascot_width_fraction=None):
    if mascot_width_fraction is None:
        return MASCOT_WIDTH_FRACTION
    return max(
        MASCOT_WIDTH_FRACTION_MIN,
        min(MASCOT_WIDTH_FRACTION_MAX, float(mascot_width_fraction)),
    )


def resolve_mascot_y_from_bottom_fraction(mascot_y_from_bottom_fraction=None):
    if mascot_y_from_bottom_fraction is None:
        return MASCOT_Y_FROM_BOTTOM_FRACTION
    return max(
        MASCOT_Y_FROM_BOTTOM_FRACTION_MIN,
        min(MASCOT_Y_FROM_BOTTOM_FRACTION_MAX, float(mascot_y_from_bottom_fraction)),
    )


def build_bunny_overlay(
    start_time,
    end_time,
    direction,
    base_vid_width,
    base_vid_height,
    base_vid_duration,
    mascot_width_fraction=MASCOT_WIDTH_FRACTION,
    mascot_y_from_bottom_fraction=MASCOT_Y_FROM_BOTTOM_FRACTION,
):
    """
    Fixed kids bunny GIF for a direction segment.
    No position motion; bottom of GIF sits at y_from_bottom of video height from bottom.
    """
    target_duration = end_time - start_time
    if target_duration <= 0:
        return None

    gif_path = get_bunny_gif_path(direction)
    bunny = VideoFileClip(gif_path, has_mask=True)

    width_fraction = resolve_mascot_width_fraction(mascot_width_fraction)
    target_width = max(1, int(base_vid_width * width_fraction))
    scale = target_width / bunny.w
    target_height = max(1, int(bunny.h * scale))
    bunny = bunny.resize((target_width, target_height))

    gif_duration = bunny.duration
    if gif_duration <= 0:
        bunny.close()
        return None

    num_loops = int(np.ceil(target_duration / gif_duration))
    bunny = concatenate_videoclips([bunny] * num_loops)
    bunny = bunny.subclip(0, min(target_duration, bunny.duration))

    y_from_bottom = resolve_mascot_y_from_bottom_fraction(mascot_y_from_bottom_fraction)
    y_pos = int(base_vid_height * (1 - y_from_bottom) - bunny.h)
    y_pos = max(0, y_pos)
    bunny = bunny.set_position(("center", y_pos))
    bunny = bunny.set_start(start_time).set_end(min(end_time, base_vid_duration))
    return bunny


def animate_arrow_gifs_v2_1(
    route_id,
    vid_name,
    source_caption,
    hex_color=None,
    mascot_width_fraction=None,
    mascot_y_from_bottom_fraction=None,
):
    """
    Kids v2.1: overlay bunny GIFs only (no arrows), fixed position.
    Same as v2 but Y from bottom may be up to 1.0.
    hex_color is accepted for API compatibility but ignored.
    """
    try:
        output_name = f"{vid_name}"
        input_dir = 'blurred'
        output_dir = 'final'

        resolved_width = resolve_mascot_width_fraction(mascot_width_fraction)
        resolved_y_from_bottom = resolve_mascot_y_from_bottom_fraction(
            mascot_y_from_bottom_fraction
        )

        captions = processDirections(source_caption)

        base_video = VideoFileClip(f"{input_dir}/{vid_name}")
        base_vid_width, base_vid_height = base_video.size
        base_vid_duration = base_video.duration

        mascot_clips = []

        for x in captions:
            start_time = x.get("startTime", 0)
            end_time = x.get("endTime", 0)
            show_animation = x.get('showAnimations', True)
            if show_animation == False:
                continue

            direction = x.get('directionIcon', 'STRAIGHT')
            if end_time - start_time == 0:
                continue

            bunny_clip = build_bunny_overlay(
                start_time,
                end_time,
                direction,
                base_vid_width,
                base_vid_height,
                base_vid_duration,
                mascot_width_fraction=resolved_width,
                mascot_y_from_bottom_fraction=resolved_y_from_bottom,
            )
            if bunny_clip is not None:
                mascot_clips.append(bunny_clip)

        all_clips = [base_video] + mascot_clips
        final = CompositeVideoClip(all_clips)

        final.write_videofile(
            f"{output_dir}/{output_name}",
            codec="libx264",
            audio_codec="aac",
            temp_audiofile="temp-audio.m4a",
            remove_temp=True,
        )
    except Exception as e:
        print(e)
        print("Error inside animation v2.1 fn")
        try:
            update_route_field(route_id, 'processStatus', 'ARROW_ATTACHMENT_ERROR')
        except Exception:
            logging.info('Error while updating DB')
