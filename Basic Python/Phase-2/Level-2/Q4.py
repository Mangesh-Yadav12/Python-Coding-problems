"""Find the sum of digits of a number."""

def sumOfDigit(n):
    num = n
    result = 0
    while num > 0:
        ld = num%10
        result += ld
        num = num//10
    return result

print(sumOfDigit(1234))