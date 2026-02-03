"""Frequency count"""

def frequencyCount(arr):
    n = len(arr)

    freq = [0] * n 
    for num in arr:
        if num <= 1 or num <= n:
            freq[num -1] += 1
    
    return freq

arr = [2,3,4,5,6,7,8,9,9,8,7,6,5,4,4,3,2,3,4,5]
print(frequencyCount(arr))