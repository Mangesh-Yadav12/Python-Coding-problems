"""Take a character and check if its a vowel or consonant."""

def checkChar(char):
    char = char.lower()
    if char in "aeiou":
        print("Vowel")
    else:
        print("Consonant")

    


checkChar("a")
checkChar("b")