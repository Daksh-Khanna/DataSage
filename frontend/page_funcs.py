# frontend/page_funcs.py
from frontend.pages.login import LoginPage
from frontend.pages.signup import SignupPage
from frontend.pages.dashboard_ui import DashboardPage
from frontend.pages.chat import ChatPage
from frontend.pages.logout import LogoutPage
from frontend.pages.admin import AdminPage  # assuming you have this

def login_page():
    LoginPage().render()

def signup_page():
    SignupPage().render()

def dashboard_page():
    DashboardPage().render()

def chat_page():
    ChatPage().render()

def logout_page():
    LogoutPage().render()

def admin_page():
    AdminPage().render()
