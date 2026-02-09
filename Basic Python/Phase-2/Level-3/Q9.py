"""Print first n terms of an arithmetic progression (a, d)."""

def printAp(a,d,n):
    for i in range(n):
        term = a + i*d
        print(term,end=" ")

printAp(2,3,10)