import streamlit as st

class SidebarFilters:
    def __init__(self, df_details):
        self.df = df_details

    def render(self):
        with st.sidebar:
            st.header("Filter Data")

            # Use temporary widget variables (not session_state) to prevent premature re-runs
            date_range = st.date_input(
                "Select Date Range", 
                value=[],
                key="date_range"
            )

            operator_filter = st.selectbox(
                "Select Operator Code",
                [""] + sorted(self.df["operator_code"].dropna().unique().tolist()),
                key="operator_filter"
            )

            email_filter = st.selectbox(
                "Select User Email",
                [""] + sorted(self.df["user_email"].dropna().unique().tolist()),
                key="email_filter"
            )

            system_status_filter = st.selectbox(
                "Select System Status",
                [""] + sorted(self.df["system_status"].dropna().unique().tolist()),
                key="system_status_filter"
            )

            user_feedback_filter = st.selectbox(
                "Select User Feedback",
                [""] + sorted(self.df["user_status"].dropna().unique().tolist()),
                key="user_feedback_filter"
            )

            col1, col2 = st.columns(2)
            apply_filters = col1.button("Apply", key="apply_filters_btn")
            reset_filters = col2.button("Reset", key="reset_filters_btn")

        return (
            date_range,
            operator_filter,
            email_filter,
            system_status_filter,
            user_feedback_filter,
            apply_filters,
            reset_filters,
        )
