"""Print all odd numbers between 1 and 100."""

def printOdd():
    for i in range(1,101):
        if i%2 != 0:
            print(i,end=" ")


printOdd()