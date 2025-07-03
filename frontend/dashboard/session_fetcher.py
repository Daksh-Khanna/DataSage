# backend/dao/data_fetcher_api.py

import requests
import pandas as pd

API_BASE = "http://localhost:8000"  # or ngrok URL if tunneling

class DataFetcherAPI:
    def fetch_metrics(self):
        res = requests.get(f"{API_BASE}/session/metrics")
        res.raise_for_status()
        data = res.json()
        return pd.DataFrame(data)

    def fetch_details(self, filters=None):
        params = {}
        if filters:
            if "start_date" in filters:
                params["start_date"] = filters["start_date"].strftime("%Y-%m-%d")
            if "end_date" in filters:
                params["end_date"] = filters["end_date"].strftime("%Y-%m-%d")
            if "operator" in filters:
                params["operator"] = filters["operator"]
            if "email" in filters:
                params["email"] = filters["email"]
            if "system_status" in filters:
                params["system_status"] = filters["system_status"]
            if "user_feedback" in filters:
                params["user_feedback"] = filters["user_feedback"]

        res = requests.get(f"{API_BASE}/session/details", params=params)
        res.raise_for_status()
        data = res.json()
        return pd.DataFrame(data)
