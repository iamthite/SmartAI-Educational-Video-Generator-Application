
# ============================================
# backend/app/config.py - ENHANCED
# ============================================
from pydantic_settings import BaseSettings
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    # App
    APP_NAME: str = "Educational Video Generator"
    API_VERSION: str = "v1"
    DEBUG: bool = True
    ENVIRONMENT: str = "development"
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./edu_video.db")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    
    # Azure OpenAI
    AZURE_OPENAI_ENDPOINT: str = os.getenv("AZURE_OPENAI_ENDPOINT", "")
    AZURE_OPENAI_API_KEY: str = os.getenv("AZURE_OPENAI_API_KEY", "")
    AZURE_OPENAI_DEPLOYMENT_NAME: str = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4")
    AZURE_OPENAI_API_VERSION: str = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")
    
    # Azure Speech
    AZURE_SPEECH_KEY: str = os.getenv("AZURE_SPEECH_KEY", "")
    AZURE_SPEECH_REGION: str = os.getenv("AZURE_SPEECH_REGION", "eastus")
    
    # Azure Storage
    AZURE_STORAGE_CONNECTION_STRING: str = os.getenv("AZURE_STORAGE_CONNECTION_STRING", "")
    AZURE_STORAGE_CONTAINER_NAME: str = os.getenv("AZURE_STORAGE_CONTAINER_NAME", "videos")
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Celery
    CELERY_BROKER_URL: str = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
    CELERY_RESULT_BACKEND: str = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")
    
    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000"
    ]
    
    # File Upload
    MAX_FILE_SIZE: int = 50 * 1024 * 1024  # 50MB
    ALLOWED_EXTENSIONS: List[str] = [".pdf", ".docx", ".txt", ".md"]
    
    # Video Settings
    DEFAULT_VIDEO_QUALITY: str = "1080p"
    MAX_VIDEO_DURATION: int = 1800  # 30 minutes
    SUPPORTED_LANGUAGES: List[str] = ["en-IN", "en-US", "hi-IN", "ta-IN", "te-IN", "mr-IN"]
    
    class Config:
        env_file = ".env"

settings = Settings()

#=========================================================================

# from pydantic_settings import BaseSettings
# from typing import List
# import os
# from dotenv import load_dotenv

# load_dotenv()

# class Settings(BaseSettings):
#     APP_NAME: str = "Educational Video Generator"
#     API_VERSION: str = "v1"
#     DEBUG: bool = True
#     ENVIRONMENT: str = "development"
#     DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./edu_video.db")
#     REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
#     AZURE_OPENAI_ENDPOINT: str = os.getenv("AZURE_OPENAI_ENDPOINT", "")
#     AZURE_OPENAI_API_KEY: str = os.getenv("AZURE_OPENAI_API_KEY", "")
#     AZURE_OPENAI_DEPLOYMENT_NAME: str = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4")
#     AZURE_OPENAI_API_VERSION: str = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")
#     AZURE_SPEECH_KEY: str = os.getenv("AZURE_SPEECH_KEY", "")
#     AZURE_SPEECH_REGION: str = os.getenv("AZURE_SPEECH_REGION", "eastus")
#     AZURE_STORAGE_CONNECTION_STRING: str = os.getenv("AZURE_STORAGE_CONNECTION_STRING", "")
#     AZURE_STORAGE_CONTAINER_NAME: str = os.getenv("AZURE_STORAGE_CONTAINER_NAME", "videos")
#     SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
#     ALGORITHM: str = "HS256"
#     ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
#     CELERY_BROKER_URL: str = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
#     CELERY_RESULT_BACKEND: str = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")
#     CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:5173", "http://127.0.0.1:3000"]
#     MAX_FILE_SIZE: int = 50 * 1024 * 1024
#     ALLOWED_EXTENSIONS: List[str] = [".pdf", ".docx", ".txt", ".md"]
#     DEFAULT_VIDEO_QUALITY: str = "1080p"
#     MAX_VIDEO_DURATION: int = 1800
#     SUPPORTED_LANGUAGES: List[str] = ["en-IN", "en-US", "hi-IN", "ta-IN", "te-IN", "mr-IN"]
    
#     class Config:
#         env_file = ".env"

# settings = Settings()