import streamlit as st
from backend.chatbot import get_sql_from_perplexity, execute_sql_and_fetch_df
from utils.logger import get_logger

logger = get_logger("chat_logger", "chat.log")

class Chatbot:
    def __init__(self):
        logger.info("Chatbot initialized")
        if "messages" not in st.session_state:
            st.session_state.messages = []

    def display(self):
        st.title("Chat with AI")

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                # Check if the content is a DataFrame (or similar)
                if hasattr(msg["content"], 'to_html'):  # Check if it's a DataFrame
                    st.dataframe(msg["content"])
                else:
                    st.markdown(msg["content"])

        if prompt := st.chat_input("Ask a question..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").markdown(prompt)

            sql_query = get_sql_from_perplexity(prompt)
            response_df = execute_sql_and_fetch_df(sql_query)

            # Store both the DataFrame and a string representation
            st.session_state.messages.append({
                "role": "assistant", 
                "content": response_df,
                "type": "dataframe"  # Add a type identifier
            })
            with st.chat_message("assistant"):
                st.dataframe(response_df)


Chatbot().display()