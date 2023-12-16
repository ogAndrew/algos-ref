"""
Asymptotic complexity in terms of size of `arr` `n`:
* Time: O(n ^ 2).
* Auxiliary space: O(1).
* Total space: O(n).
"""


def bubble_sort(arr):
    for start in range(len(arr)):
        for i in range(len(arr)-1, start, -1):
            if arr[i - 1] > arr[i]:
                (arr[i - 1], arr[i]) = (arr[i], arr[i - 1])

    return arr

# my approach


def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(n - 1, i, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr
