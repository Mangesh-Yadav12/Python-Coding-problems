"""Print cubes of numbers from 1 to n."""

def printCubes(n):
    for i in range(1,n+1):
        print(f"{i}³ = {i**3}")

printCubes(10)