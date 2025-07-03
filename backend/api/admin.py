from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr, Field
import base64, io
from backend.auth.user_manager import UserManager

router = APIRouter()
user_db = UserManager()

# Pydantic model
class AdminAddUserRequest(BaseModel):
    email: EmailStr
    password: str
    role: str = Field(..., pattern="^(user|admin)$")
    face_image_base64: str = Field(..., min_length=100)

@router.post("/admin/add_user")
def add_user(request: AdminAddUserRequest):
    try:
        image_bytes = base64.b64decode(request.face_image_base64)
        user_db.add_user(
            email=request.email,
            password=request.password,
            role=request.role,
            image_bytes=io.BytesIO(image_bytes)
        )
        return {"message": f"User {request.email} added as {request.role}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/admin/users")
def list_users():
    try:
        users = user_db.get_users()
        return [
            {
                "id": row[0],
                "email": row[1],
                "role": row[2],
                "image_path": row[3]
            }
            for row in users
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
