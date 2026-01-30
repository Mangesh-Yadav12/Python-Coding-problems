"""Take a temperature value and print "cold"“Warm”,, or “Hot” using range conditions."""

def checkTemp(temp):
    if temp < 20:
        print("cold")
    elif temp > 20 and temp < 30:
        print("warm")
    else:
        print("hot")


checkTemp(25)