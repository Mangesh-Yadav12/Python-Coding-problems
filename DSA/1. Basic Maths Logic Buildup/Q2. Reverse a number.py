"""Reverse a number"""

def reverse(num):
    num = abs(num)
    sign = -1 if num < 0 else 1

    ans = 0
    while num > 0:
        lastDigit = num%10
        ans = (ans * 10) + lastDigit
        num = num // 10
    ans *= sign

    return ans

rv = reverse(8764)
print(rv)