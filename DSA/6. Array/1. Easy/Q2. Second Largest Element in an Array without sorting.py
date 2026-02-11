"""Second Largest Element in an Array without sorting"""

def secondLargestElement(arr):
    largest = float("-inf")
    s_largest = float("-inf")
    n = len(arr)

    for i in range(0,n):
        if arr[i] > largest:
            s_largest = largest
            largest = arr[i]
        elif arr[i] > s_largest and arr[i] != largest:
            s_largest = arr[i]

    return [s_largest]

arr = [23,434,556,6,778,8,98,9,9123]
print(secondLargestElement(arr))