"""Take two angles of a triangle and compute the third angle."""

def findThridAngle(a,b):
    if a > 0 and b > 0 and a + b < 180:
        third = 180 - (a+b)
        print("Third Angle is :",third)
    else:
        print("Invalid Triangle")


findThridAngle(45,90)
findThridAngle(90,90)