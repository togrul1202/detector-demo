# Real-Time Object Detection with YOLOX: Python and C++ Inference Benchmark

Deploying a pretrained YOLOX-s detector with ONNX Runtime on GPU. The goal is to
write the full pipeline (preprocessing, decoding, NMS) myself, first in Python,
then in C++, and to compare latency and FPS between the two.

## Status

- [x] Docker dev container with GPU support
- [x] Model download script
- [ ] Python inference on image and video
- [ ] Latency and FPS benchmark
- [ ] C++ inference with ONNX Runtime
- [ ] Python vs C++ comparison

## Setup

Requirements: Docker, NVIDIA driver, NVIDIA Container Toolkit, VS Code with
the Dev Containers extension.

1. Clone the repository and open it in VS Code.
2. Run "Dev Containers: Reopen in Container".
3. Download the model: `./scripts/download_model.sh`
4. Check GPU access: `python3 scripts/check_gpu.py`

## Results

Coming soon.

## Credits

Model: [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX) (Apache-2.0).