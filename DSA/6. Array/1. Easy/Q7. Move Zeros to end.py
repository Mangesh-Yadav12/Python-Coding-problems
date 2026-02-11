"""Move Zeros to end"""

def moveZeros(nums):
    n = len(nums)
    if n == 1:
        return
    
    i = 0
    while i < n:
        if nums[i] == 0:
            break
        i += 1
    else:
        return
    j = i + 1
    while j < n:
        if nums[j] != 0:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
        j += 1

nums = [0,1,0,3,12]
moveZeros(nums)
print(nums)