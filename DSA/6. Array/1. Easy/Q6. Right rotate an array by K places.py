"""Right rotate an array by K places"""

from math import gcd
def rotate(nums,d):
    n = len(nums)
    gcdValue = gcd(n,d%n)

    for i in range(gcdValue):
        temp = nums[i]
        j = i
        while True:
            k = (j-d)%n
            if k == i:
                break
            nums[j] = nums[k]
            j = k
        nums[j] = temp

    return nums

nums = [2,3,4,5,6,4,3,1,3,4,5,7,8,9,9,7,6,5,4,5,6,7,8]
print(rotate(nums,d=8))