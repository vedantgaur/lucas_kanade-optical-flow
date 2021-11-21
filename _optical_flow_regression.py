import os
from itertools import product
from pathlib import Path
from typing import Iterator, Tuple, Union, List, Literal
import library

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from numpy import ndarray as Array
import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt

from ._get_labeled_lk_results import get_labeled_lk_results

def linear_regression(num_of_iters: int) -> Iterator[float]:
    x = np.zeros((num_of_iters, 2), dtype=float)
    y = np.zeros((num_of_iters, 2), dtype=float)
    for i in range(num_of_iters):
        for iterable in get_labeled_lk_results(num_of_iters):
            x[i] = iterable[0]
            y[i] = iterable[1]
    print(x)
    x_samples_train = x[:int(num_of_iters*0.8)]
    print(x_samples_train)
    y_true_train = y[:int(num_of_iters*0.8)]
    x_samples_test = x[int(num_of_iters*0.8):]
    print(x_samples_test)
    y_true_test = y[int(num_of_iters*0.8):]
            
    reg = LinearRegression().fit(x_samples_train, y_true_train)
    
    for i in range(int(num_of_iters*0.2)):
        y_pred = reg.predict(x_samples_test)
        yield mean_squared_error(y_pred, y_true_test)

