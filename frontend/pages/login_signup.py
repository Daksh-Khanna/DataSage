import streamlit as st
from frontend.pages.login import LoginPage
from frontend.pages.signup import SignupPage

tab1, tab2 = st.tabs(["🔐 Login", "📝 Sign Up"])

with tab1:
    LoginPage().render()
with tab2:
    SignupPage().render()