"""Check if a number is prime or not."""

from math import sqrt
def isNotPrime(n):
    fac = 0
    for i in range(1,int(sqrt(n))+1):
        if n%i == 0:
            fac += 1
            if n//i != i:
                fac += 1

    if fac == 2:
        print("Is a Prime Nunber")
    else:
        print("Not a prime number")


isNotPrime(17)