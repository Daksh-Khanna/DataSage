import streamlit as st
import pandas as pd
from backend.assistant.sql_assistant.sql_generator import generate_sql
from backend.dao.db_connector import DBConnector
from utils.logger import get_logger

logger = get_logger("chat_logger", "chat.log")

class ChatPage:
    def __init__(self):
        logger.info("Chatbot initialized")
        if "messages" not in st.session_state:
            st.session_state.messages = []

    def render(self):
        st.title("💬 Chat with AI")

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                if isinstance(msg["content"], pd.DataFrame):
                    st.dataframe(msg["content"])
                else:
                    st.markdown(msg["content"])

        if prompt := st.chat_input("Ask a question..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").markdown(prompt)

            try:
                sql_query = generate_sql(prompt)
                logger.info(f"Generated SQL: {sql_query}")

                db = DBConnector()
                with db.get_connection() as conn:
                    df = pd.read_sql(sql_query, conn)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": df
                })

                with st.chat_message("assistant"):
                    st.dataframe(df)

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