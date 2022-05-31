arr = [1,2,3,4,5]
target = 4
num={}
def TwoNum(arr, target):
    for i in range(len(arr)):
        if arr[i] not in num.keys():
            num[target-arr[i]]=i
        else:
            print(num)
            return [target-arr[i],arr[i]]
print(TwoNum(arr,target))