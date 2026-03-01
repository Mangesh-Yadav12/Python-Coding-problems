"""Merge two sorted arrays without extra space"""

def merge(a,b):
    n = len(a)
    m = len(b)
    left = n-1
    right = 0

    while left >= 0 and right < m:
        if a[left] > b[right]:
            a[left],b[right] = b[right],a[left]
            left -= 1
            right += 1
        else:
            break

    a.sort()
    b.sort()


a = [1, 5, 9, 10, 15, 20]
b = [2, 3, 8, 13]
merge(a,b)
print(a,b)