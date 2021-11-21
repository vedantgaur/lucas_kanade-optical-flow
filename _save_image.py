import os
from typing import Union
from pathlib import Path

from PIL import Image
import numpy as np
from numpy import ndarray as Array

def save_image(image: Array, path: Union[Path, str]) -> None:
    # brightness/contrast
    max_ = np.max(image)
    min_ = np.min(image)
    image -= min_
    image /= max(max_ - min_, 1e-7)

    # gamma encoding
    image = np.uint8(image ** (1 / 2.2) * 255)

    # saving
    os.makedirs(os.path.dirname(path), exist_ok=True)
    Image.fromarray(image).save(path)