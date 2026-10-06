#!/usr/bin/env python3
"""
Temp script to run arrow attachment locally from a JSON input file.

Usage:
  python temp_run_arrow_attach.py /path/to/input.json

JSON format:
  {
    "video_path": "/absolute/or/relative/path/to/video.mp4",
    "directions": [
      {
        "directionIcon": "STRAIGHT",
        "startTime": 0,
        "endTime": 5,
        "description": "Go straight",
        "message": "Go straight"
      },
      {
        "directionIcon": "LEFT",
        "startTime": 5,
        "endTime": 8,
        "description": "Turn left",
        "message": "Turn left"
      }
    ],
    "hex_color": null
  }

Optional keys:
  - hex_color: hex without '#', e.g. "FF5733". If omitted/null, uses old_arrows/.
  - use_gifs: if true, uses GIF overlay path instead of PNG overlay.
  - animation_version: "v1" (arrows + bird), "v2" (kids bunny only), "v2.1" (kids bunny, wider Y range),
    or "v3" (bunny/duck alternate on turns). Default "v2" when use_gifs is true.
  - bird_width_fraction: v1 bird size as fraction of video width (e.g. 0.45 = 45%). Clamped to 0.05–1.0.
  - bird_y_fraction: v1 bird top offset as fraction of video height (e.g. 0.06 = 6% down). Clamped to 0.0–0.8.
  - mascot_width: v2.1 size as fraction of video width. Clamped to 0.05–1.0.
  - mascot_width_fraction: v2 size, or v3 shared fallback size. Clamped to 0.05–1.0.
  - mascot_y_from_bottom_fraction: v2 Y (0.0–0.5), v2.1 Y (0.0–1.0), or v3 shared fallback Y.
  - bunny_width_fraction / bunny_y_from_bottom_fraction: v3 bunny-only size and Y (override shared).
  - duck_width_fraction / duck_y_from_bottom_fraction: v3 duck-only size and Y (override shared).
"""

import argparse
import json
import os
import shutil
import sys


def ensure_dirs():
    os.makedirs('blurred', exist_ok=True)
    os.makedirs('final', exist_ok=True)


def stage_video(video_path: str) -> str:
    if not os.path.isfile(video_path):
        raise FileNotFoundError(f'Video not found: {video_path}')

    file_name = os.path.basename(video_path)
    dest = os.path.join('blurred', file_name)

    abs_src = os.path.abspath(video_path)
    abs_dest = os.path.abspath(dest)

    if abs_src != abs_dest:
        shutil.copy2(abs_src, dest)
        print(f'Copied video -> {dest}')
    else:
        print(f'Video already in place: {dest}')

    return file_name


def load_input(json_path: str) -> dict:
    if not os.path.isfile(json_path):
        raise FileNotFoundError(f'JSON not found: {json_path}')

    with open(json_path, 'r') as f:
        data = json.load(f)

    if 'video_path' not in data:
        raise ValueError('JSON must include "video_path"')
    if 'directions' not in data or not isinstance(data['directions'], list):
        raise ValueError('JSON must include "directions" as a list')

    return data


def main():
    parser = argparse.ArgumentParser(description='Run arrow attachment from a JSON file')
    parser.add_argument('json_path', help='Path to JSON with video_path and directions')
    args = parser.parse_args()

    data = load_input(args.json_path)
    video_path = data['video_path']
    directions = data['directions']
    hex_color = data.get('hex_color')
    use_gifs = data.get('use_gifs', False)
    animation_version = data.get('animation_version', 'v2' if use_gifs else None)
    bird_width_fraction = data.get('bird_width_fraction')
    bird_y_fraction = data.get('bird_y_fraction')
    mascot_width = data.get('mascot_width')
    mascot_width_fraction = data.get('mascot_width_fraction')
    mascot_y_from_bottom_fraction = data.get('mascot_y_from_bottom_fraction')
    bunny_width_fraction = data.get('bunny_width_fraction')
    bunny_y_from_bottom_fraction = data.get('bunny_y_from_bottom_fraction')
    duck_width_fraction = data.get('duck_width_fraction')
    duck_y_from_bottom_fraction = data.get('duck_y_from_bottom_fraction')

    ensure_dirs()
    file_name = stage_video(video_path)

    print(f'Directions count: {len(directions)}')
    print(f'hex_color: {hex_color}')
    print(f'use_gifs: {use_gifs}')
    print(f'animation_version: {animation_version}')
    print(f'bird_width_fraction: {bird_width_fraction}')
    print(f'bird_y_fraction: {bird_y_fraction}')
    print(f'mascot_width: {mascot_width}')
    print(f'mascot_width_fraction: {mascot_width_fraction}')
    print(f'mascot_y_from_bottom_fraction: {mascot_y_from_bottom_fraction}')
    print(f'bunny_width_fraction: {bunny_width_fraction}')
    print(f'bunny_y_from_bottom_fraction: {bunny_y_from_bottom_fraction}')
    print(f'duck_width_fraction: {duck_width_fraction}')
    print(f'duck_y_from_bottom_fraction: {duck_y_from_bottom_fraction}')
    print('Starting arrow attachment...')

    if use_gifs:
        route_id = data.get('route_id', 'temp')
        if animation_version == 'v1':
            from arrow_animation_v1 import animate_arrow_gifs_v1
            animate_arrow_gifs_v1(
                route_id, file_name, directions, hex_color,
                bird_width_fraction=bird_width_fraction,
                bird_y_fraction=bird_y_fraction
            )
        elif animation_version == 'v3':
            from arrow_animation_v3 import animate_arrow_gifs_v3
            animate_arrow_gifs_v3(
                route_id, file_name, directions, hex_color,
                mascot_width_fraction=mascot_width_fraction,
                mascot_y_from_bottom_fraction=mascot_y_from_bottom_fraction,
                bunny_width_fraction=bunny_width_fraction,
                bunny_y_from_bottom_fraction=bunny_y_from_bottom_fraction,
                duck_width_fraction=duck_width_fraction,
                duck_y_from_bottom_fraction=duck_y_from_bottom_fraction,
            )
        elif animation_version == 'v2.1':
            from arrow_animation_v2_1 import animate_arrow_gifs_v2_1
            animate_arrow_gifs_v2_1(
                route_id, file_name, directions, hex_color,
                mascot_width_fraction=mascot_width,
                mascot_y_from_bottom_fraction=mascot_y_from_bottom_fraction,
            )
        else:
            from arrow_animation_v2 import animate_arrow_gifs_v2
            animate_arrow_gifs_v2(
                route_id, file_name, directions, hex_color,
                mascot_width_fraction=mascot_width_fraction,
                mascot_y_from_bottom_fraction=mascot_y_from_bottom_fraction
            )
    else:
        from arrow_attachment import arrow_attachment_main
        arrow_attachment_main(file_name, directions, hex_color)

    output_path = os.path.abspath(os.path.join('final', file_name))
    print(f'Done. Output: {output_path}')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        sys.exit(1)
