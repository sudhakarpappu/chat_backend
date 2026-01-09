from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client["chat_app"]

users_col = db["users"]
messages_col = db["messages"]
conversations_col = db["conversations"]
