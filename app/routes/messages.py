from fastapi import APIRouter
from app.database import messages_col
from app.models import Message

router = APIRouter()

@router.post("/sync-message")
def sync_message(message: Message):
    messages_col.insert_one(message.dict())
    return {"status": "Message synced"}
