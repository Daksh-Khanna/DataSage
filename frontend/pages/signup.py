# frontend/pages/signup.py
import streamlit as st
import requests
import base64
from config import API_KEY, API_BASE_URL

headers = {"Authorization": f"Bearer {API_KEY}"}

class SignupPage:
    def render(self):
        st.set_page_config(layout="centered")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            with st.container():
                email = st.text_input("Email", key="signup_email")
                password = st.text_input("Password", type="password", key="signup_password")
                confirm_password = st.text_input("Confirm Password", type="password", key="signup_confirm_password")
                face_image = st.camera_input("Capture Your Face", key="signup_face")

                if st.button("Sign Up",type="primary", use_container_width=True):
                    if not all([email, password, confirm_password, face_image]):
                        st.warning("All fields are required.")
                        return

                    if password != confirm_password:
                        st.error("❌ Passwords do not match.")
                        return

                    try:
                        image_bytes = face_image.getvalue()
                        image_b64 = base64.b64encode(image_bytes).decode("utf-8")

                        response = requests.post(f"{API_BASE_URL}/auth/signup", json={
                            "email": email,
                            "password": password,
                            "role": "user",
                            "face_image_base64": image_b64
                        },headers=headers
                        )

                        if response.status_code == 200:
                            st.success("✅ Account created successfully. You can now log in.")
                        else:
                            st.error(f"❌ Failed: {response.json().get('detail', 'Unknown error')}")

                    except Exception as e:
                        st.error(f"❌ Exception occurred: {e}")

SignupPage().render()