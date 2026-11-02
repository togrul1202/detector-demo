#!/usr/bin/env bash
set -euo pipefail

mkdir -p models
URL="https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_s.onnx"
curl -L --fail -o models/yolox_s.onnx "$URL"
ls -lh models/yolox_s.onnx