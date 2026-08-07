#!/usr/bin/env python3
"""
Local runner for direction detection.

Usage:
  python test_direction_detection_local.py /path/to/video.mp4
  python test_direction_detection_local.py /path/to/video.mp4 -o ./out/directions.json

Does not modify production code. Places a symlink (or copy) under blurred/
so directionDetection() can find the file, then writes JSON output.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import shutil
import sys
import time
from decimal import Decimal
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")


def _json_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")


def _ensure_blurred_link(video_path: Path, blurred_dir: Path) -> tuple[str, Path, bool]:
    """
    Make video available as blurred/<name>.
    Returns (file_name, link_path, created_temp).
    If the video already lives under blurred/, reuse it and do not delete after.
    """
    blurred_dir.mkdir(parents=True, exist_ok=True)
    video_path = video_path.resolve()

    try:
        if video_path.parent.resolve() == blurred_dir.resolve():
            return video_path.name, video_path, False
    except OSError:
        pass

    link_path = blurred_dir / video_path.name
    if link_path.exists() or link_path.is_symlink():
        # Avoid clobbering an existing blurred asset; use a unique name
        stem, suffix = video_path.stem, video_path.suffix
        link_path = blurred_dir / f"{stem}__local_test{suffix}"

    created_temp = True
    try:
        os.symlink(video_path, link_path)
        logging.info("Symlinked %s -> %s", video_path, link_path)
    except OSError:
        shutil.copy2(video_path, link_path)
        logging.info("Copied %s -> %s", video_path, link_path)

    return link_path.name, link_path, created_temp


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run direction detection on a local video and write JSON output."
    )
    parser.add_argument("video", type=str, help="Path to a local video file")
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default=None,
        help="Output JSON path (default: ./direction_output/<video_stem>_directions.json)",
    )
    parser.add_argument(
        "--keep-blurred-link",
        action="store_true",
        help="Do not remove the temporary symlink/copy under blurred/",
    )
    args = parser.parse_args()

    video_path = Path(args.video).expanduser()
    if not video_path.is_file():
        logging.error("Video not found: %s", video_path)
        return 1

    project_root = Path(__file__).resolve().parent
    os.chdir(project_root)

    blurred_dir = project_root / "blurred"
    file_name, link_path, created_temp = _ensure_blurred_link(video_path, blurred_dir)

    if args.output:
        output_path = Path(args.output).expanduser().resolve()
    else:
        out_dir = project_root / "direction_output"
        out_dir.mkdir(parents=True, exist_ok=True)
        output_path = out_dir / f"{video_path.stem}_directions.json"

    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Import after chdir so relative paths (blurred/, helpers) resolve correctly
    from direction_detection import directionDetection

    logging.info("Starting direction detection for %s", file_name)
    started = time.time()
    try:
        result = directionDetection(file_name)
    finally:
        if created_temp and not args.keep_blurred_link:
            try:
                if link_path.is_symlink() or link_path.is_file():
                    link_path.unlink()
                    logging.info("Removed temporary blurred entry %s", link_path)
            except OSError as e:
                logging.warning("Could not remove temporary file %s: %s", link_path, e)

    elapsed = time.time() - started

    if result is False or result is None:
        logging.error("directionDetection failed (elapsed %.1fs)", elapsed)
        return 2

    payload = {
        "video": str(video_path.resolve()),
        "file_name": file_name,
        "elapsed_seconds": round(elapsed, 2),
        "direction_count": len(result),
        "directions": result,
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, default=_json_default)

    logging.info("Wrote %d directions to %s (%.1fs)", len(result), output_path, elapsed)
    print(output_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
