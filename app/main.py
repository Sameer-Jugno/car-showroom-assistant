from fastapi import FastAPI
from .api import health, chat

app = FastAPI()

app.include_router(health.router)
app.include_router(chat.router, prefix="/chat")