"""Check voting eligibility for a given age (18+)."""

def eligibility(age:int):
    if age < 18:
        print("Sorry! You are under age.")
    elif age >= 18:
        print("You can Vote.")
    else:
        print("Worng input! Please enter a number.")


eligibility(16)
eligibility(28)
