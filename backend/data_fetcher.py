from backend.db_connector import get_db_connection
from backend.queries import get_query_detailstab
from backend.queries import get_query_metricstab
import pandas as pd


#fetching dataframe
def fetch_details():
    query = get_query_detailstab()
    with get_db_connection() as conn:
        df = pd.read_sql(query, conn)
        df["System Status"] = df["System Status"].apply(lambda x: "Success" if x else "Failed")
    return df

def fetch_metrics():
    query = get_query_metricstab()
    with get_db_connection() as conn:
        df=pd.read_sql(query,conn)
    return df
