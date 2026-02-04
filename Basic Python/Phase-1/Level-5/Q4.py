"""4. Take time (hours and minutes) and print the smaller angle between the hour and minutes hands"""

def findAngle(hr, mints):
    if hr < 0 or hr > 12 or mints < 0 or mints > 59:
        print("Invalid Angle")
        return
    
    if hr == 12:
        hr = 0

    hr_Angle = (hr*30) + (hr*0.5)
    min_angle = mints * 6

    angle = abs(hr_Angle-min_angle)

    small_angle = min(angle,360 - angle)

    print(small_angle)

findAngle(3, 30)
findAngle(12, 0)
findAngle(6, 0)
