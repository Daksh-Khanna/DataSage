import streamlit as st
from backend.auth.user_manager_db import UserManagerDB

class SignupPage:
    def __init__(self):
        self.user_manager = UserManagerDB()

    def render(self):
        st.set_page_config(layout="centered")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            with st.container():
                email = st.text_input("Email", key="signup_email")
                password = st.text_input("Password", type="password", key="signup_password")
                confirm_password = st.text_input("Confirm Password", type="password", key="signup_confirm_password")
                face_image = st.camera_input("Capture Your Face", key="signup_face")

                if st.button("Sign Up"):
                    if not all([email, password, confirm_password, face_image]):
                        st.warning("All fields are required.")
                        return

                    if password != confirm_password:
                        st.error("❌ Passwords do not match.")
                        return

                    try:
                        self.user_manager.add_user(email, password, "user", face_image)
                        st.success("✅ Account created successfully. You can now log in.")
                    except Exception as e:
                        st.error(f"❌ Failed to sign up: {e}")

SignupPage().render()