
arr = [4,2,1,3,5]
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
            print(arr)
        print('*'*30)

bubble_sort(arr)