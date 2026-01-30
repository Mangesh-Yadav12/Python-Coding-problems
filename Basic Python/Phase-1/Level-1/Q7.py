"""Take three numbers and print the largest"""

def largerNumber(a, b ,c):
    if a >= b and a >= c:
        print(f"larger number is a: {a}")
    elif b >= a and b >= c:
        print(f"larger number is b: {b}")
    elif c >= a and c >= b:
        print(f"larger number is c: {c}")


largerNumber(10, 20, 30)
largerNumber(30, 15, 25)
largerNumber(5, 5, 2)