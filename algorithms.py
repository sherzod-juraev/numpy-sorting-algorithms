import numpy as np
from numba import njit


@njit
def BubbleSort(arr: np.ndarray, /) -> np.ndarray:

    n = arr.shape[0]
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


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