from backend.db_connector import get_db_connection
from backend.queries import get_query
import pandas as pd

#getting query
query = get_query()

#fetching dataframe
def fetch_combined_data():
    with get_db_connection() as conn:
        df = pd.read_sql(query, conn)
        df["System Status"] = df["System Status"].apply(lambda x: "Success" if x else "Failed")
    return df