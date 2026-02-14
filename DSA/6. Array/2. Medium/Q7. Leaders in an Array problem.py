"""Leaders in an Array problem"""

def leaders(arr):
    n = len(arr)
    result = []
    maxi = float("-inf")

    for i in range(n-1,-1,-1):
        if arr[i] >= maxi:
            result.append(arr[i])
            maxi = max(maxi,arr[i])

    result.reverse()
    return result

arr = [16, 17, 4, 3, 5, 2]
print(leaders(arr))