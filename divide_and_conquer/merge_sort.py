import numpy as np
from numba import njit


@njit
def MergeSort(arr: np.ndarray, /) -> np.ndarray:

    n = arr.shape[0]
    temp = np.empty(n, dtype=arr.dtype)
    width = 1

    while width < n:

        for i in range(0, n, 2 * width):

            left = i
            mid = min(i + width, n)
            right = min(i + 2 * width, n)

            l, r, k = left, mid, left

            while l < mid and r < right:
                if arr[l] < arr[r]:
                    temp[k] = arr[l]
                    l += 1
                else:
                    temp[k] = arr[r]
                    r += 1
                k += 1

            while l < mid:
                temp[k] = arr[l]
                l += 1
                k += 1

            while r < right:
                temp[k] = arr[r]
                r += 1
                k += 1

        for i in range(n):
            arr[i] = temp[i]
        width *= 2
    return arr