arr = [1,2,3,4,5]
target = 4
num={}
def twosum(arr, target):
    for i in range(len(arr)):
        if arr[i] not in num.keys():
            num[target-arr[i]]=i
        else:
            print(num)
            return [target-arr[i],arr[i]]
print(twosum(arr,target))

#Using List Comprehension
def twoSum(self, nums: List[int], target: int) -> List[int]:
        res= [[i,j] for i in range(len(nums)-1) for j in range(i+1,len(nums)) if nums[i]+nums[j]==target]
        return res[0]
