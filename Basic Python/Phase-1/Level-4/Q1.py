"""
Take a character and check if it is a letter, a digit, or neither
"""

def isChar(chr:str):
    if chr.isalpha():
        print("Letter")
    elif chr.isdigit():
        print("Digit")
    else:
        print("Neither Letter or Digit")


isChar("q")
isChar("a")
isChar("@")