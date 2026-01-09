from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import Dict

router = APIRouter()

# Store active WebSocket connections
active_connections: Dict[str, WebSocket] = {}


@router.websocket("/ws/{user_id}")
async def websocket_endpoint(ws: WebSocket, user_id: str):
    await ws.accept()
    active_connections[user_id] = ws
    print(f"CONNECTED: {user_id}")

    try:
        while True:
            # ✅ Receive JSON (NOT text)
            payload = await ws.receive_json()

            receiver = payload.get("receiverId")
            print(f"Message from {user_id} → {receiver}")

            if receiver in active_connections:
                await active_connections[receiver].send_json(payload)
                print(f"Delivered to {receiver}")
            else:
                print(f"{receiver} is offline")

    except WebSocketDisconnect:
        print(f"DISCONNECTED: {user_id}")
        active_connections.pop(user_id, None)
