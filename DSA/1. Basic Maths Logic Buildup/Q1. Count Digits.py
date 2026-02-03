"""Count Digits"""

def countDigit(n):
    num = n
    count = 0

    while num > 0:
        lastDigit = num%10
        if lastDigit != 0 and n % lastDigit == 0:
            count += 1
        num = num//10
    return count


count = countDigit(345678)
print(count)