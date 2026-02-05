"""Print the sum of first n natural numbers."""

def sumNaturalNunber(n):
    total = 0
    for i in range(1,n+1):
        total += i
    print(total)

sumNaturalNunber(9)