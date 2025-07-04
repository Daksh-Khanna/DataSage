import streamlit as st
from frontend.dashboard.session_fetcher import DataFetcherAPI
from frontend.dashboard.details import DetailsView
from frontend.dashboard.metrics import MetricsView

class DashboardPage:
    def __init__(self):
        self.fetcher = DataFetcherAPI()  # updated

    def render(self):
        st.set_page_config(layout="wide")

        df_metrics = self.fetcher.fetch_metrics()

        tab1, tab2 = st.tabs(["Details", "Metrics"])

        with tab1:
            DetailsView(self.fetcher).render()

        with tab2:
            MetricsView(df_metrics).render()

DashboardPage().render()
