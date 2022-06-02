

def three_num_sum(arr, target):
    c,b = {},{}
    a = 0
    for i in range(len(arr)):
        if arr[i] not in c.keys():
            if (target-arr[i])>0:
                c[target-arr[i]]=i
        else:
            a = target-arr[i-1]
    num1 = list(c.keys())
    for i in range(len(num1)):
        for j in range(len(arr)):
            if arr[j] not in b.keys() and num1[i]-arr[j]>0:
                b[num1[i]-arr[j]] = j
            else:
                #print(num1)
                #print(b)
                temp =num1[i]-arr[j-1]
                return [temp,arr[j-1],(target-temp-arr[j-1])]
arr = [1,2,3,4,5,6,7,8]
target = [17,19,15,9,6]
for i in target:
    print(three_num_sum(arr,i))