import streamlit as st

# 1) Page config
st.set_page_config(page_title="AI Support", layout="wide")

# 2) Define pages
pages = [
    st.Page(
        "frontend/pages/dashboard.py",
        title="Dashboard",
        icon="📊",
    ),
    st.Page(
        "frontend/pages/chat.py",
        title="Chat with AI",
        icon="💬",
        default=True,         # makes this the initially selected page
    ),
]

# 3) Render navigation in the sidebar and run the selected page
selected_page = st.navigation(pages, position="sidebar", expanded=True)
selected_page.run()