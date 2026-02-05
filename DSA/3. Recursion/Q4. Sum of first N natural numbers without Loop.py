"""Sum of first N natural numbers without Loop"""

def sumOfSeries(n):
    if n == 0:
        return 0
    return sumOfSeries(n-1) + n ** 3


print(sumOfSeries(5))