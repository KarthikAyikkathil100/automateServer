import logging
import subprocess
from typing import Iterable, List, Sequence


def _validate_trim_ranges(to_trim_timerange: Iterable[Sequence[float]]) -> List[List[float]]:
    """Normalize and validate trim ranges as [[start, end], ...]."""
    try:
        normalized: List[List[float]] = []

        for idx, pair in enumerate(to_trim_timerange):
            if not isinstance(pair, (list, tuple)) or len(pair) != 2:
                raise ValueError(
                    f"Invalid range at index {idx}: expected [start, end], got {pair!r}"
                )

            start, end = float(pair[0]), float(pair[1])
            if start < 0 or end < 0:
                raise ValueError(f"Invalid range at index {idx}: times must be >= 0")
            if end <= start:
                raise ValueError(
                    f"Invalid range at index {idx}: end ({end}) must be > start ({start})"
                )

            normalized.append([start, end])

        return normalized
    except Exception as e:
        logging.error(e)
        raise Exception('Error while validating trim ranges')


def trim_video_helper(inputFilePath: str, outputFilePath: str, toTrimTimerange: list):
    """
    Remove time ranges from a video using ffmpeg.

    Args:
        inputFilePath: Input video file path.
        outputFilePath: Output video file path.
        toTrimTimerange: List of ranges to remove, e.g. [[1, 40], [40, 50]].
    """
    try:
        ranges = _validate_trim_ranges(toTrimTimerange)

        if not ranges:
            cmd = [
                "ffmpeg",
                "-y",
                "-i",
                inputFilePath,
                "-c",
                "copy",
                outputFilePath,
            ]
            subprocess.run(cmd, check=True)
            return outputFilePath

        # Keep everything except the provided remove-ranges.
        remove_expr = "+".join(f"between(t,{start},{end})" for start, end in ranges)
        keep_expr = f"not({remove_expr})"

        video_filter = f"select='{keep_expr}',setpts=N/FRAME_RATE/TB"
        audio_filter = f"aselect='{keep_expr}',asetpts=N/SR/TB"

        cmd = [
            "ffmpeg",
            "-y",
            "-i",
            inputFilePath,
            "-vf",
            video_filter,
            "-af",
            audio_filter,
            "-c:v",
            "libx264",
            "-c:a",
            "aac",
            outputFilePath,
        ]

        subprocess.run(cmd, check=True)
        return outputFilePath
    except Exception as e:
        logging.error(e)
        raise Exception('Error while trimming video')

