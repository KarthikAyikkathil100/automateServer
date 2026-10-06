from moviepy.editor import VideoFileClip, CompositeVideoClip, concatenate_videoclips
from animation_gif_helpers import processDirections
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)

KIDS_BUNNY_DIR = "newGifs/kids/bunny"
KIDS_DUCK_DIR = "newGifs/kids/duck"
MASCOT_WIDTH_FRACTION = 0.45
MASCOT_WIDTH_FRACTION_MIN = 0.05
MASCOT_WIDTH_FRACTION_MAX = 1.0
MASCOT_Y_FROM_BOTTOM_FRACTION = 0.20
MASCOT_Y_FROM_BOTTOM_FRACTION_MIN = 0.0
MASCOT_Y_FROM_BOTTOM_FRACTION_MAX = 0.5

TURN_DIRECTIONS = {'LEFT', 'RIGHT', 'SLIGHT_LEFT', 'SLIGHT_RIGHT'}

MASCOT_GIF_MAP = {
    'bunny': {
        'dir': KIDS_BUNNY_DIR,
        'STRAIGHT': 'bunny_loop_full.gif',
        'LEFT': 'bunny-left.gif',
        'SLIGHT_LEFT': 'bunny-left.gif',
        'RIGHT': 'bunny-right.gif',
        'SLIGHT_RIGHT': 'bunny-right.gif',
    },
    'duck': {
        'dir': KIDS_DUCK_DIR,
        'STRAIGHT': 'bird-straight.gif',
        'LEFT': 'ird-left.gif',
        'SLIGHT_LEFT': 'ird-left.gif',
        'RIGHT': 'bird-right.gif',
        'SLIGHT_RIGHT': 'bird-right.gif',
    },
}


def is_turn_direction(direction: str) -> bool:
    return direction in TURN_DIRECTIONS


def flip_mascot(active_mascot: str) -> str:
    return 'duck' if active_mascot == 'bunny' else 'bunny'


def get_mascot_gif_path(mascot: str, direction: str) -> str:
    assets = MASCOT_GIF_MAP.get(mascot, MASCOT_GIF_MAP['bunny'])
    gif_name = assets.get(direction, assets['STRAIGHT'])
    return f"{assets['dir']}/{gif_name}"


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


def build_mascot_overlay(
    start_time,
    end_time,
    mascot,
    direction,
    base_vid_width,
    base_vid_height,
    base_vid_duration,
    mascot_width_fraction=MASCOT_WIDTH_FRACTION,
    mascot_y_from_bottom_fraction=MASCOT_Y_FROM_BOTTOM_FRACTION,
):
    """
    Fixed kids mascot GIF for a direction segment.
    No position motion; bottom of GIF sits at y_from_bottom of video height from bottom.
    """
    target_duration = end_time - start_time
    if target_duration <= 0:
        return None

    gif_path = get_mascot_gif_path(mascot, direction)
    clip = VideoFileClip(gif_path, has_mask=True)

    width_fraction = resolve_mascot_width_fraction(mascot_width_fraction)
    target_width = max(1, int(base_vid_width * width_fraction))
    scale = target_width / clip.w
    target_height = max(1, int(clip.h * scale))
    clip = clip.resize((target_width, target_height))

    gif_duration = clip.duration
    if gif_duration <= 0:
        clip.close()
        return None

    num_loops = int(np.ceil(target_duration / gif_duration))
    clip = concatenate_videoclips([clip] * num_loops)
    clip = clip.subclip(0, min(target_duration, clip.duration))

    y_from_bottom = resolve_mascot_y_from_bottom_fraction(mascot_y_from_bottom_fraction)
    y_pos = int(base_vid_height * (1 - y_from_bottom) - clip.h)
    y_pos = max(0, y_pos)
    clip = clip.set_position(("center", y_pos))
    clip = clip.set_start(start_time).set_end(min(end_time, base_vid_duration))
    return clip


def animate_arrow_gifs_v3(
    route_id,
    vid_name,
    source_caption,
    hex_color=None,
    mascot_width_fraction=None,
    mascot_y_from_bottom_fraction=None,
    bunny_width_fraction=None,
    bunny_y_from_bottom_fraction=None,
    duck_width_fraction=None,
    duck_y_from_bottom_fraction=None,
):
    """
    Kids v3: bunny starts; active mascot turns; after each turn switch bunny <-> duck.
    hex_color is accepted for API compatibility but ignored.

    Per-mascot size/Y knobs take precedence over shared mascot_* fallbacks.
    """
    try:
        output_name = f"{vid_name}"
        input_dir = 'blurred'
        output_dir = 'final'

        shared_width = resolve_mascot_width_fraction(mascot_width_fraction)
        shared_y = resolve_mascot_y_from_bottom_fraction(mascot_y_from_bottom_fraction)

        bunny_width = resolve_mascot_width_fraction(
            bunny_width_fraction if bunny_width_fraction is not None else shared_width
        )
        bunny_y = resolve_mascot_y_from_bottom_fraction(
            bunny_y_from_bottom_fraction if bunny_y_from_bottom_fraction is not None else shared_y
        )
        duck_width = resolve_mascot_width_fraction(
            duck_width_fraction if duck_width_fraction is not None else shared_width
        )
        duck_y = resolve_mascot_y_from_bottom_fraction(
            duck_y_from_bottom_fraction if duck_y_from_bottom_fraction is not None else shared_y
        )

        size_by_mascot = {
            'bunny': (bunny_width, bunny_y),
            'duck': (duck_width, duck_y),
        }

        captions = processDirections(source_caption)

        base_video = VideoFileClip(f"{input_dir}/{vid_name}")
        base_vid_width, base_vid_height = base_video.size
        base_vid_duration = base_video.duration

        mascot_clips = []
        active_mascot = 'bunny'

        for x in captions:
            start_time = x.get("startTime", 0)
            end_time = x.get("endTime", 0)
            show_animation = x.get('showAnimations', True)
            if show_animation == False:
                continue

            direction = x.get('directionIcon', 'STRAIGHT')
            if end_time - start_time == 0:
                continue

            width_fraction, y_from_bottom = size_by_mascot[active_mascot]
            mascot_clip = build_mascot_overlay(
                start_time,
                end_time,
                active_mascot,
                direction,
                base_vid_width,
                base_vid_height,
                base_vid_duration,
                mascot_width_fraction=width_fraction,
                mascot_y_from_bottom_fraction=y_from_bottom,
            )
            if mascot_clip is not None:
                mascot_clips.append(mascot_clip)

            if is_turn_direction(direction):
                active_mascot = flip_mascot(active_mascot)

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
        print("Error inside animation v3 fn")
        try:
            update_route_field(route_id, 'processStatus', 'ARROW_ATTACHMENT_ERROR')
        except Exception:
            logging.info('Error while updating DB')
