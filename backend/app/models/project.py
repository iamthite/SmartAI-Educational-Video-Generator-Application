# ============================================
# backend/app/models/project.py - ENHANCED
# ============================================
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, JSON, Enum, Float
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.database import Base

class ProjectStatus(str, enum.Enum):
    CREATED = "created"
    ANALYZING = "analyzing"
    GENERATING_SCRIPT = "generating_script"
    CREATING_VISUALS = "creating_visuals"
    GENERATING_AUDIO = "generating_audio"
    COMPOSING_VIDEO = "composing_video"
    UPLOADING = "uploading"
    COMPLETED = "completed"
    FAILED = "failed"

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(255))
    role = Column(String(50), default="user")  # user, premium, admin
    is_active = Column(Integer, default=1)
    videos_generated = Column(Integer, default=0)
    storage_used = Column(Float, default=0.0)  # in GB
    created_at = Column(DateTime, default=datetime.utcnow)
    
    projects = relationship("Project", back_populates="user")

class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    content = Column(Text, nullable=False)
    status = Column(Enum(ProjectStatus), default=ProjectStatus.CREATED)
    progress = Column(Integer, default=0)
    config = Column(JSON, default={})
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user = relationship("User", back_populates="projects")
    videos = relationship("Video", back_populates="project", cascade="all, delete-orphan")
    assets = relationship("Asset", back_populates="project", cascade="all, delete-orphan")

class Video(Base):
    __tablename__ = "videos"
    
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    title = Column(String(255), nullable=False)
    duration = Column(Integer)  # seconds
    file_url = Column(String(500))
    thumbnail_url = Column(String(500))
    file_size = Column(Float)  # in MB
    quality = Column(String(20), default="1080p")
    script = Column(Text)
    scenes = Column(JSON, default=[])
    status = Column(String(50), default="pending")
    views = Column(Integer, default=0)
    downloads = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    project = relationship("Project", back_populates="videos")

class Asset(Base):
    __tablename__ = "assets"
    
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    asset_type = Column(String(50))  # image, audio, diagram, subtitle
    file_url = Column(String(500))
    file_size = Column(Float)  # in MB
    file_metadata = Column(JSON, default={})
    created_at = Column(DateTime, default=datetime.utcnow)
    
    project = relationship("Project", back_populates="assets")

class Analytics(Base):
    __tablename__ = "analytics"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    event_type = Column(String(100))  # video_generated, video_downloaded, etc.
    event_data = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)

#======================================================================


# from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, JSON, Enum, Float
# from sqlalchemy.orm import relationship
# from datetime import datetime
# import enum
# from app.database import Base

# class ProjectStatus(str, enum.Enum):
#     CREATED = "created"
#     ANALYZING = "analyzing"
#     GENERATING_SCRIPT = "generating_script"
#     CREATING_VISUALS = "creating_visuals"
#     GENERATING_AUDIO = "generating_audio"
#     COMPOSING_VIDEO = "composing_video"
#     UPLOADING = "uploading"
#     COMPLETED = "completed"
#     FAILED = "failed"

# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String(255), unique=True, index=True, nullable=False)
#     hashed_password = Column(String(255), nullable=False)
#     full_name = Column(String(255))
#     role = Column(String(50), default="user")
#     is_active = Column(Integer, default=1)
#     videos_generated = Column(Integer, default=0)
#     storage_used = Column(Float, default=0.0)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     projects = relationship("Project", back_populates="user")

# class Project(Base):
#     __tablename__ = "projects"
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
#     title = Column(String(255), nullable=False)
#     description = Column(Text)
#     content = Column(Text, nullable=False)
#     status = Column(Enum(ProjectStatus), default=ProjectStatus.CREATED)
#     progress = Column(Integer, default=0)
#     config = Column(JSON, default={})
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
#     user = relationship("User", back_populates="projects")
#     videos = relationship("Video", back_populates="project", cascade="all, delete-orphan")
#     assets = relationship("Asset", back_populates="project", cascade="all, delete-orphan")

# class Video(Base):
#     __tablename__ = "videos"
#     id = Column(Integer, primary_key=True, index=True)
#     project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
#     title = Column(String(255), nullable=False)
#     duration = Column(Integer)
#     file_url = Column(String(500))
#     thumbnail_url = Column(String(500))
#     file_size = Column(Float)
#     quality = Column(String(20), default="1080p")
#     script = Column(Text)
#     scenes = Column(JSON, default=[])
#     status = Column(String(50), default="pending")
#     views = Column(Integer, default=0)
#     downloads = Column(Integer, default=0)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     project = relationship("Project", back_populates="videos")

# class Asset(Base):
#     __tablename__ = "assets"
#     id = Column(Integer, primary_key=True, index=True)
#     project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
#     asset_type = Column(String(50))
#     file_url = Column(String(500))
#     file_size = Column(Float)
#     asset_metadata = Column(JSON, default={})  # RENAMED from metadata to asset_metadata
#     created_at = Column(DateTime, default=datetime.utcnow)
#     project = relationship("Project", back_populates="assets")

# class Analytics(Base):
#     __tablename__ = "analytics"
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     event_type = Column(String(100))
#     event_data = Column(JSON)
#     created_at = Column(DateTime, default=datetime.utcnow)