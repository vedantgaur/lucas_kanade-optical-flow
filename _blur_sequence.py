import os
from pathlib import Path

from skimage import filters

from ._save_image import save_image
from ._load_image import load_image
from ._grayscale import grayscale


def blur_sequence(sequence_name: str) -> None:

    sintel_path = Path(os.environ["SINTEL_PATH"]).expanduser()
    sequence_path = sintel_path/f"test/final/{sequence_name}"
    frame_paths = sorted(sequence_path.iterdir())

    for frame_path in frame_paths:
        frame = grayscale(load_image(frame_path))
        blurred_frame = filters.gaussian(frame, sigma=5)
        blurred_frame_path = f"_results/{sequence_name}/blurred/{frame_path.name}"
        save_image(blurred_frame, blurred_frame_path)

    os.system(f"ffmpeg -framerate 6" 
              f" -i _results/{sequence_name}/blurred/frame_%04d.png -y"
              f" -pix_fmt yuv420p _results/{sequence_name}/blurred.mp4")