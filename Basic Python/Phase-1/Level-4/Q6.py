"""Take two numbers and check if both are positive and their sum is less than 100."""

def checkSum(a,b):
    if a > 0 and b > 0:
        c = a + b
        if c < 100:
            print("yes")
        else:
            print("no")
    else:
        print("Negative number")


checkSum(34,56)
checkSum(45,87)
checkSum(-23,89)