import os
from pathlib import Path
from typing import Iterator, Tuple, Union, Literal

from numpy import ndarray as Array

from skimage import filters

from ._save_image import save_image
from ._load_image import load_image
from ._grayscale import grayscale

def get_sequence_gradients(sequence_name: str, blur_radius: float = 0) -> None: #type: ignore
    sintel_path = Path(os.environ["SINTEL_PATH"]).expanduser()
    sequence_path = sintel_path/"test/final/{sequence_name}"
    frame_paths = sorted(sequence_path.iterdir())

    for i, (frame0, frame1) in enumerate(gray_frame_pairs(sequence_name)):
        frame = filters.gaussian(frame1, sigma=blur_radius)
        hori_der = frame[2:, 2:] - frame[2:, 1:-1]
        hori_der_path = f"_results/{sequence_name}/horizontal/{i:04d}.png"

        vert_der = frame[2:, 2:] - frame[1:-1, 2:]
        vert_der_path = f"_results/{sequence_name}/vertical/{i:04d}.png"
        
        temp_der = (frame1 - frame0)[2:, 2:]
        temp_der_path = f"_results/{sequence_name}/temporal/{i:04d}.png"

        save_image(hori_der, hori_der_path)
        save_image(vert_der, vert_der_path)
        save_image(temp_der, temp_der_path)

# TODO: in the future add blur value to path name
    os.system(f"ffmpeg -framerate 6" 
              f" -i _results/{sequence_name}/horizontal/%04d.png -y"
              f" -pix_fmt yuv420p _results/{sequence_name}/horizontal.mp4")
    os.system(f"ffmpeg -framerate 6" 
              f" -i _results/{sequence_name}/vertical/%04d.png -y"
              f" -pix_fmt yuv420p _results/{sequence_name}/vertical.mp4")
    os.system(f"ffmpeg -framerate 6" 
              f" -i _results/{sequence_name}/temporal/%04d.png -y"
              f" -pix_fmt yuv420p _results/{sequence_name}/temporal.mp4")


def gray_frame_pairs(sequence_name: str, split: Literal["test", "training"]) -> Iterator[Tuple[Array, Array]]:
    sintel_path = Path(os.environ["SINTEL_PATH"]).expanduser()
    sequence_path = sintel_path/f"{split}/final/{sequence_name}"
    frame_paths = sorted(sequence_path.iterdir())
    previous_frame: Union[Array, None] = None

    for frame_path in frame_paths:
        current_frame = grayscale(load_image(frame_path))
        if previous_frame is not None:
            yield previous_frame, current_frame
        previous_frame = current_frame
        
        
# frame = load_image(f"frame_{frame_num:04d}.png")


# def spatial_derivatives() :
    
#     # math
#     vert_der = frame[1:, 1:] - frame[:-1, 1:]
#     hori_der = frame[1:, 1:] - frame[1:, :-1]
#     #energy = (vert_der ** 2 + hori_der ** 2) ** 0.5
#     ##energy = (hori_der ** 2) ** 0.5
#     ##energy[0, 0, 0] = np.min(hori_der)

#     #save_image(energy, f"modified_horizontal_spatial_{frame_num:06d}.png")

#     save_image(vert_der, f"vertical/{frame_num:06d}.png")
#     save_image(hori_der, f"horizontal/{frame_num:06d}.png")
