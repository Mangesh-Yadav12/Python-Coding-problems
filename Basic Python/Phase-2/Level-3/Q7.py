"""Find the sum of all factors of a number."""
from math import sqrt
def findfactor(n):
    factor = 0
    for i in range(1,int(sqrt(n))+1):
        if n%i == 0:
            factor += i
            if n//i != i:
                factor += i

    print(factor)

findfactor(36)