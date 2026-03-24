FROM python:3.8


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

# Install the required dependencies inside the virtual environment
# RUN pip install --no-cache-dir common Flask boto3 numpy opencv-python-headless awscli deface psutil moviepy==1.0.3 pillow imageio tqdm decorator

RUN pip install --no-cache-dir \
    pillow==9.5.0 \
    common \
    numpy==1.24.4 \
    moviepy==1.0.3 \
    opencv-python-headless==4.8.1.78 \
    imageio==2.35.1 \
    imageio-ffmpeg==0.5.1 \
    decorator \
    tqdm \
    Flask \
    boto3 \
    awscli \
    deface \
    psutil \
    "celery[sqs]"

# Force MoviePy to use system ffmpeg
ENV IMAGEIO_FFMPEG_EXE=/usr/bin/ffmpeg

# RUN apt-get update && \
#     apt-get install -y ffmpeg && \
#     rm -rf /var/lib/apt/lists/*

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
COPY diy_segment_helpers.py ./diy_segment_helpers.py
COPY constants.py ./constants.py
COPY trim_video.py ./trim_video.py

# Celery
COPY celery_app.py ./celery_app.py
COPY celery_tasks.py ./celery_tasks.py
COPY ecs_protection.py ./ecs_protection.py

# Verify the installation
RUN aws --version

# Expose the port the app runs on
EXPOSE 5000

# ENTRYPOINT ["python", "app.py"]
# Default command
CMD ["celery", "-A", "celery_app", "worker", "--loglevel=info", "--concurrency=4", "--pool=prefork", "--prefetch-multiplier=1"]

