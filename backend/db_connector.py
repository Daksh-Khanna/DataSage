import psycopg2
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST

def get_db_connection():
    """Establishes connection using environment variables from config."""
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST
    )