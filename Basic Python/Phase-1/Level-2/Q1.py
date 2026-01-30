"""Take three sides and check if they form a valid triangle."""

def checkTriangle(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        print("Valid")
    else:
        print("Invalid")


checkTriangle(3,4,5)
checkTriangle(1,2,3)