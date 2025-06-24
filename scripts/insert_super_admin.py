import sys
import os
import uuid
import hashlib
import psycopg2

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.dao.db_connector import DBConnector
from config import PASSWD

# ======== CONFIGURE THESE =========
EMAIL = "daksh.khanna.official@gmail.com"
PASSWORD = PASSWD
IMAGE_PATH = "dataset/daksh.khanna.official@gmail.com/captured.jpg"
# ==================================

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def insert_super_admin():
    db = DBConnector()
    conn = db.get_connection()

    user_id = str(uuid.uuid4())
    hashed_pwd = hash_password(PASSWORD)

    with conn.cursor() as cur:
        try:
            cur.execute("""
                INSERT INTO users (id, email, password, role, image_path)
                VALUES (%s, %s, %s, %s, %s)
            """, (user_id, EMAIL, hashed_pwd, "super_admin", IMAGE_PATH))
            conn.commit()
            print(f"[✅] Super admin inserted: {EMAIL} ({user_id})")
        except psycopg2.Error as e:
            print(f"[❌] Failed to insert: {e}")
            conn.rollback()

if __name__ == "__main__":
    insert_super_admin()
