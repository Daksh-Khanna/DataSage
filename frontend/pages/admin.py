# frontend/pages/admin.py
import streamlit as st
import pandas as pd
import requests
import base64

API_BASE_URL = "http://localhost:8000/admin"  # Change if using ngrok

class AdminPage:
    def render(self):
        st.set_page_config(layout="wide")
        tab_onboard, tab_view = st.tabs(["➕ Onboard User", "📋 View Users"])

        with tab_onboard:
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
                            # Convert image to base64
                            face_bytes = face_image.getvalue()
                            image_base64 = base64.b64encode(face_bytes).decode("utf-8")

                            payload = {
                                "email": email,
                                "password": password,
                                "role": role,
                                "face_image_base64": image_base64
                            }

                            try:
                                response = requests.post(f"{API_BASE_URL}/add_user", json=payload)
                                if response.status_code == 200:
                                    st.success(f"✅ User {email} onboarded as {role}.")
                                else:
                                    st.error(f"❌ Failed: {response.json().get('detail', response.text)}")
                            except Exception as e:
                                st.error(f"❌ Error: {e}")

        with tab_view:
            try:
                response = requests.get(f"{API_BASE_URL}/users")
                if response.status_code == 200:
                    users = response.json()
                else:
                    st.error("Failed to fetch users.")
                    return
            except Exception as e:
                st.error(f"Error fetching users: {e}")
                return

            if not users:
                st.info("No users found.")
                return

            df = pd.DataFrame(users)

            # Convert image_path to base64 inline images
            def img_to_data_url(path):
                try:
                    with open(path, "rb") as f:
                        b64 = base64.b64encode(f.read()).decode("utf-8")
                        return f"data:image/png;base64,{b64}"
                except:
                    return None

            df["photo"] = df["image_path"].apply(img_to_data_url)

            st.dataframe(
                df[["id", "email", "role", "photo"]],
                use_container_width=True,
                hide_index=True,
                column_config={
                    "photo": st.column_config.ImageColumn(
                        "Photo", width="small", help="User face image"
                    )
                },
            )

AdminPage().render()
