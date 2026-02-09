"""print all numbers between a and b divisible by 7."""

def printNumbers(a,b):
    for i in range(a,b+1):
        if i%7 == 0:
            print(i)


printNumbers(234,933)