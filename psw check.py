import re

def check_password_strength(password):
    score = 0

    # Length Check
    if len(password) >= 8:
        score += 1

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1

    # Number Check
    if re.search(r"\d", password):
        score += 1

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Strength Evaluation
    if score <= 2:
        return "Weak Password 🔴"
    elif score == 3 or score == 4:
        return "Moderate Password 🟡"
    else:
        return "Strong Password 🟢"


def main():
    print("=" * 40)
    print("      PASSWORD STRENGTH CHECKER")
    print("=" * 40)

    password = input("Enter your password: ")

    result = check_password_strength(password)

    print("\nPassword Analysis:")
    print(f"Strength: {result}")

    print("\nSuggestions:")
    
    if len(password) < 8:
        print("- Use at least 8 characters.")

    if not re.search(r"[A-Z]", password):
        print("- Add uppercase letters.")

    if not re.search(r"[a-z]", password):
        print("- Add lowercase letters.")

    if not re.search(r"\d", password):
        print("- Add numbers.")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("- Add special characters.")

    print("\nThank you for using Password Strength Checker!")


if __name__ == "__main__":
    main()




