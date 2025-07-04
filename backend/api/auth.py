from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr, Field
from backend.auth.user_manager import UserManager
from backend.auth.face_authenticator import FaceAuthenticator
import base64
import io
from backend.api.api_key_auth import verify_bearer_token

# Initialize router and services
router = APIRouter(dependencies=[Depends(verify_bearer_token)])
user_db = UserManager()
face_auth = FaceAuthenticator()

# -------- Pydantic Model --------
class AuthWithFaceRequest(BaseModel):
    email: EmailStr
    password: str
    face_image_base64: str = Field(..., min_length=100)


# -------- Signup Endpoint --------
@router.post("/auth/signup")
def signup(request: AuthWithFaceRequest):
    try:
        image_bytes = base64.b64decode(request.face_image_base64)
        user_db.add_user(
            email=request.email,
            password=request.password,
            role="user",
            image_bytes=io.BytesIO(image_bytes)
        )
        return {"message": f"User {request.email} signed up successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# -------- Login Endpoint --------
@router.post("/auth/login")
def login(request: AuthWithFaceRequest):
    user = user_db.authenticate(request.email, request.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    try:
        image_bytes = base64.b64decode(request.face_image_base64)
        match = face_auth.verify(io.BytesIO(image_bytes), user["image_path"])

        if not match:
            raise HTTPException(status_code=403, detail="Face not recognized")

        return {
            "message": f"Welcome {user['role']} {user['email']}",
            "email": user["email"],
            "role": user["role"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
