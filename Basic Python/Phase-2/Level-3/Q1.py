""" Print the squares of numbers from 1 to n."""

def printSquares(n):
    for i in range(1,n+1):
        print(f"{i}² = {i**2}")

printSquares(10)