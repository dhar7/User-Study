import serializes
from itertools import tee

def bubble_sort(arr):
    for _ in range(len(arr)):
        a, b = tee(arr)
        next(b, None)
        for i, j in zip(a, b):
            if i > j:
                arr[arr.index(i)], arr[arr.index(j)] = j, i
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", bubble_sort(arr))
