"""Check if a given year is a leap year"""

def leapYear(Year):
    if (Year % 4 == 0 ) or (Year % 400 == 0 and Year % 100 != 0):
        print(f"{Year} is a Leap Year")
    else:
        print(f"{Year} is not a Leap Year")


leapYear(2020)
leapYear(1900)