# frontend/pages/admin.py
import streamlit as st
import pandas as pd
import base64
from backend.auth.user_manager_db import UserManagerDB

class AdminPage:
    def __init__(self):
        self.user_manager = UserManagerDB()

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
                            try:
                                self.user_manager.add_user(email, password, role, face_image)
                                st.success(f"✅ User {email} onboarded as {role}.")
                            except Exception as e:
                                st.error(f"❌ Failed to add user: {e}")

        with tab_view:

            users = self.user_manager.get_all_users_full()
            if not users:
                st.info("No users found.")
                return

            df = pd.DataFrame(users, columns=["id", "email", "role", "image_path"])

            # Convert image_path to base64 data URLs
            def img_to_data_url(path):
                data = open(path, "rb").read()
                b64 = base64.b64encode(data).decode("utf-8")
                return f"data:image/png;base64,{b64}"

            df["photo"] = df["image_path"].apply(img_to_data_url)

            # Display dataframe with inline photos
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