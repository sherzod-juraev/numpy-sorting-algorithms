import numpy as np
from numba import njit


@njit
def CountSort(arr: np.ndarray, /) -> np.ndarray:

    n = arr.shape[0]
    border = arr.max()
    num = np.zeros(shape=border + 1, dtype=np.int64)
    auxiliary = np.zeros(shape=n, dtype=np.int64)
    for i in range(n):
        num[arr[i]] += 1
    for j in range(1, border + 1):
        num[j] += num[j - 1]
    for k in range(n - 1, -1, -1):
        auxiliary[num[arr[k]] - 1] = arr[k]
        num[arr[k]] -= 1
    for l in range(n):
        arr[l] = auxiliary[l]
    return arr