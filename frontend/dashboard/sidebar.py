import streamlit as st

class SidebarFilters:
    def __init__(self, df_details):
        self.df = df_details
        self.filters = {}

    def render(self):
        with st.sidebar:
            st.header("Filter Data")

            date_range = st.date_input(
            "Select Date Range", 
            st.session_state.get("date_range", [])
       		)

            operator_filter = st.selectbox(
                "Select Operator Code",
                [""] + list(self.df["operator_code"].unique()),
                key="operator_filter"
            )

            email_filter = st.selectbox(
                "Select User Email",
                [""] + list(self.df["user_email"].unique()),
                key="email_filter"
            )

            system_status_filter = st.selectbox(
                "Select System Status",
                [""] + list(self.df["system_status"].unique()),
                key="system_status_filter"
            )

            user_feedback_filter = st.selectbox(
                "Select User Feedback",
                [""] + list(self.df["user_status"].unique()),
                key="user_feedback_filter"
            )

            col1, col2 = st.columns(2)
            apply_filters = col1.button("Apply")
            reset_filters = col2.button("Reset")

        return (
            date_range,            
            operator_filter,
            email_filter,
            system_status_filter,
            user_feedback_filter,
            apply_filters,
            reset_filters,
        )
