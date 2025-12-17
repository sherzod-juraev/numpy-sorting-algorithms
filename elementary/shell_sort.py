import numpy as np
from numba import njit


@njit
def ShellSort(arr: np.ndarray, /) -> np.ndarray:

    h, n = 1, arr.shape[0]
    while h < n // 3:
        h = (h * 3) + 1
    while h > 0:
        for j in range(h, n):
            min_value, k = arr[j], j
            while k >= h and arr[k - h] > min_value:
                arr[k] = arr[k - h]
                k -= h
            arr[k] = min_value
        h //= 3
    return arr