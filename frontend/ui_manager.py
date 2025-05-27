import streamlit as st
import pandas as pd
from backend.data_fetcher import DataFetcher

class UIManager:
    def __init__(self):
        self.fetcher = DataFetcher()

    def display_dashboard(self):
        st.set_page_config(page_title="Dashboard", layout="wide")
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

                date_range = st.date_input("Select Date Range", st.session_state["date_range"])
                operator_filter = st.selectbox("Select Operator Code", [""] + list(df_details["Operator"].unique()), key="operator_filter")
                email_filter = st.selectbox("Select User Email", [""] + list(df_details["Email"].unique()), key="email_filter")
                system_status_filter = st.selectbox("Select System Status", [""] + list(df_details["System Status"].unique()), key="system_status_filter")
                user_feedback_filter = st.selectbox("Select User Feedback", [""] + list(df_details["User Feedback"].unique()), key="user_feedback_filter")

                col1, col2 = st.columns(2)
                apply_filters = col1.button("Apply")
                reset_filters = col2.button("Reset")

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
                st.session_state.clear()
                st.rerun()

            st.dataframe(df_details, hide_index=True, use_container_width=True)

    def _show_metrics_tab(self, container, df_metrics):
        with container:
            st.subheader("Session Metrics")
            latest = df_metrics.iloc[-1]
            col1, col2, col3, col4, col5 = st.columns(5)
            col1.metric("Active Operators", latest["Active Operators"])
            col2.metric("Active Users", latest["Active Users"])
            col3.metric("Active Sessions", latest["Active Sessions"])
            col4.metric("Total Questions", latest["Total Questions"])
            col5.metric("Questions Per Session", latest["Questions Per Session"])

            st.subheader("Daily Trends")
            r1c1, r1c2 = st.columns(2)
            r2c1, r2c2 = st.columns(2)

            with r1c1:
                st.subheader("Active Users")
                st.bar_chart(df_metrics.set_index("Date")[["Active Users"]])
            with r1c2:
                st.subheader("Active Sessions")
                st.bar_chart(df_metrics.set_index("Date")[["Active Sessions"]])
            with r2c1:
                st.subheader("Total Questions")
                st.bar_chart(df_metrics.set_index("Date")[["Total Questions"]])
            with r2c2:
                st.subheader("Questions Per Session")
                st.line_chart(df_metrics.set_index("Date")[["Questions Per Session"]])
