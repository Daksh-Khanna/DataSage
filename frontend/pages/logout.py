# frontend/pages/logout.py
import streamlit as st

class LogoutPage:
    def __init__(self):
        """Initialize the LogoutPage"""
        pass

    def render(self):
        """Render the logout page and handle logout logic"""
        st.session_state.clear()
        st.session_state.authenticated = False
        st.success("You have been logged out successfully!")
        st.rerun()

LogoutPage().render()