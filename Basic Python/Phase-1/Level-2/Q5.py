"""Take the hour of the day (0–23) and print “Good Morning”,“Good Afternoon”,“Good Evening”, or “Good Night”"""

def greeting(time):
    if time > 0 and time < 11.59:
        print("Good Morning")
    elif time > 12 and time < 15:
        print("Good Afternoon")
    elif time > 15 and time < 20:
        print("Good Evening")
    elif time > 20 and time < 23.59:
        print("Good Night")
    else:
        print("Wrong input")


greeting(10.15)
greeting(13)
greeting(17)
greeting(22.15)
greeting(65)
