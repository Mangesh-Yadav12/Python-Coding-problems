"""Take a character and check whether it’s uppercase, lowercase, a digit, or a special character."""

def checkchar(ch: str):
    if ch.isupper():
        print("uppercase")
    elif ch.islower():
        print("lower")
    elif ch.isdigit():
        print("Digit")
    else:
        print("Special character")

checkchar("A")
checkchar("b")
checkchar("12")
checkchar("$")