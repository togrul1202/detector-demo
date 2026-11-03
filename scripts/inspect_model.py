import sys
import cv2
from python.detector import create_session, preprocess

model_path = "models/yolox_s.onnx"
image_path = sys.argv[1]

session = create_session(model_path)

inp = session.get_inputs()[0]
print("Input:", inp.name, inp.shape, inp.type)
for out in session.get_outputs():
    print("Output:", out.name, out.shape)

image = cv2.imread(image_path)
tensor, ratio = preprocess(image)
outputs = session.run(None, {inp.name: tensor})
print("Raw output shape:", outputs[0].shape)
print("First row:", outputs[0][0, 0])