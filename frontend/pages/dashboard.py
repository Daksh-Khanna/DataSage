import streamlit as st
import pandas as pd
from backend.dao.data_fetcher import DataFetcher
from utils.logger import get_logger

logger = get_logger("ui_logger", "ui.log")

class dashboard:
    def __init__(self):
        self.fetcher = DataFetcher()
        logger.info("UI initialized")

    def display_dashboard(self):
        st.title("Interactive Dashboard")

        df_details = self.fetcher.fetch_details()
        df_metrics = self.fetcher.fetch_metrics()

        tab1, tab2 = st.tabs(["Details", "Metrics"])

        self._show_details_tab(tab1, df_details)
        self._show_metrics_tab(tab2, df_metrics)

    def _show_details_tab(self, container, df_details):
        with container:
            st.subheader("Session Details")

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
                
                date_range = st.date_input(
                    "Select Date Range", 
                    st.session_state["date_range"]
                )

                operator_filter = st.selectbox(
                    "Select Operator Code", 
                    [""] + list(df_details["operator_code"].unique()),  # Changed from "Operator"
                    key="operator_filter"
                )
                email_filter = st.selectbox(
                    "Select User Email",
                    [""] + list(df_details["user_email"].unique()),  # Changed from "Email"
                    key="email_filter"
                )
                system_status_filter = st.selectbox(
                    "Select System Status", 
                    [""] + list(df_details["system_status"].unique()),  # Changed from "System Status"
                    key="system_status_filter"
                )
                user_feedback_filter = st.selectbox(
                    "Select User Feedback", 
                    [""] + list(df_details["user_status"].unique()),  # Changed from "User Feedback"
                    key="user_feedback_filter"
                )
                col1, col2 = st.columns(2)
                apply_filters = col1.button("Apply")
                reset_filters = col2.button("Reset")

            filters = {}
            if apply_filters:
                if date_range and len(date_range) == 2:
                    filters["start_date"] = pd.to_datetime(date_range[0])
                    filters["end_date"] = pd.to_datetime(date_range[1])
                if operator_filter:
                    filters["operator"] = operator_filter
                if email_filter:
                    filters["email"] = email_filter
                if system_status_filter:
                    filters["system_status"] = system_status_filter
                if user_feedback_filter:
                    filters["user_feedback"] = user_feedback_filter
                
                df_details = self.fetcher.fetch_details(filters)
            else:
                df_details = self.fetcher.fetch_details()

            if reset_filters:
                st.session_state.clear()
                st.rerun()

            display_df = df_details.rename(columns={
                "start_time_utc": "Date Time",
                "user_email": "Email",
                "operator_code": "Operator",
                "question": "Question",
                "system_status": "System Status",
                "user_status": "User Feedback",
                "response_time": "Response Time"
            })

            st.dataframe(display_df, hide_index=True, use_container_width=True)

    def _show_metrics_tab(self, container, df_metrics):
        with container:
            st.subheader("Session Metrics")
            latest = df_metrics.iloc[-1]
            col1, col2, col3, col4, col5 = st.columns(5)
            col1.metric("Active Operators", latest["active_operators"])
            col2.metric("Active Users", latest["active_users"])
            col3.metric("Active Sessions", latest["active_sessions"])
            col4.metric("Total Questions", latest["total_questions"])
            col5.metric("Questions Per Session", latest["questions_per_session"])

            st.subheader("Daily Trends")
            r1c1, r1c2 = st.columns(2)
            r2c1, r2c2 = st.columns(2)

            with r1c1:
                st.subheader("Active Users")
                st.bar_chart(df_metrics.set_index("date")[["active_users"]])
            with r1c2:
                st.subheader("Active Sessions")
                st.bar_chart(df_metrics.set_index("date")[["active_sessions"]])
            with r2c1:
                st.subheader("Total Questions")
                st.bar_chart(df_metrics.set_index("date")[["total_questions"]])
            with r2c2:
                st.subheader("Questions Per Session")
                st.line_chart(df_metrics.set_index("date")[["questions_per_session"]])


dashboard().display_dashboard()