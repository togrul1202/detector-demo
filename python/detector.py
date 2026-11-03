import cv2
import numpy as np

INPUT_SIZE = (640, 640)  # (height, width)
PAD_VALUE = 114


def preprocess(image_bgr, input_size=INPUT_SIZE):
    h, w = image_bgr.shape[:2]
    ratio = min(input_size[0] / h, input_size[1] / w)
    new_w, new_h = int(w * ratio), int(h * ratio)

    resized = cv2.resize(image_bgr, (new_w, new_h), interpolation=cv2.INTER_LINEAR)
    padded = np.full((input_size[0], input_size[1], 3), PAD_VALUE, dtype=np.uint8)
    padded[:new_h, :new_w] = resized

    tensor = padded.transpose(2, 0, 1)                        # HWC -> CHW
    tensor = np.ascontiguousarray(tensor, dtype=np.float32)
    return tensor[None], ratio                                # (1, 3, 640, 640)