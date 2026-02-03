"""Take a single digit (0–9) and print its word form (“Zero” to “Nine”)."""

def printWord(num):
    nums = {
        0:"Zero", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five",
        6:"Six", 7:"Seven", 8: "Eight", 9:"Nine"
    }

    print(nums.get(num,"Invalid number"))


printWord(6)