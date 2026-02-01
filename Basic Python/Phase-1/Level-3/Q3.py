"""Take a 4-digit number and check if the first and last digits are equal."""


def checkFirstLastEqual(num):
    num = abs(num)

    if num < 1000 and num > 9999:
        print("Not a 4-digit number")
        return
    
    first = num // 1000
    last = num % 10

    if first == last:
        print("First and last digit are equal")
    else:
        print("Both are not equal")


checkFirstLastEqual(1221)
checkFirstLastEqual(3456)