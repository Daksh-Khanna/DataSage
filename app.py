import streamlit as st

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

# 3) Render navigation in the sidebar and run the selected page
selected_page = st.navigation(pages, position="sidebar", expanded=True)
selected_page.run()