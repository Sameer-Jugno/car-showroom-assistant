from fastapi import APIRouter 
from pydantic import BaseModel 
from app.agents.car_agent import ask_agent

router = APIRouter() 

class ChatRequest(BaseModel) : 
    query : str 
    session_id : str | None = None 

class ChatResponse(BaseModel) : 
    response : str 
    session_id : str | None = None 


@router.post("/query", response_model=ChatResponse)
async def chat(chat: ChatRequest):
    session_id = chat.session_id or "default"
    response_text = await ask_agent(chat.query, session_id=session_id)
    return {"response": response_text, "session_id": session_id}