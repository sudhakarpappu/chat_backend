from fastapi import FastAPI
from app.routes import users, messages
from app.routes.websocket import router as websocket_router

app = FastAPI()

# ✅ WebSocket router
app.include_router(websocket_router)

# ✅ REST routers
app.include_router(users.router)
app.include_router(messages.router)

@app.get("/")
def health():
    return {"status": "Backend running"}
