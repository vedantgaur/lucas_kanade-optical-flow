# import os

# from PIL import Image
# import numpy as np
# import matplotlib.pyplot as plt
# from numpy import ndarray as Array


# def save_image(image: Array, path: str) -> None:
#     # brightness/contrast
#     max_ = np.max(image)
#     min_ = np.min(image)
#     image -= min_
#     image /= max(max_ - min_, 1e-7)

#     # gamma encoding
#     image = np.uint8(image ** (1 / 2.2) * 255)

#     # saving
#     os.makedirs(os.path.dirname(path), exist_ok=True)
#     Image.fromarray(image, "RGB").save(path)


# def load_image(path: str) -> Array:
#     with Image.open(path) as pil_image:
#         lum_srgb = np.array(pil_image)

#     # gamma decoding
#     lum_linear = (lum_srgb / 255) ** 2.2
#     return lum_linear


# for frame_num in range(1, 50):
#     frame0 = load_image(f"frame_{frame_num:04d}.png")
#     frame1 = load_image(f"frame_{frame_num+1:04d}.png")

#     diff = (frame1 - frame0)[1:, 1:]
#     save_image(diff, f"temporal/{frame_num:06d}.png")