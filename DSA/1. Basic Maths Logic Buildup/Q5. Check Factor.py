"""Check factor"""

from math import sqrt

def checkfactor(num):
    count = 0
    result = []

    for i in range(1,int(sqrt(num))+1):
        if num%i == 0:
            result.append(i)
            count += 1
            if num//i != i:
                result.append(num//i)
                count += 1
    result.sort()
    return count," Factors: " ,result


print(checkfactor(36))