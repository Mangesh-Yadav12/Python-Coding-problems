"""Take two numbers and print the larger one"""

def largerNumber(a, b):
    if a > b:
        print(f"larger number is {a}")
    elif b > a:
        print(f"larger number is {b}")
    else:
        print("both number are equal")

largerNumber(10, 20)
largerNumber(30, 15)
largerNumber(5, 5)