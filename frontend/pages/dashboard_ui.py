import streamlit as st
from backend.dao.data_fetcher import DataFetcher
from frontend.dashboard.details import DetailsView
from frontend.dashboard.metrics import MetricsView

st.set_page_config(page_title="Dashboard", layout="wide")

class Dashboard:
    def __init__(self):
        self.fetcher = DataFetcher()

    def display_dashboard(self):
        st.title("Interactive Dashboard")

        df_metrics = self.fetcher.fetch_metrics()

        tab1, tab2 = st.tabs(["Details", "Metrics"])

        with tab1:
            DetailsView(self.fetcher).render()

        with tab2:
            MetricsView(df_metrics).render()

Dashboard().display_dashboard()
