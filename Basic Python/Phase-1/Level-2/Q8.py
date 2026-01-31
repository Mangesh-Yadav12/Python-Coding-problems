"""Take an alphabet character and check if it lies between ‘a’ and ‘m’ or ‘n’ and ‘z’. """

def chechAlphabet(ch:str):
    ch = ch.lower()
    if ch >= "a" and ch <= "m":
        print("Char lies between a to m")
    elif ch >= "n" and ch <= "z":
        print("Char lies between n to z")


chechAlphabet("g")
chechAlphabet("o")