from fastapi import FastAPI 
from .api import  health, chat

app = FastAPI()

app.include_router( router = health.router)
app.include_router( router = chat.router, prefix="/chat" )

