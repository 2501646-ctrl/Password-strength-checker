# Password Strength Checker

🔗 **Live Demo:** [Click here]((https://password-strength-checker-rbijbsfb7k3xqmjjxsamco.streamlit.app/))

A password strength analyzer built in Python that checks:
- Character variety (uppercase, lowercase, numbers, symbols)
- Entropy (mathematical randomness in bits)
- Common/breached password detection

## Features
- Real-time strength scoring (Weak/Moderate/Strong)
- Entropy-based analysis, not just character rules
- Flags commonly used passwords even if they look complex

## Tech Stack
Python, Streamlit, Regex, Math (entropy calculation)

## How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## What I Learned
This project taught me how real password security works — entropy calculations, common attack patterns, and why "complex-looking" passwords can still be weak if they're commonly used.
