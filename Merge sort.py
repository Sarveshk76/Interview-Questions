arr = [5,3,4,2,1]
def merge_sort(arr):
    l,r = [],[]
    n = len(arr)
    if n>1:
        mid = n//2
        l = arr[:mid]
        r = arr[mid:]
        merge_sort(l)
        print(l)
        merge_sort(r)
        print(r)

    i,j,k = 0,0,0
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            arr[k] = l[i]
            i+=1
        else:
            arr[k] = r[j]
            j+=1
        k+=1
    while i<len(l):
        arr[k] = l[i]
        i+=1
        k+=1

    while j<len(r):
        arr[k] = r[j]
        j+=1
        k+=1

    return l,r,arr
print(merge_sort(arr))