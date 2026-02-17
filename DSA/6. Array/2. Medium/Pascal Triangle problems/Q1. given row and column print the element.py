"""given row and column print the element row = 5, col = 3"""

def noColRow(n,r):
    result = 1
    for i in range(0,r):
        result = result * (n-1)
        result = result//(i+1)
    return result

print(noColRow(4,5))