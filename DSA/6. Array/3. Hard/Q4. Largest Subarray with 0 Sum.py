"""Largest Subarray with 0 Sum"""

def maxLength(arr):
    n = len(arr)
    prefixSum = {}
    maxi = 0
    summ = 0
    for i in range(n):
        summ += arr[i]
        if summ == 0:
            maxi = i + 1
        else:
            if summ in prefixSum:
                maxi = max(maxi, i - prefixSum[summ])
            else:
                prefixSum[summ] = i
    return maxi

arr = [15, -2, 2, -8, 1, 7, 10, 23]

print(maxLength(arr))