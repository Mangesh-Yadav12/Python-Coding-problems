"""Take a year and print the corresponding century (e.g.,“19th century”,“20th century”)"""

def findCentury(year):
    century = (year - 1)//100+1

    if century%10== 1 and century!= 11:
        suffix = "st"
    elif century%10 == 2 and century != 12:
        suffix ="nd"
    elif century%10 == 3 and century != 13:
        suffix = "rd"
    else:
        suffix = "th"

    print(f"{century} {suffix} century")


findCentury(1905)
findCentury(2000)
findCentury(2024)
findCentury(1701)