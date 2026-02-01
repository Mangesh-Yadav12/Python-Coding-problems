"""Take a 3-digit number and check if all digits are distinct."""

def checkUniqueNumber(num):
    if num < 100 or num > 999:
        print("Not a 3 digit number")
        return

    a = num // 100
    b  = (num // 10)%10
    c = num%10

    if a != b and a != c and c != b:
        print("All digits are distinct.")
    else:
        print("Digits are not distinct")


checkUniqueNumber(123)
checkUniqueNumber(121)
checkUniqueNumber(99)