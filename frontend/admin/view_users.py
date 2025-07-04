# frontend/admin/view_users.py
import streamlit as st
import pandas as pd
import requests
import base64
from config import API_KEY, API_BASE_URL

headers = {"Authorization": f"Bearer {API_KEY}"}

class ViewUsersTab:
    def render(self):
        try:
            response = requests.get(f"{API_BASE_URL}/admin/users", headers=headers)
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
