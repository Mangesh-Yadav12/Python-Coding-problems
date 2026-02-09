"""Print all factors of a given number."""

from math import sqrt
def findFactor(n):
    factor = []
    for i in range(1,int(sqrt(n+1))):
        if n%i == 0:
            factor.append(i)
            if n//i != i:
                factor.append(n//i)

    factor.sort()
    return factor

print(findFactor(36))