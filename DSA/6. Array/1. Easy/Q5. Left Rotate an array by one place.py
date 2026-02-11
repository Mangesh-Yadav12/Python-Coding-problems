"""Left Rotate an array by one place"""

def rotateByone(nums):
    n = len(nums)
    temp = nums[n-1]
    for i in range(n-2,-1,-1):
        nums[i+1] = nums[i]
    nums[0] = temp

    return nums

nums = [1,2,1,2,3,4,4,3,3,2,2,1,3,4,5]
print(rotateByone(nums))