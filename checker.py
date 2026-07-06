import re
import math

def load_common_passwords():
    try:
        with open('common_passwords.txt', 'r') as f:
            return set(line.strip().lower() for line in f)
    except FileNotFoundError:
        return set()


def check_password_strength(password):
    common_passwords = load_common_passwords()
    score = 0
    feedback = []

    # Common password check
    if password.lower() in common_passwords:
        feedback.append("⚠️ This is a commonly used password — very easy to guess!")

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password too short (use at least 8 characters, 12+ recommended)")

    # Entropy calculation
    charset_size = 0
    if re.search(r'[a-z]', password):
        charset_size += 26
    if re.search(r'[A-Z]', password):
        charset_size += 26
    if re.search(r'[0-9]', password):
        charset_size += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        charset_size += 32

    entropy = len(password) * math.log2(charset_size) if charset_size > 0 else 0

    # Character variety checks
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add numbers")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add special characters (!@#$%^&* etc.)")

    # Rating based on score
    if password.lower() in common_passwords:
        rating = "Weak"
    elif score <= 2:
        rating = "Weak"
    elif score <= 4:
        rating = "Moderate"
    else:
        rating = "Strong"

    return rating, score, feedback, entropy


# Test it
if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    rating, score, feedback, entropy = check_password_strength(pwd)

    print(f"\nStrength: {rating} (Score: {score}/6)")
    print(f"Entropy: {entropy:.2f} bits")

    if feedback:
        print("\nSuggestions:")
        for tip in feedback:
            print(f"- {tip}")