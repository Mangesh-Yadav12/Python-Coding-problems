"""Count the number of digits in a given number."""

def countDigit(digit):
    count = 0
    num = abs(digit)
    while num > 0:
        ld = num%10
        count += 1
        num = num // 10
    return count


print(countDigit(digit=12345))
