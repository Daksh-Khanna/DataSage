import requests
import pandas as pd
from config import API_KEY, API_BASE_URL

headers = {"Authorization": f"Bearer {API_KEY}"}

class DataFetcherAPI:
    def fetch_metrics(self):
        res = requests.get(f"{API_BASE_URL}/session/metrics",headers=headers)
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

        res = requests.get(f"{API_BASE_URL}/session/details", params=params, headers=headers)
        res.raise_for_status()
        data = res.json()
        return pd.DataFrame(data)
