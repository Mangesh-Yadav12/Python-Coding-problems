"""Merge 2 sorted Arrays"""

def mergeArray(a,b):
    n = len(a)
    m = len(b)

    result = []

    i = 0
    j = 0

    while i < n and j < m:
        if a[i] <= b[j]:
            if len(result) == 0 or result[-1] != a[i]:
                result.append(a[i])
            i += 1
        else:
            if len(result) == 0 or result[-1] != b[j]:
                result.append(b[j])
            j += 1

    while i < n:
        if len(result) == 0 or result[-1] != a[i]:
            result.append(a[i])
        i += 1
    
    while j < m:
        if len(result) == 0 or result[-1] != b:
            result.append(b[j])
        j += 1
    
    return result

a = [1, 2, 3, 4, 5]
b= [1, 2, 3, 6, 7]

print(mergeArray(a,b))