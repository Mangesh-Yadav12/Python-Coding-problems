"""Print the sum of all odd numbers up to n."""

def SumOfOdd(n):
    total = 0
    for i in range(1,n+1):
        if i%2 != 0:
            total += i

    return total

print(SumOfOdd(99))