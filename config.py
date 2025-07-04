from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access credentials
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
PPLX_API_KEY=os.getenv("PPLX_API_KEY")
PASSWD=os.getenv("PASSWD")
NGROK_TOKEN=os.getenv("NGROK_TOKEN")
API_KEY=os.getenv("API_KEY")
API_BASE_URL=os.getenv("API_BASE_URL")