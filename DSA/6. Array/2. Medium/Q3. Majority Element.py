"""Majority Element """

def majorElement(nums):
    me = float("-inf")
    votes = 0
    for num in nums:
        if votes == 0:
            me = num
            votes = 1
        else:
            if me == num:
                votes += 1
            else:
                votes -= 1

    return me

nums = [2,2,1,1,1,2,2]
print(majorElement(nums))
