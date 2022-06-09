def insertion_sort(arr):

    for i in range(1, len(arr)):
        value = arr[i]
        j = i - 1
        while j >= 0 and value < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value
        print('pass: ',i)
        print(arr)

arr =[5,3,4,1,2]
insertion_sort(arr)