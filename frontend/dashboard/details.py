import streamlit as st
import pandas as pd
from frontend.dashboard.sidebar import SidebarFilters

class DetailsView:
    def __init__(self, fetcher):
        self.fetcher = fetcher

    def render(self):
        df_details = self.fetcher.fetch_details()

        filter_ui = SidebarFilters(df_details)
        (
            date_range,
            operator_filter,
            email_filter,
            system_status_filter,
            user_feedback_filter,
            apply_filters,
            reset_filters,
        ) = filter_ui.render()

        filters = {}
        if apply_filters:
            if date_range and len(date_range)==2:
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

        st.subheader("Session Details")
        st.dataframe(display_df, hide_index=True, use_container_width=True)
