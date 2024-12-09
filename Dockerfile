FROM python:3


WORKDIR /app

RUN mkdir -p inputs blurred multithreaded_ou multithread-res final images text_json


# Create a virtual environment
RUN python -m venv venv

# Install the required dependencies inside the virtual environment
RUN pip install --no-cache-dir common Flask boto3 numpy opencv-python-headless awscli deface psutil

RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

COPY video.py .
COPY tst_scene_render.py .

COPY app.py .
COPY arrow_attachment.py .
COPY direction_detection.py .
COPY blur_automate.py .
COPY sliding_window.py .
COPY arrow_attachment.py .
COPY helpers.py .
COPY text_blur.py .
COPY images/ ./images/

# Verify the installation
RUN aws --version

# Expose the port the app runs on
EXPOSE 5000

ENTRYPOINT ["python", "app.py"]

