from fastapi import APIRouter 
from pydantic import BaseModel 

router = APIRouter() 

class ChatRequest(BaseModel) : 
    query : str 
    session_id : str | None = None 

class ChatResponse(BaseModel) : 
    response : str 
    session_id : str | None = None 

@router.post("/query", response_model=ChatResponse) 
def chat(chat : ChatRequest) : 
    return {"response": "".join(reversed(chat.query)), "session_id": chat.session_id}