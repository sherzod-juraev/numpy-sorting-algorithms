import numpy as np
from numba import njit


@njit
def InsertionSort(arr: np.ndarray, /) -> np.ndarray:

    n = arr.shape[0]
    for i in range(1, n):
        min_value, j = arr[i], i
        while j >= 1 and arr[j - 1] > min_value:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = min_value
    return arr