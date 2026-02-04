"""Print N times with Recursion"""

def printGFG(n):
    if n == 0:
        return
    printGFG(n-1)
    print("GFG",end= " ")

printGFG(7)