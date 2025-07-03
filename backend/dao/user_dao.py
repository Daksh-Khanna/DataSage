# backend/dao/user_dao.py

import uuid
from backend.dao.db_connector import DBConnector
from backend.dao.user_query import UserQueryBuilder

class UserDAO:
    def __init__(self):
        self.db = DBConnector()
        self.conn = self.db.get_connection()
        self.queries = UserQueryBuilder()
        self._create_users_table()

    def _create_users_table(self):
        with self.conn.cursor() as cur:
            cur.execute(self.queries.create_users_table())
            self.conn.commit()

    def insert_user(self, email, hashed_password, role, image_path):
        user_id = str(uuid.uuid4())
        with self.conn.cursor() as cur:
            cur.execute(
                self.queries.insert_user(),
                (user_id, email, hashed_password, role, image_path)
            )
            self.conn.commit()

    def get_user_by_credentials(self, email, hashed_password):
        with self.conn.cursor() as cur:
            cur.execute(self.queries.auth_user(), (email, hashed_password))
            return cur.fetchone()

    def get_all_users(self):
        with self.conn.cursor() as cur:
            cur.execute(self.queries.get_all_users())
            return cur.fetchall()
