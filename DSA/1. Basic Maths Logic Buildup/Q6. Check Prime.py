"""Check Prime"""

from math import sqrt
def isPrime(n):
    factor = 0

    for i in range(1,int(sqrt(n))+1):
        if n%i == 0:
            factor += 1
            if n//i != i:
                factor += 1

    if factor == 2:
        return True
    else:
        return False
    

print(isPrime(36))
print(isPrime(7))