"""Take a password string and check basic rules (length ≥ 8 and contains at least one digit)."""

def checkPassword(password):
    has_digit = False

    for ch in password:
        if ch.isdigit():
            has_digit = True
            break

    if len(password) >= 8 and has_digit:
        print("valid Password")
    else:
        print("Invalid Password")


checkPassword("45fghjkdfgh")
checkPassword("oiuytredcghj")