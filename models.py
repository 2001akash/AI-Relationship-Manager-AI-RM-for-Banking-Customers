from pydantic import BaseModel
from typing import List, Dict, Optional


class ChatRequest(BaseModel):
    query: str


class ChatResponse(BaseModel):
    reply: str
    intent: str
    meta: Optional[Dict] = None


class ContextResponse(BaseModel):
    profile: Dict
    transactions: List[Dict]
    investments: List[Dict]
