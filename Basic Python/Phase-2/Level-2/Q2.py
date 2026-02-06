"""Print the reverse of a given number."""

def reverseDigit(n):
    num = n
    result = 0
    while num > 0:
        ld = num%10
        result = (result * 10) + ld
        num = num//10
    return result
print(reverseDigit(123456))
