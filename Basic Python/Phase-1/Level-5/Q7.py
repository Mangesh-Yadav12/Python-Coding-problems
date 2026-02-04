"""Take a 3-digit number and check if the sum of the first and last digit equals the middle
digit."""

def checkSum(a,b,c):
    if (a+c) == b:
        print("Yes")
    else:
        print("No")

checkSum(4,8,4)