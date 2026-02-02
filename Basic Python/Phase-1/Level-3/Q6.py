"""Take coordinates (x, y) and determine which quadrant the point lies in"""

def findQuadrant(x,y):
    if x > 0 and y > 0:
        print("Quadrant-I")
    elif x < 0 and y > 0:
        print("Quadrant-II")
    elif x < 0 and y < 0:
        print("Quadrant-III")
    elif x > 0 and y < 0:
        print("Quadrant-IV")
    elif x ==0 and y == 0:
        print("Orignal")
    elif x == 0:
        print("Y-Axis")
    else:
        print("X-Ais")

findQuadrant(3, 4)
findQuadrant(-2, 5)
findQuadrant(-3, -6)
findQuadrant(0, 7)
