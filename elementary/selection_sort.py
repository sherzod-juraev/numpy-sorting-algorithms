import numpy as np
from numba import njit


@njit
def SelectionSort(arr: np.ndarray, /) -> np.ndarray:

    n = arr.shape[0]
    for i in range(n - 1, -1, -1):
        max_index = i
        for j in range(i, -1, -1):
            if arr[j] > arr[max_index]:
                max_index = j
        if max_index != i:
            arr[max_index], arr[i] = arr[i], arr[max_index]
    return arr