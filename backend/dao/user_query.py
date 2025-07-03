# backend/dao/user_query.py

class UserQueryBuilder:
    def create_users_table(self):
        return """
            CREATE TABLE IF NOT EXISTS users (
                id UUID PRIMARY KEY,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                role TEXT CHECK (role IN ('user', 'admin', 'super_admin')) NOT NULL,
                image_path TEXT NOT NULL
            )
        """

    def insert_user(self):
        return """
            INSERT INTO users (id, email, password, role, image_path)
            VALUES (%s, %s, %s, %s, %s)
        """

    def auth_user(self):
        return """
            SELECT id, email, role, image_path FROM users
            WHERE email = %s AND password = %s
        """

    def get_all_users(self):
        return """
            SELECT id, email, role, image_path FROM users ORDER BY email
        """
