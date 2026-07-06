import streamlit as st
from checker import check_password_strength

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

st.title("🔒 Password Strength Checker")
st.write("Check how strong your password really is — beyond just length and symbols.")

password = st.text_input("Enter your password", type="password")

if password:
    rating, score, feedback, entropy = check_password_strength(password)

    # Color-coded strength display
    if rating == "Weak":
        st.error(f"Strength: {rating} (Score: {score}/6)")
    elif rating == "Moderate":
        st.warning(f"Strength: {rating} (Score: {score}/6)")
    else:
        st.success(f"Strength: {rating} (Score: {score}/6)")

    st.write(f"**Entropy:** {entropy:.2f} bits")

    # Progress bar for visual score
    st.progress(min(score / 6, 1.0))

    if feedback:
        st.subheader("Suggestions:")
        for tip in feedback:
            st.write(f"- {tip}")
    else:
        st.write("✅ No improvements needed — this is a strong password!")