def selectionsort(arr):
    n = len(arr)

    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if arr[min] > arr[j]:
                min = j
        print('Pass ',i+1,':')
        print(arr)
        arr[i], arr[min] = arr[min], arr[i]
    return


selectionsort([5,1,4,2,3])