"""Check whether a given integer is single-digit, double-digit, or multi-digit."""

def checkInteger(num):
    num = abs(num)

    if num < 10:
        print("Single digit number")
    elif num > 9 and num < 100:
        print("Double digit number")
    else:
        print("Multi digit number")


checkInteger(99)
checkInteger(9)
checkInteger(876)