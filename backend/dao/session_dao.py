import pandas as pd
from .db_connector import DBConnector
from .session_query import SessionQueryBuilder

class DataFetcher:
    def __init__(self):
        self.db = DBConnector()

    def fetch_details(self, filters=None):
        filters = filters or {}
        query, params = SessionQueryBuilder.build_details_query(filters)
        with self.db.get_connection() as conn:
            df = pd.read_sql(query, conn, params=params)
        df["start_time_utc"] = pd.to_datetime(df["start_time_utc"])
        df["end_time_utc"] = pd.to_datetime(df["end_time_utc"])
        # Add Response Time column (based on raw timestamps)
        df["response_time"] = df["end_time_utc"] - df["start_time_utc"]

        # Format Response Time
        total_seconds = df["response_time"].dt.total_seconds().astype(int)
        df["response_time"] = total_seconds.apply(
            lambda s: f"{s} sec" if s < 60 
            else f"{s//60} min {s%60} sec"
        )        
        # Drop unnecessary column
        df = df.drop(columns=["end_time_utc"])

        # Format System Status from boolean to text
        df["system_status"] = df["system_status"].apply(lambda x: "Success" if x else "Failed")

        return df

    def fetch_metrics(self):
        query = SessionQueryBuilder.build_metrics_query()
        with self.db.get_connection() as conn:
            df = pd.read_sql(query, conn)
        return df
