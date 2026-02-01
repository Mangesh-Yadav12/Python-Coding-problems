"""Check if a number is a multiple of 7 or ends with 7."""

def checkSeven(num):
    if num%7==0 or abs(num)%10 == 7:
        print("a number is a multiple of 7 or ends with 7")
    else:
        print("Neither number is a multiple of 7 or ends with 7")


checkSeven(21)
checkSeven(27)
checkSeven(45)