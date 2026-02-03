"""Take 24-hour time (hours and minutes) and print whether it is AM or PM."""

def hours(time:float):
    if time < 0 or time > 24:
        print("Wrong input")
    elif time > 0 and time <= 12:
        print("AM")
    else:
        print("PM")


hours(22)
hours(9)
hours(54)