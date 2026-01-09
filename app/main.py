from fastapi import FastAPI
from app.routes import users, messages

from app.routes.websocket import router as websocket_router

app = FastAPI()
app.include_router(websocket_router)



app.include_router(users.router)
app.include_router(messages.router)
app.include_router(websocket.router)

@app.get("/")
def health():
    return {"status": "Backend running"}
