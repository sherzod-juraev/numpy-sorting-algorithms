import numpy as np
from numba import njit


@njit
def RadixSortLSD(arr: np.ndarray, /) -> np.ndarray:

    n = arr.shape[0]
    border = arr.max()
    num = np.zeros(shape=10, dtype=np.int64)
    auxiliary = np.zeros(shape=n, dtype=np.int64)
    exp = 1
    while exp <= border:
        for j in range(10):
            num[j] = 0
        for k in range(n):
            num[(arr[k] // exp) % 10] += 1
        for l in range(1, 10):
            num[l] += num[l - 1]
        for m in range(n - 1, -1, -1):
            auxiliary[num[(arr[m] // exp) % 10] - 1] = arr[m]
            num[(arr[m] // exp) % 10] -= 1
        for o in range(n):
            arr[o] = auxiliary[o]
        exp *= 10
    return arr


arr = np.random.randint(1, 99, 30)
print(RadixSortLSD(arr))