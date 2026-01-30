"""Take a number and print whether it’s positive, negative, or zero."""

def checkNumber(n):
    if n > 0:
        print(f"Nunber {n} is Positive")
    elif n < 0:
        print(f"Number {n} is negative")
    else:
        print(f"Number {n} is Zero")


checkNumber(10)
checkNumber(0)
checkNumber(-8)
