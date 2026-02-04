"""Take day and month and check if it forms a valid calendar date (ignoring leap years)."""

def checkDate( day,month):
    if month < 1 and month > 12:
        print("Invalid Month")
        return
    
    if month in [1,3,5,7,8,10,12]:
        maxDay = 31
    elif month in [4,6,9,11]:
        maxDay = 30
    elif month == 2:
        maxDay = 28

    if day >= 1 and day <= maxDay:
        print("Valid Date")
    else:
        print("Invaild Date")


checkDate(15, 6)
checkDate(31, 4)
checkDate(29, 2)
