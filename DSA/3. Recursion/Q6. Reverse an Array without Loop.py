"""Reverse an Array without Loop"""

def func(arr,l,r):
    if l >= r:
        return
    arr[l],arr[r] = arr[r],arr[l]
    func(arr,l+1,r-1)
    return arr
arr= [9,2,3,4,5,4,3,2,3,4,5,6,6]
print(func(arr,3,7))


def function(arr,l,r):
    l = 0
    r = len(arr)-1
    while l >= r:
        break
    arr[l],arr[r] = arr[r],arr[l]
    l += 1
    r -= 1
    return arr    

arr= [9,2,3,4,5,4,3,2,3]
print(function(arr,0,8))