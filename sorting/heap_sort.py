"""
Asymptotic complexity in terms of size of `arr` `n`:
* Time: O(n * log(n)).
* Auxiliary space: O(1).
* Total space: O(n).
"""


def heapify(arr, n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    # if left is inbounds and left child is greater than root 
    if l < n and arr[i] < arr[l]:
        largest = l
    # if right is inbounds and right child is greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    # Build max heap
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]
        # Heapify root element
        heapify(arr, i, 0)
    return arr
