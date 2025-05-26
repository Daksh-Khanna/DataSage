import streamlit as st
import pandas as pd
from backend.data_fetcher import fetch_details
from backend.data_fetcher import fetch_metrics


def show_ui():
    st.set_page_config(page_title="Dashboard",layout="wide")
    st.title("Interactive Dashboard")

    # Fetch data
    df_details = fetch_details()
    df_metrics = fetch_metrics()

    tab1,tab2=st.tabs({"Details","Metrics"})

    with tab1:
        st.subheader("Session Details")
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
            operator_filter = st.selectbox("Select Operator Code", [""] + list(df_details["Operator"].unique()), key="operator_filter")
            email_filter = st.selectbox("Select User Email", [""] + list(df_details["Email"].unique()), key="email_filter")
            system_status_filter = st.selectbox("Select System Status", [""] + list(df_details["System Status"].unique()), key="system_status_filter")
            user_feedback_filter = st.selectbox("Select User Feedback", [""] + list(df_details["User Feedback"].unique()), key="user_feedback_filter")
            # 🔹 Create two columns for buttons (side by side)
            col1, col2 = st.columns(2)

            with col1:
                apply_filters = st.button("Apply")

            with col2:
                reset_filters = st.button("Reset")

        # Apply filters only when "Apply" is clicked
        if apply_filters:
            if date_range:
                df_details = df_details[(df_details["Date Time"] >= pd.to_datetime(date_range[0])) & (df_details["Date Time"] <= pd.to_datetime(date_range[1]))]
            if operator_filter:
                df_details = df_details[df_details["Operator"] == operator_filter]
            if email_filter:
                df_details = df_details[df_details["Email"] == email_filter]
            if system_status_filter:
                df_details = df_details[df_details["System Status"] == system_status_filter]
            if user_feedback_filter:
                df_details = df_details[df_details["User Feedback"] == user_feedback_filter]
        
        if reset_filters:
            st.session_state.clear()  # Clears all stored values
            st.rerun()  # Refresh the app to reset filters
        
        #Always Show the Table Without Resetting Filters
        st.dataframe(df_details, hide_index=True, use_container_width=True)
    
    with tab2:
        st.subheader("Session metrics")
        latest_metrics = df_metrics.iloc[-1]
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("Active Operators", latest_metrics["Active Operators"])
        col2.metric("Active Users", latest_metrics["Active Users"])
        col3.metric("Active Sessions", latest_metrics["Active Sessions"])
        col4.metric("Total Questions", latest_metrics["Total Questions"])
        col5.metric("Questions Per Session", latest_metrics["Questions Per Session"])

        st.subheader("Daily Trends")
        row1_col1, row1_col2 = st.columns(2)
        row2_col1, row2_col2 = st.columns(2)

        with row1_col1:
            st.subheader("Active Users")
            st.bar_chart(df_metrics.set_index("Date")[["Active Users"]])

        with row1_col2:
            st.subheader("Active Sessions")
            st.bar_chart(df_metrics.set_index("Date")[["Active Sessions"]])

        with row2_col1:
            st.subheader("Total Questions")
            st.bar_chart(df_metrics.set_index("Date")[["Total Questions"]])

        with row2_col2:
            st.subheader("Questions Per Session")
            st.line_chart(df_metrics.set_index("Date")[["Questions Per Session"]])