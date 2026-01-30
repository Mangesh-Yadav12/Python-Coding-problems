"""check if one of two given numbers is a multiple of the other."""

def checkMultiple(a,b):
    if a%b == 0 or b%a == 0:
        print("One number is a multiple of the other")
    else:
        print("Neither number is a multiple of the other")

checkMultiple(2,4)
checkMultiple(3,7)