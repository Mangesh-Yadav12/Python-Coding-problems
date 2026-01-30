"""Take marks (0–100) and print the corresponding grade (A/B/C/D/F)."""

def checkGrade(n):
    if n < 100 and n > 85:
        print("Grade A")
    elif n <= 85 and n > 70:
        print("Grade B")
    elif n<= 70 and n > 55:
        print("Grade C")
    elif n <= 55 and n >= 40:
        print("Grade D")
    elif n < 40 and n > 0:
        print("Grade F")
    else:
        print("Please Enter proper marks")

checkGrade(98)
checkGrade(70)
checkGrade(76)
checkGrade(44)
checkGrade(32)
checkGrade(101)