FROM nvidia/cuda:12.6.3-cudnn-runtime-ubuntu24.04
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv git
WORKDIR /work
COPY requirements.txt .
RUN pip install --break-system-packages -r requirements.txt
COPY . .
