"""Linear Search"""

def search(nums,x):
    for i in range(0,len(nums)):
        if nums[i] == x:
            return i
    return -1

nums = [1,2,3,2,1,34,55,66]
print(search(nums,66))