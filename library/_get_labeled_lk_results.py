import os
from os import listdir
from itertools import product
from pathlib import Path
#from posix import listdir
from typing import Iterator, Tuple, Union, Iterable, Literal

from numpy import ndarray as Array
import numpy as np
import numpy
from numpy.core.records import array
from ._read_flow import read_flow_files

"""
for _ in range(1000):
# sample a random sequence (sequence_name)
# sample random frame 
# sample random locations in frame
    for _ in blur_radii:

"""#split: Literal["test", "training"], sequence_names: Iterable[str]
#np.frombuffer, Path.read_bytes
def get_labeled_lk_results(num_of_iters: int): #-> Tuple:
    flow_pairs = [0, 0]
    true_flow_pairs = [0, 0]
    flow_components = np.array
    true_flow_components = np.array
    #list of folders /_results with the starting 'lucas_kanade('
    sintel_path = Path(os.environ["SINTEL_PATH"]).expanduser()
    #lk_dirs = list(Path("_results").glob(f"lucas_kanade(*"))
    MPI_dirs = list(os.listdir(sintel_path/"training/flow"))
    # print(len(MPI_dirs))
    #print(MPI_dirs)
    for i in range(num_of_iters):
        random_sequence_index = np.random.randint(0, len(MPI_dirs))
        # print(random_sequence_index)
        chosen_sequence = MPI_dirs[random_sequence_index]
        chosen_sequence_results = list(Path("_results").glob(f"lucas_kanade({chosen_sequence}*"))
        random_sequence_index_blur = np.random.randint(0, len(chosen_sequence_results))
        result_numpy_arrays = list(chosen_sequence_results[random_sequence_index_blur].glob("*.npy"))
        # print(result_numpy_arrays)
        result_flow_arrays = listdir(sintel_path/f"training/flow/{MPI_dirs[random_sequence_index]}")
        n_frames = len(result_numpy_arrays)  
        random_frame_index = np.random.randint(0, n_frames)
        random_frame_npy = np.load(f'{result_numpy_arrays[random_frame_index]}')
        random_frame_flo = read_flow_files(str(sintel_path/f"training/flow/{MPI_dirs[random_sequence_index]}/{result_flow_arrays[random_frame_index]}"))
        # print(random_frame_npy)
        random_pixel_index_x = np.random.randint(0, (random_frame_npy.shape)[0])
        # print((random_frame_npy.shape)[0])
        # print((random_frame_npy.shape)[1])
        random_pixel_index_y = np.random.randint(0, (random_frame_npy.shape)[1])
        flow_pairs[0] = random_frame_npy[random_pixel_index_x, random_pixel_index_y, 0]
        flow_pairs[1] = random_frame_npy[random_pixel_index_x, random_pixel_index_y, 1]
        
        # flow_components = numpy.append(flow_components, flow_pairs)
        true_flow_pairs[0] = random_frame_flo[random_pixel_index_x, random_pixel_index_y, 0]
        true_flow_pairs[1] = random_frame_flo[random_pixel_index_x, random_pixel_index_y, 1]
        # true_flow_components = numpy.append(true_flow_components, true_flow_pairs)

        full_results = [flow_pairs, true_flow_pairs]
        yield full_results
        # flow_components = numpy.append(flow_components, random_frame_npy[random_pixel_index_x, random_pixel_index_y, 0])
        # flow_components = numpy.append(flow_components, random_frame_npy[random_pixel_index_x, random_pixel_index_y, 1])
        # true_flow_components = numpy.append(true_flow_components, random_frame_flo[random_pixel_index_x, random_pixel_index_y, 0])
        # true_flow_components = numpy.append(true_flow_components, random_frame_flo[random_pixel_index_x, random_pixel_index_y, 1])
    # print(flow_components)
    # results = np.array(((flow_components), (true_flow_components)), dtype=object)
    # # print(f"full results ------> {results}")
    # # print(f"FIRST CELL ======== {results[0][0]}")
    # # print(f"calculated results {results[0]}")
    # # print(f"both results {results}")
    # #an_array = np.array(((1, 2),(3, 4)))
    # # array_of_tuples = map(tuple, results)
    # # tuple_of_tuples = tuple(array_of_tuples)
    # # print(tuple_of_tuples)
    # return results
    # frame_paths = lk_dirs[0].glob("*.npy")
    # concatenate function --> flatten all arrays out