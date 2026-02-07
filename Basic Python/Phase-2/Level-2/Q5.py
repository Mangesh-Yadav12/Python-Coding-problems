"""Check if a number is an Armstrong number."""

def armstrong(n):
    num = n
    result = 0
    nod = len(str(n))
    while num > 0:
        ld = num%10
        result += (ld**nod)
        num = num//10
    return n == result

print(armstrong(153))