def binary_search(arr, key):
    start = 0
    end = len(arr) - 1
    while(start <= end):
        mid = (start + end) // 2
        if(arr[mid] > key):
            end = mid - 1
        elif(arr[mid] < key):
            start = mid + 1
        else:
            return mid
    return

arr = [5,3,4,1,2]
key = 4

print(binary_search(arr,key))