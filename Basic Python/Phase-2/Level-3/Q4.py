"""find HCF (GCD) of two numbers using loops."""


def findHCF(a,b):
    x = a
    y = b
    while y != 0:
        x,y = y , x%y
    print("HCF = ",x)

findHCF(34,98)