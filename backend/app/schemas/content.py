from pydantic import BaseModel, Field
from typing import Optional, Dict, List
from datetime import datetime

class ContentUpload(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    content: str = Field(..., min_length=10)
    content_type: str = "text"  # text, url, file

class VideoConfig(BaseModel):
    voice: str = "en-US-JennyNeural"
    style: str = "professional"  # professional, casual, academic
    duration_target: int = 300  # seconds
    include_subtitles: bool = True
    background_music: bool = False
    language: str = "en-US"

class ProjectCreate(BaseModel):
    title: str
    description: Optional[str] = None
    content: str
    config: Optional[VideoConfig] = None

class ProjectResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True
