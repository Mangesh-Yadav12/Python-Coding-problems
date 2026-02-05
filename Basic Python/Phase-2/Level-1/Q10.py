"""Print the product of digits of a given number."""

def product(n):
    n = abs(n)
    result = 1
    if n == 0:
        return 0

    while n > 0:
        digit = n % 10
        result *= digit
        n = n // 10
    return result

print(product(899))
