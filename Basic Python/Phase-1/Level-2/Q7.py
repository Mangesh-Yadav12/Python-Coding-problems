"""Take two numbers and determine whether both are even, both are odd, or one is even and one is odd."""

def checkNumbers(a, b):
    if a%2 == 0 and b%2 == 0:
        print("Both are Even")
    elif a%2 != 0 and b%2 != 0:
        print("Both are odd")
    else:
        print("one is even and one is odd.")


checkNumbers(12,18)
checkNumbers(12,17)
checkNumbers(13,17)