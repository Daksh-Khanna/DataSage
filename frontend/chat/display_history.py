# frontend/chat/methods/display_history.py
import streamlit as st
import pandas as pd

class DisplayHistory:
    def __init__(self):
        if "messages" not in st.session_state:
            st.session_state.messages = []

    def render(self):
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                if isinstance(msg["content"], pd.DataFrame):
                    st.dataframe(msg["content"])
                else:
                    st.markdown(msg["content"])
