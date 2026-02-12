"""Maximum Consecutive Ones"""

def maxOnes(nums):
    n = len(nums)

    count = 0
    maxi = 0

    for i in range(0,n):
        if nums[i] == 1:
            count += 1
        else:
            maxi = max(maxi,count)
            count = 0
    return max(maxi,count)

nums = [1,1,0,1,1,1]
print(maxOnes(nums))