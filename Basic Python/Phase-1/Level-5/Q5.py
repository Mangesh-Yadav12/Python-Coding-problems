"""Take three numbers and check if they are in arithmetic progression."""

def checkAp(a,b,c):
    if 2*b == a + c:
        print("Numbers are in Arithmetic Progression")
    else:
        print("Numbers are not in Arithmetic Progression")

checkAp(2, 4, 6)
checkAp(3, 6, 9)
checkAp(1, 3, 5)
checkAp(2, 5, 9)
