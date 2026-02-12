"""Find missing number in an array"""

def missingNumber(nums):
    n = len(nums)
    orignalTotal = (n*(n+1))//2
    return orignalTotal - sum(nums)


nums = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums))