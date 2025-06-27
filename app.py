import streamlit as st
from frontend.page_config import get_pages_for_role


# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.email = None
    st.session_state.role = "guest"

def create_navigation_pages():
    # if user is authenticated, get authorized pages based on role; else get public pages
    role = st.session_state.role if st.session_state.authenticated else "guest"
    page_configs = get_pages_for_role(role)
    pages = []
    for page in page_configs:
        #func = getattr(page_funcs, page["func_name"])
        pages.append(st.Page(page["path"], title=page["title"], icon=page["icon"]))
    return pages

# Build navigation
pages = create_navigation_pages()
selected = st.navigation(pages, position="sidebar", expanded=True)
# Run the selected page
selected.run()

