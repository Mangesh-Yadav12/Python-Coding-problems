"""Largest Element in an Array"""

def LargestElement(arr):
    max_num = arr[0]

    for num in arr:
        if num > max_num:
            max_num = num

    return max_num


arr = [23,434,556,6,778,8,98,9,9123]

print(LargestElement(arr))