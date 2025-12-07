# ============================================
# backend/app/schemas/video.py - ENHANCED
# ============================================
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class EducationLevel(BaseModel):
    """Education level configuration"""
    level: str = Field(..., description="1st-12th, Diploma, Engineering, Medical, etc.")
    subject: Optional[str] = Field(None, description="Mathematics, Physics, Biology, etc.")
    topic: Optional[str] = Field(None, description="Specific topic name")

class VoiceConfig(BaseModel):
    """Voice configuration"""
    gender: str = Field("female", description="male or female")
    language: str = Field("en-IN", description="en-IN, hi-IN, ta-IN, etc.")
    accent: str = Field("indian", description="indian, american, british")
    speed: float = Field(1.0, description="0.5 to 2.0")
    pitch: float = Field(1.0, description="0.5 to 2.0")

class VideoStyle(BaseModel):
    """Video style configuration"""
    theme: str = Field("educational", description="educational, professional, casual")
    color_scheme: str = Field("blue", description="blue, green, purple, custom")
    animation_style: str = Field("smooth", description="smooth, minimal, dynamic")
    include_transitions: bool = Field(True)
    background_music: bool = Field(False)
    music_volume: int = Field(30, ge=0, le=100)

class VideoConfig(BaseModel):
    """Complete video configuration"""
    education_level: EducationLevel
    voice: VoiceConfig
    style: VideoStyle
    quality: str = Field("1080p", description="720p, 1080p, 1440p")
    duration_preference: str = Field("medium", description="short, medium, long")
    include_subtitles: bool = Field(True)
    subtitle_language: str = Field("en")
    pacing: str = Field("medium", description="slow, medium, fast")
    include_diagrams: bool = Field(True)
    include_examples: bool = Field(True)

class ContentUpload(BaseModel):
    """Content upload schema"""
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    content: str = Field(..., min_length=50)
    content_type: str = "text"
    config: Optional[VideoConfig] = None

class ProjectCreate(BaseModel):
    """Project creation schema"""
    title: str
    description: Optional[str] = None
    content: str
    config: VideoConfig

class ProjectResponse(BaseModel):
    """Project response schema"""
    id: int
    title: str
    description: Optional[str]
    status: str
    progress: int = 0
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class VideoResponse(BaseModel):
    """Video response schema"""
    id: int
    project_id: int
    title: str
    file_url: Optional[str]
    thumbnail_url: Optional[str]
    duration: Optional[int]
    status: str
    quality: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class VideoProgress(BaseModel):
    """Real-time progress update"""
    progress: int = Field(..., ge=0, le=100)
    status: str
    message: str
    current_step: str
    estimated_time_remaining: Optional[int] = None
