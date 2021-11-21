import os
from itertools import product
from pathlib import Path
from typing import Iterator, Tuple, Union, List, Literal

from numpy import ndarray as Array
import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt

from skimage import filters

from ._save_image import save_image
from ._load_image import load_image
from ._grayscale import grayscale
from ._get_sequence_gradients import get_sequence_gradients, gray_frame_pairs

def get_sequence_names(split: Literal["test", "training"]) -> Iterator[str]:
    sintel_path = Path(os.environ["SINTEL_PATH"]).expanduser()
    for sequence_path in (sintel_path/f"{split}/final").iterdir():
        print(f"-----> {sequence_path}")
        yield sequence_path.name

