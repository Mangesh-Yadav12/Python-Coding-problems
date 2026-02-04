"""Take three numbers and check if they are in geometric progression."""

def checkGp(a,b,c):
    if a!= 0 and b!= 0:
        if (b/a) == (c/b):
            print("The numbers are in Geometric Progression (GP).")
        else:
            print("The numbers are NOT in Geometric Progression.")
    else:
        print("Cannot check GP because division by zero is not allowed.")


checkGp(2,6,18)