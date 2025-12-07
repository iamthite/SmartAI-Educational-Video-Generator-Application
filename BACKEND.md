# ⚙️ Backend Documentation - FastAPI + Python

Complete backend code documentation for the Educational Video Generator.

---

## 📋 Overview

- **Framework:** FastAPI 0.109
- **Language:** Python 3.9+
- **Database:** SQLite (SQLAlchemy ORM)
- **Task Queue:** Celery 5.3
- **Message Broker:** Redis
- **AI Orchestration:** LangGraph
- **LLM:** Azure OpenAI (GPT-4)
- **Video:** MoviePy 1.0
- **Diagrams:** Matplotlib 3.8

---

## 🗂️ Folder Structure

```
backend/
│
├── app/
│   ├── main.py                      ← FastAPI application entry
│   ├── config.py                    ← Configuration & settings
│   ├── database.py                  ← SQLAlchemy setup
│   │
│   ├── models/                      ← Database models
│   │   ├── __init__.py
│   │   ├── user.py                 ← User model
│   │   ├── project.py              ← Project model
│   │   ├── video.py                ← Video model
│   │   └── asset.py                ← Asset model
│   │
│   ├── schemas/                     ← Pydantic validators
│   │   ├── __init__.py
│   │   ├── content.py              ← Content schemas
│   │   └── video.py                ← Video schemas
│   │
│   ├── api/v1/                      ← API endpoints
│   │   ├── __init__.py
│   │   ├── routes.py               ← Main router
│   │   ├── auth.py                 ← Login/Register
│   │   ├── content.py              ← Content upload/management
│   │   ├── video.py                ← Video generation
│   │   └── status.py               ← Task status
│   │
│   ├── agents/                      ← LangGraph Agents
│   │   ├── __init__.py
│   │   ├── orchestrator.py         ← Main orchestrator (Agent Runner)
│   │   ├── content_analyzer.py     ← Agent 1: Analysis
│   │   ├── script_generator.py     ← Agent 2: Script
│   │   ├── visual_planner.py       ← Agent 3: Visuals
│   │   ├── diagram_generator.py    ← Agent 4: Diagrams
│   │   └── video_composer.py       ← Agent 5: Composition
│   │
│   ├── services/                    ← Business logic
│   │   ├── __init__.py
│   │   ├── azure_openai.py         ← OpenAI client
│   │   ├── azure_speech.py         ← Speech synthesis
│   │   ├── azure_storage.py        ← Cloud storage
│   │   ├── document_parser.py      ← PDF/DOCX parsing
│   │   ├── diagram_service.py      ← Matplotlib diagrams
│   │   ├── image_generator.py      ← Image generation
│   │   └── video_service.py        ← MoviePy composition
│   │
│   ├── core/                        ← Core utilities
│   │   ├── __init__.py
│   │   ├── celery_app.py           ← Celery config
│   │   ├── security.py             ← JWT & hashing
│   │   ├── dependencies.py         ← FastAPI dependencies
│   │   └── exceptions.py           ← Custom exceptions
│   │
│   └── utils/                       ← Utilities
│       ├── __init__.py
│       ├── file_handler.py         ← File operations
│       ├── validators.py           ← Input validation
│       └── helpers.py              ← Helper functions
│
├── alembic/                         ← Database migrations
│   ├── versions/                   ← Migration scripts
│   └── env.py
│
├── tests/                           ← Unit tests
│   ├── __init__.py
│   ├── test_api.py
│   └── test_agents.py
│
├── requirements.txt                 ← Python dependencies
├── Dockerfile                       ← Container image
├── .env.example                     ← Environment template
└── .gitignore
```

---

## 📄 Key Files

### `main.py` - FastAPI Application

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import routes

app = FastAPI(title="Educational Video Generator API")

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(routes.router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "Educational Video Generator"}
```

---

### `config.py` - Configuration

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Azure
    AZURE_OPENAI_ENDPOINT: str
    AZURE_OPENAI_API_KEY: str
    AZURE_OPENAI_DEPLOYMENT_NAME: str
    AZURE_SPEECH_KEY: str
    AZURE_SPEECH_REGION: str
    
    # Database
    DATABASE_URL: str = "sqlite:///./edu_video.db"
    
    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379"
    
    class Config:
        env_file = ".env"

settings = Settings()
```

---

### `database.py` - Database Setup

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

---

## 🤖 LangGraph Agents

### Agent Architecture

```
┌──────────────────────────────────────────────────┐
│           Orchestrator (Main Workflow)           │
├──────────────────────────────────────────────────┤
│                                                  │
│  Input: Project ID + Content                    │
│         ↓                                        │
│  Agent 1: ContentAnalyzer                       │
│    - Extract text                               │
│    - Parse structure                            │
│    - Analyze with Azure OpenAI                  │
│    - Output: Analysis JSON                      │
│         ↓                                        │
│  Agent 2: ScriptGenerator                       │
│    - Create video structure                     │
│    - Generate narration                         │
│    - Time scenes                                │
│    - Output: Video Script                       │
│         ↓                                        │
│  Agent 3: VisualPlanner                         │
│    - Plan visual elements                       │
│    - Choose styles                              │
│    - Design layout                              │
│    - Output: Visual Plan                        │
│         ↓                                        │
│  Agent 4: DiagramGenerator                      │
│    - Create diagrams                            │
│    - Generate images                            │
│    - Export as PNG                              │
│    - Output: Image files                        │
│         ↓                                        │
│  Agent 5: VideoComposer                         │
│    - Synthesize speech                          │
│    - Compose video                              │
│    - Add effects                                │
│    - Export MP4                                 │
│    - Output: Video file                         │
│         ↓                                        │
│  Result: Complete video ready for user          │
└──────────────────────────────────────────────────┘
```

### `orchestrator.py` - Main Workflow

```python
from langgraph.graph import StateGraph
from typing import TypedDict

class VideoState(TypedDict):
    project_id: int
    content: str
    analysis: dict
    script: dict
    visual_plan: dict
    assets: list
    video_path: str

def create_workflow():
    workflow = StateGraph(VideoState)
    
    # Add nodes (agents)
    workflow.add_node("analyze", content_analyzer)
    workflow.add_node("script", script_generator)
    workflow.add_node("visual", visual_planner)
    workflow.add_node("diagram", diagram_generator)
    workflow.add_node("compose", video_composer)
    
    # Add edges (flow)
    workflow.add_edge("analyze", "script")
    workflow.add_edge("script", "visual")
    workflow.add_edge("visual", "diagram")
    workflow.add_edge("diagram", "compose")
    
    workflow.set_entry_point("analyze")
    workflow.set_finish_point("compose")
    
    return workflow.compile()
```

---

### Agent 1: ContentAnalyzer

```python
# app/agents/content_analyzer.py

async def analyze_content(state: VideoState) -> VideoState:
    """
    Extract and analyze content using Azure OpenAI
    """
    content = state["content"]
    
    # Parse document if PDF/DOCX
    parsed_text = extract_text(content)
    
    # Call Azure OpenAI for analysis
    analysis = await openai_service.analyze(parsed_text)
    
    state["analysis"] = analysis
    return state

# Output example:
{
    "summary": "Introduction to Python functions...",
    "key_concepts": ["functions", "arguments", "return values"],
    "difficulty_level": "beginner",
    "estimated_duration": 600,
    "target_audience": "Class 10 students"
}
```

---

### Agent 2: ScriptGenerator

```python
# app/agents/script_generator.py

async def generate_script(state: VideoState) -> VideoState:
    """
    Generate video script with narration and timing
    """
    analysis = state["analysis"]
    
    # Create video structure
    script = await openai_service.generate_script(analysis)
    
    state["script"] = script
    return state

# Output example:
{
    "title": "Introduction to Python Functions",
    "scenes": [
        {
            "scene_number": 1,
            "title": "Introduction",
            "narration": "Today we'll learn about functions...",
            "duration": 30,
            "key_points": ["What is a function", "Why use functions"]
        },
        {
            "scene_number": 2,
            "title": "Syntax",
            "narration": "The basic syntax of a function is...",
            "duration": 45,
            "key_points": ["def keyword", "Parameters", "Return statement"]
        }
    ]
}
```

---

### Agent 3: VisualPlanner

```python
# app/agents/visual_planner.py

async def plan_visuals(state: VideoState) -> VideoState:
    """
    Plan visual elements for each scene
    """
    script = state["script"]
    
    visual_plan = await openai_service.plan_visuals(script)
    
    state["visual_plan"] = visual_plan
    return state

# Output example:
{
    "scene_1": {
        "visual_type": "text_overlay",
        "elements": ["Title", "Subtitle"],
        "colors": ["#007AFF", "#FFFFFF"],
        "animation": "fade_in"
    },
    "scene_2": {
        "visual_type": "diagram",
        "elements": ["Code syntax", "Arrows"],
        "colors": ["#000000", "#FF5733"],
        "animation": "type_write"
    }
}
```

---

### Agent 4: DiagramGenerator

```python
# app/agents/diagram_generator.py

async def generate_diagrams(state: VideoState) -> VideoState:
    """
    Generate diagrams and images using Matplotlib
    """
    visual_plan = state["visual_plan"]
    
    assets = []
    for scene_id, visual in visual_plan.items():
        image_path = await diagram_service.create(visual)
        assets.append({
            "scene": scene_id,
            "path": image_path,
            "type": "image"
        })
    
    state["assets"] = assets
    return state
```

---

### Agent 5: VideoComposer

```python
# app/agents/video_composer.py

async def compose_video(state: VideoState) -> VideoState:
    """
    Compose final video with audio and visuals
    """
    script = state["script"]
    assets = state["assets"]
    
    # Generate speech
    audio_path = await speech_service.synthesize(script)
    
    # Compose video
    video_path = await video_service.compose(
        scenes=script["scenes"],
        images=assets,
        audio=audio_path
    )
    
    state["video_path"] = video_path
    return state
```

---

## 🔌 API Endpoints

### Content Endpoints

#### Upload Content
```
POST /api/v1/content/upload
Content-Type: application/json

{
  "title": "Python Functions",
  "description": "Learn about functions",
  "content": "Functions are...",
  "content_type": "text"
}

Response:
{
  "project_id": 1,
  "status": "created",
  "message": "Project created successfully"
}
```

#### Get Projects
```
GET /api/v1/content/projects

Response:
[
  {
    "id": 1,
    "title": "Python Functions",
    "status": "completed",
    "created_at": "2025-12-07T..."
  }
]
```

### Video Endpoints

#### Generate Video
```
POST /api/v1/video/generate/{project_id}

Response:
{
  "task_id": "abc123",
  "status": "processing",
  "message": "Video generation started"
}
```

#### Get Task Status
```
GET /api/v1/status/task/{task_id}

Response:
{
  "task_id": "abc123",
  "status": "PROGRESS",
  "progress": 45,
  "message": "Generating audio...",
  "current_step": "video_composition"
}
```

---

## 📦 Services

### Azure OpenAI Service

```python
# app/services/azure_openai.py

class AzureOpenAIService:
    def __init__(self):
        self.client = AzureOpenAI(
            api_key=settings.AZURE_OPENAI_API_KEY,
            api_version="2024-02-15-preview",
            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT
        )
    
    async def analyze(self, content: str) -> dict:
        """Analyze content and extract key information"""
        response = self.client.chat.completions.create(
            model=settings.AZURE_OPENAI_DEPLOYMENT_NAME,
            messages=[
                {"role": "system", "content": "You are an educational content analyzer..."},
                {"role": "user", "content": f"Analyze: {content}"}
            ]
        )
        return parse_response(response)
    
    async def generate_script(self, analysis: dict) -> dict:
        """Generate video script from analysis"""
        # Similar implementation
        pass
```

---

### Azure Speech Service

```python
# app/services/azure_speech.py

class AzureSpeechService:
    async def synthesize(self, script: dict) -> str:
        """Convert text to speech"""
        speech_config = speechsdk.SpeechConfig(
            subscription=settings.AZURE_SPEECH_KEY,
            region=settings.AZURE_SPEECH_REGION
        )
        
        audio_config = speechsdk.audio.AudioOutputConfig(
            filename="output_audio.wav"
        )
        
        synthesizer = speechsdk.SpeechSynthesizer(
            speech_config=speech_config,
            audio_config=audio_config
        )
        
        # Synthesize narration
        for scene in script["scenes"]:
            result = synthesizer.speak_text_async(scene["narration"]).get()
        
        return "output_audio.wav"
```

---

### Video Service

```python
# app/services/video_service.py

class VideoService:
    def compose(self, scenes: list, images: list, audio: str) -> str:
        """Compose final video using MoviePy"""
        from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
        
        clips = []
        
        # Create video clips from images
        for scene, image in zip(scenes, images):
            clip = ImageClip(image["path"]).set_duration(scene["duration"])
            clips.append(clip)
        
        # Concatenate clips
        video = concatenate_videoclips(clips)
        
        # Add audio
        audio_clip = AudioFileClip(audio)
        video = video.set_audio(audio_clip)
        
        # Write to file
        output_path = "generated_video.mp4"
        video.write_videofile(output_path, verbose=False, logger=None)
        
        return output_path
```

---

## 🔐 Database Models

### User Model

```python
# app/models/user.py

class User(Base):
    __tablename__ = "users"
    
    id: int = Column(Integer, primary_key=True)
    email: str = Column(String, unique=True, index=True)
    hashed_password: str = Column(String)
    full_name: str = Column(String)
    created_at: datetime = Column(DateTime, default=datetime.utcnow)
    
    projects: list["Project"] = relationship("Project", back_populates="user")
```

### Project Model

```python
class Project(Base):
    __tablename__ = "projects"
    
    id: int = Column(Integer, primary_key=True)
    user_id: int = Column(Integer, ForeignKey("users.id"))
    title: str = Column(String)
    description: str = Column(String, nullable=True)
    content: str = Column(String)
    status: str = Column(String, default="created")
    created_at: datetime = Column(DateTime, default=datetime.utcnow)
    
    user: User = relationship("User", back_populates="projects")
    videos: list["Video"] = relationship("Video", back_populates="project")
```

### Video Model

```python
class Video(Base):
    __tablename__ = "videos"
    
    id: int = Column(Integer, primary_key=True)
    project_id: int = Column(Integer, ForeignKey("projects.id"))
    title: str = Column(String)
    file_url: str = Column(String)
    duration: int = Column(Integer)
    status: str = Column(String, default="processing")
    created_at: datetime = Column(DateTime, default=datetime.utcnow)
    
    project: Project = relationship("Project", back_populates="videos")
```

---

## 📋 Pydantic Schemas

```python
# app/schemas/content.py

class ContentUploadSchema(BaseModel):
    title: str
    description: Optional[str] = None
    content: str
    content_type: Optional[str] = "text"
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "Python Functions",
                "description": "Learn about functions",
                "content": "Functions are reusable blocks of code...",
                "content_type": "text"
            }
        }

class ProjectSchema(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True
```

---

## 🔄 Celery Task Queue

### Celery Configuration

```python
# app/core/celery_app.py

from celery import Celery
from app.config import settings

celery_app = Celery(
    "video_generator",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

@celery_app.task
async def generate_video_task(project_id: int):
    """Long-running video generation task"""
    # Run orchestrator workflow
    # Update progress in Redis
    # Save results to database
    pass
```

---

## 🔒 Security

### JWT Authentication

```python
# app/core/security.py

from datetime import datetime, timedelta
import jwt

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(hours=24)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return user_id
```

---

## 🧪 Testing

```python
# app/tests/test_api.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_upload_content():
    data = {
        "title": "Test Project",
        "content": "Test content..."
    }
    response = client.post("/api/v1/content/upload", json=data)
    assert response.status_code == 200
```

---

## 🚀 Deployment

### Docker

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Environment Variables

```bash
AZURE_OPENAI_ENDPOINT=https://...
AZURE_OPENAI_API_KEY=...
AZURE_SPEECH_KEY=...
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///./edu_video.db
REDIS_URL=redis://localhost:6379
```

---

## 📚 Resources

- **FastAPI:** https://fastapi.tiangolo.com
- **SQLAlchemy:** https://www.sqlalchemy.org
- **LangGraph:** https://github.com/langchain-ai/langgraph
- **Azure OpenAI:** https://learn.microsoft.com/en-us/azure/ai-services/openai
- **Celery:** https://docs.celeryproject.io
- **MoviePy:** https://zulko.github.io/moviepy

---

**Backend is ready to deploy! ⚙️**
