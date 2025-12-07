# ============================================
# backend/app/main.py - PRODUCTION READY
# ============================================
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn
import logging
from app.config import settings
from app.database import engine, Base
from app.api.v1 import routes
from app.services.websocket_manager import ConnectionManager, manager

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# # WebSocket Manager
# class ConnectionManager:
#     def __init__(self):
#         self.active_connections: dict[str, WebSocket] = {}

#     async def connect(self, websocket: WebSocket, client_id: str):
#         await websocket.accept()
#         self.active_connections[client_id] = websocket
#         logger.info(f"WebSocket connected: {client_id}")

#     def disconnect(self, client_id: str):
#         if client_id in self.active_connections:
#             del self.active_connections[client_id]
#             logger.info(f"WebSocket disconnected: {client_id}")

#     async def send_progress(self, client_id: str, progress: int, status: str, message: str):
#         if client_id in self.active_connections:
#             try:
#                 await self.active_connections[client_id].send_json({
#                     "progress": progress,
#                     "status": status,
#                     "message": message,
#                     "timestamp": str(__import__('datetime').datetime.now())
#                 })
#             except Exception as e:
#                 logger.error(f"Error sending to {client_id}: {e}")
#                 self.disconnect(client_id)

# manager = ConnectionManager()

# Lifespan management
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Starting Educational Video Generator API...")
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("✓ Database tables created")
    except Exception as e:
        logger.warning(f"Database warning: {e}")
    
    yield
    
    # Shutdown
    logger.info("Shutting down...")

# Initialize FastAPI
app = FastAPI(
    title="Educational Video Generator API",
    version="2.0.0",
    description="AI-Powered Educational Video Generation Platform",
    lifespan=lifespan
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(routes.router, prefix=f"/api/{settings.API_VERSION}")

# WebSocket endpoint
@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket, client_id)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_progress(client_id, 0, "connected", "WebSocket connected")
    except WebSocketDisconnect:
        manager.disconnect(client_id)

# Health check
@app.get("/")
async def root():
    return {
        "service": "Educational Video Generator",
        "version": "2.0.0",
        "status": "running",
        "docs": "/docs"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "database": "connected",
        "services": {
            "azure_openai": bool(settings.AZURE_OPENAI_API_KEY),
            "azure_speech": bool(settings.AZURE_SPEECH_KEY),
            "azure_storage": bool(settings.AZURE_STORAGE_CONNECTION_STRING)
        }
    }

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG
    )





#==========================================================================



# from fastapi import FastAPI, WebSocket, WebSocketDisconnect
# from fastapi.middleware.cors import CORSMiddleware
# from contextlib import asynccontextmanager
# import uvicorn
# import logging
# from app.config import settings
# from app.database import engine, Base
# from app.api.v1 import routes

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)

# class ConnectionManager:
#     def __init__(self):
#         self.active_connections: dict[str, WebSocket] = {}

#     async def connect(self, websocket: WebSocket, client_id: str):
#         await websocket.accept()
#         self.active_connections[client_id] = websocket
#         logger.info(f"WebSocket connected: {client_id}")

#     def disconnect(self, client_id: str):
#         if client_id in self.active_connections:
#             del self.active_connections[client_id]
#             logger.info(f"WebSocket disconnected: {client_id}")

#     async def send_progress(self, client_id: str, progress: int, status: str, message: str):
#         if client_id in self.active_connections:
#             try:
#                 import datetime
#                 await self.active_connections[client_id].send_json({
#                     "progress": progress,
#                     "status": status,
#                     "message": message,
#                     "timestamp": str(datetime.datetime.now())
#                 })
#             except Exception as e:
#                 logger.error(f"Error sending to {client_id}: {e}")
#                 self.disconnect(client_id)

# manager = ConnectionManager()

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     logger.info("Starting Educational Video Generator API...")
#     try:
#         Base.metadata.create_all(bind=engine)
#         logger.info("✓ Database tables created")
#     except Exception as e:
#         logger.warning(f"Database warning: {e}")
#     yield
#     logger.info("Shutting down...")

# app = FastAPI(
#     title="Educational Video Generator API",
#     version="2.0.0",
#     description="AI-Powered Educational Video Generation Platform",
#     lifespan=lifespan
# )

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=settings.CORS_ORIGINS,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.include_router(routes.router, prefix=f"/api/{settings.API_VERSION}")

# @app.websocket("/ws/{client_id}")
# async def websocket_endpoint(websocket: WebSocket, client_id: str):
#     await manager.connect(websocket, client_id)
#     try:
#         while True:
#             data = await websocket.receive_text()
#             await manager.send_progress(client_id, 0, "connected", "WebSocket connected")
#     except WebSocketDisconnect:
#         manager.disconnect(client_id)

# @app.get("/")
# async def root():
#     return {"service": "Educational Video Generator", "version": "2.0.0", "status": "running"}

# @app.get("/health")
# async def health():
#     return {
#         "status": "healthy",
#         "database": "connected",
#         "services": {
#             "azure_openai": bool(settings.AZURE_OPENAI_API_KEY),
#             "azure_speech": bool(settings.AZURE_SPEECH_KEY),
#             "azure_storage": bool(settings.AZURE_STORAGE_CONNECTION_STRING)
#         }
#     }

# if __name__ == "__main__":
#     uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=settings.DEBUG)