"""Print all prime numbers between 1 and 100."""

def checkPrime():
    for num in range(2,101):
        isPrime = True
        for i in range(2,num):
            if num%i == 0:
                isPrime = False

        if isPrime:
            print(num,end=" ")


checkPrime()