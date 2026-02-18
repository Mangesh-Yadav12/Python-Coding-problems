"""Majority Element II"""

def majorityElement(nums):
    if not nums:
        return []
    
    maxEle1 = maxEle2 = None
    count1 = count2= 0

    for num in nums:
        if num is not None and num == maxEle1:
            count1 += 1
        elif num is not None and num == maxEle2:
            count2 += 1
        elif count1 == 0:
            maxEle1 = num
            count1 = 1
        elif count2 == 0:
            maxEle2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1
    
    result = []
    threshold = len(nums)//3

    if maxEle1 is not None:
        if nums.count(maxEle1) > threshold:
            result.append(maxEle1)

    if maxEle2 is not None:
        if nums.count(maxEle2) > threshold:
            result.append(maxEle2)

    return result


nums = [3,2,3]
print(majorityElement(nums))