import numpy as np


def BucketSort(arr: np.ndarray, /) -> np.ndarray:

    n = arr.shape[0]
    num = np.zeros(shape=(10, n + 1), dtype=np.int64)
    max_value = arr.max()
    digit = 0
    while max_value > 0:
        max_value //= 10
        digit += 1
    for i in range(digit):
        for j in range(n):
            row_index = (arr[j] // (10 ** i)) % 10
            num[row_index, num[row_index, n]] = arr[j]
            num[row_index, n] += 1
        index = 0
        for k in range(10):
            if num[k, n] > 0:
                for l in range(num[k, n]):
                    arr[index] = num[k, l]
                    index += 1
                num[k, n] = 0
    return arr