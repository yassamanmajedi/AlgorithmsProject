def insertion_sort(arr):
    for o in range(1, len(arr)):
        key = arr[o]
        p = o - 1
        while p >= 0 and arr[p] > key:
            arr[p + 1] = arr[p]
            arr[p] = key
            p -= 1

    return arr
