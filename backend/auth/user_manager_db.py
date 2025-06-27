import os
import uuid
import hashlib
from backend.dao.db_connector import DBConnector

class UserManagerDB:
    def __init__(self, dataset_path="dataset"):
        self.db = DBConnector()
        self.conn = self.db.get_connection()
        self.dataset_path = dataset_path
        os.makedirs(self.dataset_path, exist_ok=True)
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id UUID PRIMARY KEY,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    role TEXT CHECK (role IN ('user', 'admin', 'super_admin')) NOT NULL,
                    image_path TEXT NOT NULL
                )
            """)
            self.conn.commit()

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def add_user(self, email, password, role, image_bytes):
        user_id = str(uuid.uuid4())
        hashed = self._hash_password(password)

        user_folder = os.path.join(self.dataset_path, email)
        os.makedirs(user_folder, exist_ok=True)

        image_path = os.path.join(user_folder, "captured.jpg")
        with open(image_path, "wb") as f:
            f.write(image_bytes.getbuffer())

        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO users (id, email, password, role, image_path)
                VALUES (%s, %s, %s, %s, %s)
            """, (user_id, email, hashed, role, image_path))
            self.conn.commit()

    def authenticate(self, email, password):
        hashed = self._hash_password(password)
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT id, email, role, image_path FROM users
                WHERE email = %s AND password = %s
            """, (email, hashed))
            result = cur.fetchone()
            if result:
                return {
                    "id": result[0],
                    "email": result[1],
                    "role": result[2],
                    "image_path": result[3]
                }
        return None

    def get_all_users(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT email, role FROM users")
            return cur.fetchall()
        
    def get_all_users_full(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT id, email, role, image_path FROM users ORDER BY email")
            return cur.fetchall()
