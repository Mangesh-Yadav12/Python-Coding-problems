"""Armstrong Number"""

def ArmstrongNumber(n):
    nod = len(str(n))
    num = n
    result = 0

    while num > 0:
        lastDigit = num%10
        result = result + (lastDigit**nod)
        num = num//10
    
    return n == result

print(ArmstrongNumber(153))