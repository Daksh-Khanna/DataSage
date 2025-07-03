from fastapi import FastAPI
from backend.api import admin, auth, chat, session

app = FastAPI()

app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(session.router)
app.include_router(chat.router)
