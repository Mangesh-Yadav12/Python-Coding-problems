"""Print N to 1 without Loop"""

def printN(n):
    if n == 0:
        return
    print(n,end=" ")
    printN(n-1)


printN(6)