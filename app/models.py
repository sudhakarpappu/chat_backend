from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    userId: str
    name: str
    phone: str
    publicKey: str
    createdAt: datetime

class Message(BaseModel):
    messageId: str
    conversationId: str
    senderId: str
    receiverId: str
    content: str
    timestamp: datetime
    status: str
    mode: str
    synced: bool
