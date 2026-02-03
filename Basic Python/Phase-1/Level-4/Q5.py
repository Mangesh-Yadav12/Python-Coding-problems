"""Take income and age, and check if eligible for tax (age > 18 and income > 5 L)."""

def eligible(age, income):
    if (age > 18 and income > 500000):
        print("Yes! you are eligible for tax")
    else:
        print("No! You are not eligible for tax")


eligible(16,987654)
eligible(45,3456782)