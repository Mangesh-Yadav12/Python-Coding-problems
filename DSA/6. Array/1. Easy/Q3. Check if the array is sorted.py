"""Check if the array is sorted"""

def isSorted(arr):
    n = len(arr)

    for i in range(0,n-1):
        if arr[i] > arr[i+1]:
            return False
        
    return True

arr = [1,2,3,4,5,6]
print(isSorted(arr))

print("----------------------------------")

arr = [1,2,3,2,1]
print(isSorted(arr))