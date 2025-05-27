import pandas as pd
from backend.db_connector import DBConnector
from backend.queries import QueryBuilder

class DataFetcher:
    def __init__(self):
        self.db = DBConnector()
        self.queries = QueryBuilder()

    def fetch_details(self):
        query = self.queries.get_detail_query()
        with self.db.get_connection() as conn:
            df = pd.read_sql(query, conn)
            df["System Status"] = df["System Status"].apply(lambda x: "Success" if x else "Failed")
        return df

    def fetch_metrics(self):
        query = self.queries.get_metrics_query()
        with self.db.get_connection() as conn:
            df = pd.read_sql(query, conn)
        return df
