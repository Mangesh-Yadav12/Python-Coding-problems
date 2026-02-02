"""Check whether a number is a perfect square (without using the square root function)."""

def isSquare(num):
    if num < 0:
        print("Not perfect Square")
        return
    
    i = 0
    while i * i <= num:
        if i * i == num:
            print("Is perfect Square")
            return
        i += 1

    print("Not perfect Square")


isSquare(25)
isSquare(36)
isSquare(20)
