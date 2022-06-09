def partition(l, r, arr):

    pivot, ptr = arr[r], l
    for i in range(l, r):
        if arr[i] <= pivot:

            arr[i], arr[ptr] = arr[ptr], arr[i]
            ptr += 1
            print(arr)

    arr[ptr], arr[r] = arr[r], arr[ptr]

    return ptr


def quicksort(l, r, arr):
    if len(arr) == 1:
        return arr

    if l < r:
        pivot = partition(l, r, arr)
        quicksort(l, pivot - 1, arr)
        quicksort(pivot + 1, r, arr)
    return arr


example = [4, 5, 1, 2, 3]
result = [1, 2, 3, 4, 5]
print(quicksort(0, len(example) - 1, example))