# mine

def merge_sort(arr):
    helper(arr, 0, len(arr) - 1)
    return arr


def helper(arr, start, end):
    # leaf node
    if start == end:
        return

    # internal node worker
    mid = (start + end) // 2
    helper(arr, start, mid)
    helper(arr, mid + 1, end)

    # merge two sorted halfs
    i = start
    j = mid + 1
    aux = []

    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            aux.append(arr[i])
            i += 1
        else:
            aux.append(arr[j])
            j += 1

    # gather phase
    while i <= mid:
        aux.append(arr[i])
        i += 1
    while j <= end:
        aux.append(arr[j])
        j += 1

    # store in original array
    for idx, num in enumerate(aux):
        arr[start + idx] = num

    return


# solution from IK
def merge_sort(arr):
    msort(arr, 0, len(arr) - 1)
    return arr


def msort(arr, start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    msort(arr, start, mid)
    msort(arr, mid + 1, end)
    i = start
    j = mid + 1
    mlist = []
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            mlist.append(arr[i])
            i += 1
        elif arr[j] < arr[i]:
            mlist.append(arr[j])
            j += 1

    # gather phase
    while i <= mid:
        mlist.append(arr[i])
        i += 1
    while j <= end:
        mlist.append(arr[j])
        j += 1

    arr[start:end + 1] = mlist
