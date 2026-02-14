"""Rearrange Array Elements by Sign"""

def rearrangeArray(nums):
    n = len(nums)
    result = [0] * n
    posIndex = 0
    negIndex = 1

    for i in range(0,n):
        if nums[i] >= 0:
            result[posIndex] = nums[i]
            posIndex += 2
        else:
            result[negIndex] = nums[i]
            negIndex += 2
    return result

nums = [3,1,-2,-5,2,-4]
print(rearrangeArray(nums))