from typing import Union
from pathlib import Path

from PIL import Image
import numpy as np
from numpy import ndarray as Array

def load_image(path: Union[Path, str]) -> Array:
    with Image.open(path) as pil_image:
        lum_srgb = np.array(pil_image)

    # gamma decoding
    lum_linear = (lum_srgb / 255) ** 2.2
    return lum_linear