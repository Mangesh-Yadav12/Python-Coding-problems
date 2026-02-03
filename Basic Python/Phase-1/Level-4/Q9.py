"""Take electricity units consumed and calculate the bill as per slabs (using if-else)."""

def calculateBill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = (units * 5) + (units - 100) * 7
    else:
        bill = (units * 5) + (100 * 7 ) + (units - 200) * 10

    print("Electricity bill:", bill)


calculateBill(456)