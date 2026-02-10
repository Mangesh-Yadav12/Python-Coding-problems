"""Selection Sort"""

def selectionSort(num):
    n = len(num)

    for i in range(0,n):
        minIndex = i
        for j in range(i+1,n):
            if num[j] < num[minIndex]:
                minIndex = j
        num[i],num[minIndex] = num[minIndex],num[i]
    return num

num = [3,2,4,5,6,7,8,6,5,4]
print(selectionSort(num))