"""Take an integer (1–9999) and check if the sum of its digits is greater than the product
of its digits."""

def checkSumProduct(num):
    num = abs(num)

    if num < 1 or num > 10000:
        print("Number must be in between 1 - 9999")
        return
    
    total = 0
    product = 1
    while num > 0:
        ld = num%10
        total += ld
        product *= ld
        num = num//10

    if total > product:
        print("Sum of digits is greater than product")
    else:
        print("Sum of digits is not greater than product")


checkSumProduct(123)
checkSumProduct(105)
checkSumProduct(39)
