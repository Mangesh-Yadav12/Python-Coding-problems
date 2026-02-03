"""Take three numbers and print the median value (neither maximum nor minimum)."""

def medianValue(a,b,c):
    if (a > b and a < c) or (a < b and a > c):
        print("Median value:", a)
    elif (b > a and b < c ) and (b < a and b > c):
        print("Median value:", b)
    else:
        print("Median Value:", c)

    
medianValue(5,8,9)
medianValue(4,5,3)
medianValue(9,7,8)