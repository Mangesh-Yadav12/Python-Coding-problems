"""Print the sum of all even numbers up to n."""

def SumOfEven(n):
    total = 0
    for i in range(1,n+1):
        if i%2 == 0:
            total += i

    print(total)

SumOfEven(67)