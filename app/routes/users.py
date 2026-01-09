from fastapi import APIRouter
from app.database import users_col
from app.models import User

router = APIRouter()

@router.post("/register")
def register_user(user: User):
    users_col.insert_one(user.dict())
    return {"message": "User registered"}
