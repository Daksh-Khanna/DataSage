import psycopg2
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST

class DBConnector:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if not self.connection or self.connection.closed:
            self.connection = psycopg2.connect(
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST
            )
        return self.connection
    
    def __del__(self):
     if self.connection and not self.connection.closed:
        self.connection.close()