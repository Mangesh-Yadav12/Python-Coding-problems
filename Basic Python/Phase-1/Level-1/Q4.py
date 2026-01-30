"""Check if a number is divisible by both 3 and 5"""

def divisibleBy5and3(n):
    if n%5==0 and n%3==0:
        print(f"Number {n} is divisible by both 5 and 3")


divisibleBy5and3(15)
