"""Check if an amount can be evenly divided into 2000, 500, and 100 currency notes."""

def checkAmount(amt):
    if amt % 100 == 0:
        print("Amount can be evenly divided into 2000, 500, and 100 notes")
    else:
        print("Amount cannot be evenly divided into these notes")



checkAmount(1500)
checkAmount(2350)
checkAmount(80)
