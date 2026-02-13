"""Two Sum"""

def twoSum(nums,target):
    n = len(nums)
    hashMap = dict()

    for i in range(n):
        remaining = target - nums[i]
        if remaining in hashMap:
            return [hashMap[remaining],i]
        hashMap[nums[i]] = i


nums = [2,7,11,15]
target = 9

print(twoSum(nums,target))