# frontend/pages/admin.py
import streamlit as st
from frontend.admin.onboard_users import OnboardUserTab
from frontend.admin.view_users import ViewUsersTab

class AdminPage:
    def render(self):
        st.set_page_config(layout="wide")
        tab_onboard, tab_view = st.tabs(["➕ Onboard User", "📋 View Users"])

        with tab_onboard:
            OnboardUserTab().render()

        with tab_view:
            ViewUsersTab().render()

AdminPage().render()
