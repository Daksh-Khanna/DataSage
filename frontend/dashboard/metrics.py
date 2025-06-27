import streamlit as st

class MetricsView:
    def __init__(self, df_metrics):
        self.df = df_metrics

    def render(self):
        st.subheader("Session Metrics",divider="grey")

        latest = self.df.iloc[-1]
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
            st.bar_chart(self.df.set_index("date")[["active_users"]])
        with r1c2:
            st.subheader("Active Sessions")
            st.bar_chart(self.df.set_index("date")[["active_sessions"]])
        with r2c1:
            st.subheader("Total Questions")
            st.bar_chart(self.df.set_index("date")[["total_questions"]])
        with r2c2:
            st.subheader("Questions Per Session")
            st.line_chart(self.df.set_index("date")[["questions_per_session"]])
