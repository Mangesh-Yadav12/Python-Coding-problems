"""Take a day number (1–7) and print the corresponding day name."""

def GetDayNumber(day):
    days = {
        1 : "Monday" , 2 : "Tuesday" , 3 : "Wednesday" , 
        4 : "Thursday" , 5 : "Friday" , 6 : "Saturday" , 7 : "Sunday"
    }
    print(days.get(day,"Invalid day number"))


GetDayNumber(6)
GetDayNumber(8)
