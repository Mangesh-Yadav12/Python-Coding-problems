"""If the sides form a valid triangle, determine whether it is equilateral, isosceles, or scalene."""

def triangleType(a,b,c):
    if a + b > c and a + c > b and c + b > a:
        if a == b == c:
            print("equilateral triangle")
        elif a == b or b == c or c == a:
            print("isosceles triangle")
        else:
            print("scalene triangle")
    else:
        print("Not valid")


triangleType(3,3,3)
triangleType(3,4,4)
triangleType(3,4,5)
triangleType(1,2,3)