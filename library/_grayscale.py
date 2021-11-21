from numpy import ndarray as Array

def grayscale(image: Array) -> Array:
  return 0.3*image[:, :, 0] + 0.6*image[:, :, 1] + 0.1*image[:, :, 2] 