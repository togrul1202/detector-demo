import numpy as np
from python.detector import preprocess


def test_preprocess_shape_dtype_and_ratio():
    image = np.zeros((480, 1280, 3), dtype=np.uint8)
    tensor, ratio = preprocess(image)
    assert tensor.shape == (1, 3, 640, 640)
    assert tensor.dtype == np.float32
    assert ratio == 0.5