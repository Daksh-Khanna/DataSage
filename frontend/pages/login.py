# frontend/pages/login.py
import streamlit as st
from backend.auth.user_manager_db import UserManagerDB
from backend.auth.face_authenticator import FaceAuthenticator

class LoginPage:
    def __init__(self):
        self.user_manager = UserManagerDB()
        self.face_auth = FaceAuthenticator()

    def render(self):
        st.set_page_config(layout="centered")
        with st.container():
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                email = st.text_input("Email", key="login_email")
                password = st.text_input("Password", type="password", key="login_password")
                face_image = st.camera_input("Capture your face", key="login_face")

                if st.button("Login", type="primary", use_container_width=True):
                    if not (email and password and face_image):
                        st.warning("Please complete all fields.")
                        return

                    user = self.user_manager.authenticate(email, password)
                    if not user:
                        st.error("❌ Invalid email or password.")
                        return

                    match = self.face_auth.verify(face_image, user["image_path"])
                    if not match:
                        st.error("❌ Face not recognized.")
                        return

                    st.session_state.authenticated = True
                    st.session_state.email = user["email"]
                    st.session_state.role = user["role"]
                    st.success(f"✅ Welcome {user['role']}: {user['email']}")
                    st.rerun()

LoginPage().render()