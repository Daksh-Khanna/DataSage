import streamlit as st
from backend.dao.data_fetcher import DataFetcher
from frontend.dashboard.details import DetailsView
from frontend.dashboard.metrics import MetricsView

class DashboardPage:
    def __init__(self):
        self.fetcher = DataFetcher()

    def render(self):
        
        st.title("📊 Interactive Dashboard")

        df_metrics = self.fetcher.fetch_metrics()

        tab1, tab2 = st.tabs(["Details", "Metrics"])

        with tab1:
            DetailsView(self.fetcher).render()

        with tab2:
            MetricsView(df_metrics).render()

DashboardPage().render()