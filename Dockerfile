FROM python:3.12-slim-bookworm@sha256:935c3c5b12357a7e10caa9c1e6ca5692344d97cf229832ef584be2cec9fc03df


WORKDIR /app

RUN mkdir -p inputs blurred multithreaded_ou multithread-res final images text_json colored_gifs


# Create a virtual environment
# RUN python -m venv venv

# RUN source venv/bin/activate

# Install system libs required for Pillow/MoviePy/OpenCV
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6 \
    libxrender1 \
    libgl1 \
    libcurl4 \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libwebp-dev \
    zlib1g-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libopenjp2-7-dev \
    libharfbuzz-dev \
    libfribidi-dev \
    giflib-tools \
    libimagequant-dev \
    libraqm-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
# deface declares opencv-python. Install it without dependencies so the
# headless cv2 wheel stays the only OpenCV distribution in the image.
RUN grep -v '^deface==' requirements.txt > /tmp/requirements-main.txt \
    && pip install --no-cache-dir -r /tmp/requirements-main.txt \
    && pip install --no-cache-dir --no-deps deface==1.5.0 \
    && python - <<'PY'
import subprocess
import importlib.metadata as metadata

check = subprocess.run(["pip", "check"], capture_output=True, text=True)
allowed = "deface 1.5.0 requires opencv-python, which is not installed."
lines = [ln.strip() for ln in (check.stdout + check.stderr).splitlines() if ln.strip()]
unexpected = [ln for ln in lines if ln != allowed]
if unexpected:
    raise SystemExit("pip check failed:\n" + "\n".join(unexpected))
names = {dist.metadata["Name"].lower() for dist in metadata.distributions()}
if "opencv-python" in names or "opencv-python-headless" not in names:
    raise SystemExit(f"unexpected OpenCV distributions: {sorted(names)}")
PY
RUN deface --help >/dev/null \
    && python -c "import cv2, PIL, boto3, requests, celery, pycurl; from moviepy.editor import VideoFileClip"

# Force MoviePy to use system ffmpeg
ENV IMAGEIO_FFMPEG_EXE=/usr/bin/ffmpeg

# RUN apt-get update && \
#     apt-get install -y ffmpeg && \
#     rm -rf /var/lib/apt/lists/*

COPY common.py .
COPY video.py .
COPY tst_scene_render.py .

COPY arrow_attachment.py .
COPY direction_detection.py .
COPY blur_automate.py .
COPY sliding_window.py .
COPY arrow_attachment.py .
COPY helpers.py .
COPY text_blur.py .
COPY tint_color.py .
COPY images/ ./images/
COPY old_arrows/ ./old_arrows/
COPY newGifs/ ./newGifs/
COPY arrow_animations.py ./arrow_animations.py
COPY animation_gif_helpers.py ./animation_gif_helpers.py
COPY constants.py ./constants.py

# Celery
COPY celery_app.py ./celery_app.py
COPY celery_tasks.py ./celery_tasks.py
COPY ecs_protection.py ./ecs_protection.py

# Default command
CMD ["celery", "-A", "celery_app", "worker", "--loglevel=info", "--concurrency=5", "--pool=prefork", "--prefetch-multiplier=1"]

