""" Print first n terms of a geometric progression (a, r)."""

def printGP(a,r,n):
    term = a

    for i in range(n):
        print(term,end= " ")
        term = term * r

printGP(2, 3, 6)