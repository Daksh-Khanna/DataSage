# frontend/pages/login.py
import streamlit as st
import requests
import base64

API_URL = "http://localhost:8000"  # Replace with ngrok/public URL when deployed

class LoginPage:
    def render(self):
        st.set_page_config(layout="centered")
        with st.container():
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.title("Login")

                email = st.text_input("Email", key="login_email")
                password = st.text_input("Password", type="password", key="login_password")
                face_image = st.camera_input("Capture your face", key="login_face")

                if st.button("Login", type="primary", use_container_width=True):
                    if not all([email, password, face_image]):
                        st.warning("Please complete all fields.")
                        return

                    try:
                        # Encode face image to base64
                        image_b64 = base64.b64encode(face_image.getvalue()).decode("utf-8")

                        # Send login request
                        response = requests.post(f"{API_URL}/auth/login", json={
                            "email": email,
                            "password": password,
                            "face_image_base64": image_b64
                        })

                        if response.status_code == 200:
                            data = response.json()
                            st.session_state.authenticated = True
                            st.session_state.email = data["email"]
                            st.session_state.role = data["role"]

                            st.success(f"✅ Welcome {data['role']}: {data['email']}")
                            st.rerun()
                        else:
                            st.error(f"❌ {response.json().get('detail', 'Login failed')}")

                    except Exception as e:
                        st.error(f"❌ Exception: {e}")

# Render the login page
LoginPage().render()
