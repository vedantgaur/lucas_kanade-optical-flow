import os
from itertools import product
from pathlib import Path
from typing import Iterator, Tuple, Union, Literal

from numpy import ndarray as Array
import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt

from skimage import filters

from ._save_image import save_image
from ._load_image import load_image
from ._grayscale import grayscale
from ._get_sequence_gradients import get_sequence_gradients, gray_frame_pairs

def calc_lk(sequence_name: str, sequence_type: Literal["test", "training"], blur_radius: float = 15, patch_size: int = 9) -> None: #type: ignore
    #patch = find patch of image --> need to know how/which patch is the best
    print(f"inside calc_lk {sequence_name}")
    for i, (frame0, frame1) in enumerate(gray_frame_pairs(sequence_name, sequence_type)):
        frame0 = filters.gaussian(frame0, sigma=blur_radius)
        frame1 = filters.gaussian(frame1, sigma=blur_radius)

        x_der = frame1[2:, 2:] - frame1[2:, 1:-1]
        y_der = frame1[2:, 2:] - frame1[1:-1, 2:]
        t_der = (frame1 - frame0)[2:, 2:]

        flow_field = np.zeros((frame1.shape[0]-2*patch_size, frame1.shape[1]-2*patch_size, 2))
        for u,v in product(range(flow_field.shape[0]), range(flow_field.shape[1])):
            x_der_patch = x_der[u:u+patch_size, v:v+patch_size].reshape(-1)
            y_der_patch = y_der[u:u+patch_size, v:v+patch_size].reshape(-1)
            t_der_patch = t_der[u:u+patch_size, v:v+patch_size].reshape(-1)

            #computes least squares of the stacked x and y derivatives with the t_der_patch as the y
            #print(np.vstack([x_der_patch, y_der_patch]).T.shape, t_der_patch.shape)
            flow_field[u, v] = np.linalg.lstsq(np.vstack([x_der_patch, y_der_patch]).T, t_der_patch, rcond=None)[0]
        # plt.imshow((flow_field[:, :, 0]**2+flow_field[:, :, 1]**2)**0.5)
        # plt.show()
        output_path = f"_results//lucas_kanade({sequence_name},blur={blur_radius})"
        os.makedirs(output_path, exist_ok=True)
        np.save(f"{output_path}/flow{i:04d}.npy", flow_field)
        print(f"{output_path}/flow{i:04d}.npy")
        vis = np.dstack((flow_field, np.zeros((*flow_field.shape[:2], 1)))) #type: ignore
        save_image(vis, f"{output_path}/vis{i:04d}.png")

    os.system(f"ffmpeg -framerate 6" 
              f" -i {output_path}/vis%04d.png -y"
              f" -pix_fmt yuv420p {output_path}/vis.mp4")


    # A, v = []
    # i = 0
    # for pixel in x_der:
    #     A[i, 0] =  pixel
    #     for ypixel in y_der:
    #         A[i, 1] = ypixel
    #     i += 13