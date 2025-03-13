import re
import streamlit as st

# Page Configuration
st.set_page_config(page_title="Password Strength Checker", layout="centered")

# Custom Styling
st.markdown("""
<style>
   .main {text-align: center;}
   .stTextInput {width: 60% !important; margin: auto;}
   .stButton button {width: 50%; background-color: #4CAF50; color: white; font-size: 18px;}
   .stButton button:hover { background-color: #45a049;}
</style>
""", unsafe_allow_html=True)

# Title
st.title("Password Strength Checker")
st.write("Enter your password below to check its security level.")

# Password Input Field (Moved Outside the Function)
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong")

# Password Strength Checker Function
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be **at least 8 characters long**.")

    # Uppercase & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    # Numeric Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password should include **at least one number (0-9)**.")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Include **at least one special character (!@#$%^&*)**.")

    # Strength Feedback
    if score == 4:
        st.success("**Strong Password** - Your Password is secure.")
    elif score == 3:
        st.info("**Moderate Password** - Consider improving security by adding more features.")
    else:
        st.error("**Weak Password** - Follow the suggestions below to strengthen it.")

    # Display Suggestions
    if feedback:
        with st.expander("**Improve Your Password**"):
            for item in feedback:
                st.write(item)

# Button to Check Password Strength (Moved Outside the Function)
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("Please enter a password first!")
