# backend/models/user_manager.py
import os
import hashlib
from backend.dao.user_dao import UserDAO

class UserManager:
    def __init__(self, dataset_path="dataset"):
        self.user_dao = UserDAO()
        self.dataset_path = dataset_path
        os.makedirs(self.dataset_path, exist_ok=True)

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def add_user(self, email, password, role, image_bytes):
        hashed = self._hash_password(password)

        user_folder = os.path.join(self.dataset_path, email)
        os.makedirs(user_folder, exist_ok=True)

        image_path = os.path.join(user_folder, "captured.jpg")
        with open(image_path, "wb") as f:
            f.write(image_bytes.getbuffer())

        self.user_dao.insert_user(email, hashed, role, image_path)

    def authenticate(self, email, password):
        hashed = self._hash_password(password)
        result = self.user_dao.get_user_by_credentials(email, hashed)
        if result:
            return {
                "id": result[0],
                "email": result[1],
                "role": result[2],
                "image_path": result[3]
            }
        return None

    def get_users(self):
        return self.user_dao.get_all_users()
