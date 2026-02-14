"""Longest Consecutive Sequence in an Array"""

def longestConsecutive(nums):
    n = len(nums)
    mySet = set()

    for i in range(0,n):
        mySet.add(nums[i])

    longest = 0
    for num in mySet:
        if num-1 not in mySet:
            x = num
            count = 1
            while x + 1 in mySet:
                count += 1
                x += 1
            longest = max(longest,count)
    return longest

nums = [0,3,7,2,5,8,4,6,0,1]

print(longestConsecutive(nums))