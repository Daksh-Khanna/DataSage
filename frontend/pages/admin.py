import streamlit as st
from backend.auth.user_manager_db import UserManagerDB

class AdminPage:
    def __init__(self):
        self.user_manager = UserManagerDB()

    def render(self):
        st.title("🛠️ Admin Control Panel")

        st.subheader("➕ Onboard New User")
        email = st.text_input("New User Email", key="admin_email")  
        password = st.text_input("Password", type="password", key="admin_password")
        role = st.selectbox("Select Role", ["user", "admin"], key="admin_role")
        face_image = st.camera_input("Capture User's Face", key="admin_face")

        if st.button("Add User"):
            if not all([email, password, face_image]):
                st.warning("All fields are required.")
                return

            try:
                self.user_manager.add_user(email, password, role, face_image)
                st.success(f"✅ User {email} onboarded as {role}.")
            except Exception as e:
                st.error(f"❌ Failed to add user: {e}")

        st.subheader("📋 Registered Users")
        users = self.user_manager.get_all_users()
        for email, role in users:
            st.write(f"🔸 {email} — 🔐 {role}")
