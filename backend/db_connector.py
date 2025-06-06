import psycopg2
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST
from utils.logger import get_logger
logger = get_logger("db_logger","db.log")

class DBConnector:
    def __init__(self):
        self.connection = None
        logger.info("DBConnector initialized")

    def get_connection(self):
        try:
            if not self.connection or self.connection.closed:
                self.connection = psycopg2.connect(
                    dbname=DB_NAME,
                    user=DB_USER,
                    password=DB_PASSWORD,
                    host=DB_HOST
                )
                logger.info("Database connection established.")
        except psycopg2.Error as e:
            logger.error(f"Database connection failed: {e}")
            raise
        return self.connection
    
    def __del__(self):
        try:
            if self.connection and not self.connection.closed:
                self.connection.close()
                logger.info("Database connection closed.")
        except Exception as e:
            logger.warning(f"Error closing DB connection: {e}")