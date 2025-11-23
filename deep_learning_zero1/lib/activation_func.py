

import numpy as np


def sigmoid_func(x):
    return 1 / (1 + np.exp(-x))    

def step_func(x):
    return np.array(x > 0, dtype=int)

def relu_func(x):
    return np.maximum(0, x)