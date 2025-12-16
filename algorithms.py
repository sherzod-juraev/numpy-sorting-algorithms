import numpy as np
from numba import njit
from datetime import datetime

@njit
def BubbleSort(arr: np.ndarray, /) -> np.ndarray:

    n = arr.shape[0]
    for i in range(n):
        fiting = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                fiting = True
        if not fiting:
            break
    return arr

arr = np.random.randint(0, 10000, size=20_000)
print(arr)
start = datetime.now()
print(BubbleSort(arr))
ended = datetime.now()
print(ended - start)