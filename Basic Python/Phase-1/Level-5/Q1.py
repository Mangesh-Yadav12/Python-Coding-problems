"""Take coordinates (x, y) and check if the point lies on the X-axis, Y-axis, or at the origin"""

def checkPosition(x,y):
    if x ==0 and y == 0:
        print("At the origin")
    elif x == 0:
        print("y-axis")
    elif y == 0:
        print("x-axis")
    else:
        print("point is not in any axis")


checkPosition(0, 0)
checkPosition(0, 5)
checkPosition(4, 0)
checkPosition(3, 2)
