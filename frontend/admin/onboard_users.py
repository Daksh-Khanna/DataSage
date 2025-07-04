# frontend/admin/onboard_users.py
import streamlit as st
import requests
import base64
from config import API_KEY, API_BASE_URL

headers = {"Authorization": f"Bearer {API_KEY}"}

class OnboardUserTab:
    def render(self):
        with st.container():
            col1, col2, col3 = st.columns([2, 2, 2])
            with col2:
                email = st.text_input("New User Email", key="admin_email")
                password = st.text_input("Password", type="password", key="admin_password")
                role = st.selectbox("Select Role", ["user", "admin"], key="admin_role")
                face_image = st.camera_input("Capture User's Face", key="admin_face")

                if st.button("Add User"):
                    if not all([email, password, face_image]):
                        st.warning("All fields are required.")
                    else:
                        face_bytes = face_image.getvalue()
                        image_base64 = base64.b64encode(face_bytes).decode("utf-8")

                        payload = {
                            "email": email,
                            "password": password,
                            "role": role,
                            "face_image_base64": image_base64
                        }

                        try:
                            response = requests.post(
                                f"{API_BASE_URL}/admin/add_user",
                                json=payload,
                                headers=headers
                            )
                            if response.status_code == 200:
                                st.success(f"✅ User {email} onboarded as {role}.")
                            else:
                                st.error(f"❌ Failed: {response.json().get('detail', response.text)}")
                        except Exception as e:
                            st.error(f"❌ Error: {e}")
