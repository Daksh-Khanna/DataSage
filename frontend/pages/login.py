import streamlit as st
from backend.auth.user_manager_db import UserManagerDB
from backend.auth.face_authenticator import FaceAuthenticator

class LoginPage:
    def __init__(self):
        self.user_manager = UserManagerDB()
        self.face_auth = FaceAuthenticator()

    def render(self):
        st.title("🔐 Secure Login")

        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")
        face_image = st.camera_input("Capture your face", key="login_face")

        if "authenticated" not in st.session_state:
            st.session_state.authenticated = False
            st.session_state.email = None
            st.session_state.role = None

        if st.button("Login"):
            if not (email and password and face_image):
                st.warning("Please complete all fields.")
                return False

            user = self.user_manager.authenticate(email, password)
            if not user:
                st.error("❌ Invalid email or password.")
                return False

            match = self.face_auth.verify(face_image, user["image_path"])
            if not match:
                st.error("❌ Face not recognized.")
                return False

            # ✅ Login success
            st.session_state.authenticated = True
            st.session_state.email = user["email"]
            st.session_state.role = user["role"]
            st.success(f"✅ Welcome {user['role']}: {user['email']}")
            st.rerun()
            return True

        return False