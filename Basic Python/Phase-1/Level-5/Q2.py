"""Take three numbers and check if they can form a Pythagorean triplet."""


def checkTriplet(a,b,c):
    largest = max(a,b,c)

    if largest == a:
        x,y =b,c
    elif largest == b:
        x,y = a,c
    elif largest == c:
        x,y=a,b


    if largest ** 2 == x ** 2 + y ** 2:
        print("Pythagorean Triplet")
    else:
        print("Not a ythagorean Triplet")


checkTriplet(3, 4, 5)
checkTriplet(5, 12, 13)
checkTriplet(2, 3, 4)
