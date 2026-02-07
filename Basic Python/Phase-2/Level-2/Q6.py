"""Check if a number is a perfect number."""

def perfectNumber(n):

    if n <= 1:
        print("Not a perfect number")

    total = 0

    for i in range(1,n):
        if n%i == 0:
            total += i

    if total == n:
        print("Its a perfect number")
    else:
        print("Not a perfect number")

perfectNumber(6)