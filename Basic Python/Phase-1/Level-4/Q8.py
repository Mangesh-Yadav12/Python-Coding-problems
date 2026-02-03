"""Take a weekday number (1–7) and determine if it is a weekday or weekend."""

def checkday(num):
    if num > 0 and num <=5:
        print("Weekday")
    elif num == 6 or num == 7:
        print("Weekend")
    else:
        print("Wrong input")


checkday(7)
checkday(4)