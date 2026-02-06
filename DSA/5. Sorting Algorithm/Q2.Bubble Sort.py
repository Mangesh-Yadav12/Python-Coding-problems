"""Bubble Sort"""

def bubbleSort(num):
    n = len(num)

    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if num[j]> num[j+1]:
                num[j],num[j+1] = num[j+1],num[j]

    return num

num = [3,2,4,5,6,7,8,6,5,4]

print(bubbleSort(num))