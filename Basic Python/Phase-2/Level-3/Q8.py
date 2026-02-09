"""Check if a number is a strong number (sum of factorials of digits = number)."""

def strongNumber(n):
    temp = n
    result = 0

    while temp > 0:
        digit = temp % 10

        # Find factorial of digit
        fact = 1
        for i in range(1, digit + 1):
            fact *= i

        result += fact
        temp //= 10

    return result == n


num = 145

if strongNumber(num):
    print(num, "is a Strong Number")
else:
    print(num, "is NOT a Strong Number")
