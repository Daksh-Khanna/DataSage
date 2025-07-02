import streamlit as st
import requests
from frontend.chat.display_history import DisplayHistory
from utils.logger import get_logger

logger = get_logger("chat_logger", "chat.log")

API_URL = "http://localhost:8000/chat/query"  # Change this if deployed

class ChatPage:
    def __init__(self):
        logger.info("Chatbot initialized")

    def render(self):
        st.set_page_config(layout="centered")
        st.subheader("💬 Chat with AI", divider="grey")
        DisplayHistory().render()

        if prompt := st.chat_input("Ask a question..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").markdown(prompt)

            try:
                # Send prompt to FastAPI
                response = requests.post(API_URL, json={"prompt": prompt})

                if response.status_code != 200:
                    raise Exception(response.json().get("detail", "Unknown error"))

                data = response.json()
                logger.info(f"Generated SQL: {data['sql']}")

                # Display results
                df_columns = data["columns"]
                df_rows = data["rows"]

                import pandas as pd
                df = pd.DataFrame(df_rows, columns=df_columns)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": df
                })

                with st.chat_message("assistant"):
                    st.dataframe(df, use_container_width=False)

            except Exception as e:
                error_msg = f"❌ Error: {e}"
                logger.error(error_msg)
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_msg
                })
                with st.chat_message("assistant"):
                    st.error(error_msg)

ChatPage().render()
