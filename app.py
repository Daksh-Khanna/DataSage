import streamlit as st
from frontend.pages.login import LoginPage
from frontend.pages.signup import SignupPage
from frontend.pages.dashboard_ui import DashboardPage
from frontend.pages.chat import ChatPage
from frontend.pages.admin import AdminPage

# Initialize session
# Initialize all session keys safely
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "role" not in st.session_state:
    st.session_state.role = None
if "email" not in st.session_state:
    st.session_state.email = None


if st.session_state.authenticated:
    if st.sidebar.button("🚪 Logout"):
        st.session_state.clear()
        st.rerun()

if not st.session_state.authenticated:
    tab1, tab2 = st.tabs(["🔐 Login", "📝 Sign Up"])

    login_success = False
    with tab1:
        login_success = LoginPage().render()

    with tab2:
        SignupPage().render()

    if not login_success:
        st.stop()


# Role-based rendering
role = st.session_state.role

if role == "user":
    pages = [
    st.Page(
        "frontend/pages/dashboard_ui.py",
        title="Dashboard",
        icon="📊",
		default=True
        ),
    st.Page(
        "frontend/pages/chat.py",
        title="Chat with AI",
        icon="💬",
        ),
    ]
    selected_page = st.navigation(pages, position="sidebar", expanded=True)
    selected_page.run()

elif role == "admin" or role == "super_admin":
    AdminPage().render()
else:
    st.error("🚫 Unknown role.")
