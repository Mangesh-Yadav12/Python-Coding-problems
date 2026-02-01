"""Take a 3-digit number and determine if the middle digit is the largest, smallest, or
neither."""

def checkMiddleDigit(num):
    num = abs(num)

    if num < 100 and num > 999:
        print("Not a 3-digit number")
        return
    
    first = num // 100
    middle = (num // 10) % 10
    last = num % 10

    if middle > first and middle > last:
        print("Middle is largest")
    elif middle < first and middle < last:
        print("Middle is smallest")
    else:
        print("Neither Middle is largest or smallest")


checkMiddleDigit(592)
checkMiddleDigit(183)
checkMiddleDigit(343)