"""Remove duplicates from Sorted array"""

def removeDuplicates(nums):
    n = len(nums)
    if n == 1:
        return 1
    
    i = 0
    j = i + 1
    while j < n:
        if nums[j] != nums[i]:
            i += 1
            nums[i],nums[j] = nums[j],nums[i]
        j += 1
    return i + 1

nums = [1,1,2,3,3,4,4,5,6,7,8,8,9,10]
print(removeDuplicates(nums))