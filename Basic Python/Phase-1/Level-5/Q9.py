"""Take two dates (day and month) and determine which one comes first in the
calendar."""

def compareDates(d1, m1, d2, m2):

    if m1 < m2:
        print("First date comes before second date")
    elif m1 > m2:
        print("Second date comes before first date")

    else:
        if d1 < d2:
            print("First date comes before second date")
        elif d1 > d2:
            print("Second date comes before first date")
        else:
            print("Both dates are the same")

compareDates(12, 5, 20, 5)   
compareDates(10, 3, 5, 6)   
compareDates(15, 8, 15, 8) 
