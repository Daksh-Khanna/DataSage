from fastapi import FastAPI
from backend.api import auth_api, admin_api, session_api, chat_api

app = FastAPI()

app.include_router(auth_api.router)
app.include_router(admin_api.router)
app.include_router(session_api.router)
app.include_router(chat_api.router)
