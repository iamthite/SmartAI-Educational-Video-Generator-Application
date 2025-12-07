from fastapi import WebSocket, WebSocketDisconnect
from typing import Dict
import logging
import datetime

# Configure logging
logger = logging.getLogger(__name__)

class ConnectionManager:
    """Handles WebSocket connections and message broadcasting."""
    def __init__(self):
        # Using a dictionary to map client_id (str) to WebSocket
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket, client_id: str):
        await websocket.accept()
        self.active_connections[client_id] = websocket
        logger.info(f"WebSocket connected: {client_id}")

    def disconnect(self, client_id: str):
        """Removes a connection by client_id."""
        if client_id in self.active_connections:
            # Note: We don't need to close the socket here; it's closed by the exception handler.
            del self.active_connections[client_id]
            logger.info(f"WebSocket disconnected: {client_id}")

    async def send_progress(self, client_id: str, progress: int, status: str, message: str):
        """Sends a JSON progress update to a specific client."""
        if client_id in self.active_connections:
            try:
                await self.active_connections[client_id].send_json({
                    "progress": progress,
                    "status": status,
                    "message": message,
                    "timestamp": str(datetime.datetime.now())
                })
            except Exception as e:
                logger.error(f"Error sending to {client_id}: {e}")
                self.disconnect(client_id)

# Initialize the single manager instance for use across the application
manager = ConnectionManager()