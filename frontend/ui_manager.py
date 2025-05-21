import streamlit as st
import pandas as pd
from backend.data_fetcher import fetch_combined_data

def show_ui():
    st.set_page_config(layout="wide")
    st.title("Processed Session Data")

    # Fetch data
    df = fetch_combined_data()

    # Initialize session state for filters
    if "date_range" not in st.session_state:
        st.session_state["date_range"] = []
    if "operator_filter" not in st.session_state:
        st.session_state["operator_filter"] = None
    if "email_filter" not in st.session_state:
        st.session_state["email_filter"] = None
    if "system_status_filter" not in st.session_state:
        st.session_state["system_status_filter"] = None
    if "user_feedback_filter" not in st.session_state:
        st.session_state["user_feedback_filter"] = None

    with st.sidebar:
        st.header("Filter Data")

        # Date Range Filter
        date_range = st.date_input("Select Date Range", st.session_state["date_range"])

        # Dropdowns (Preserving values using session_state keys)
        operator_filter = st.selectbox("Select Operator Code", [""] + list(df["Operator"].unique()), key="operator_filter")
        email_filter = st.selectbox("Select User Email", [""] + list(df["Email"].unique()), key="email_filter")
        system_status_filter = st.selectbox("Select System Status", [""] + list(df["System Status"].unique()), key="system_status_filter")
        user_feedback_filter = st.selectbox("Select User Feedback", [""] + list(df["User Feedback"].unique()), key="user_feedback_filter")
        # 🔹 Create two columns for buttons (side by side)
        col1, col2 = st.columns(2)

        with col1:
            apply_filters = st.button("Apply")

        with col2:
            reset_filters = st.button("Reset")

    # Apply filters only when "Apply" is clicked
    if apply_filters:
        if date_range:
            df = df[(df["Date Time"] >= pd.to_datetime(date_range[0])) & (df["Date Time"] <= pd.to_datetime(date_range[1]))]
        if operator_filter:
            df = df[df["Operator"] == operator_filter]
        if email_filter:
            df = df[df["Email"] == email_filter]
        if system_status_filter:
            df = df[df["System Status"] == system_status_filter]
        if user_feedback_filter:
            df = df[df["User Feedback"] == user_feedback_filter]
    
    if reset_filters:
        st.session_state.clear()  # Clears all stored values
        st.rerun()  # Refresh the app to reset filters
    
    #Always Show the Table Without Resetting Filters
    st.dataframe(df, hide_index=True, use_container_width=True)