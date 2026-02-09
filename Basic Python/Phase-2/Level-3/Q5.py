"""Find LCM of two numbers using loops."""

def findLCM(a,b):
    max_num = max(a,b)
    lcm = max_num

    while True:
        if lcm%a == 0 and lcm%b == 0:
            break
        lcm += max_num

    print("LCM = ",lcm)

findLCM(12342,76543)