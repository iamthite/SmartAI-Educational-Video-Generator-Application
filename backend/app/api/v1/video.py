# ============================================
# backend/app/api/v1/video.py - ENHANCED WITH PROGRESS
# ============================================
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.video import ProjectCreate, VideoResponse, VideoProgress
from app.models.project import Project, Video, ProjectStatus
from app.services.websocket_manager import ConnectionManager, manager
import asyncio
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/generate/{project_id}")
async def generate_video(
    project_id: int,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    """Start video generation"""
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    project.status = ProjectStatus.ANALYZING
    project.progress = 0
    db.commit()
    
    # Start background task
    background_tasks.add_task(generate_video_task, project_id, str(project_id))
    
    return {
        "message": "Video generation started",
        "project_id": project_id,
        "websocket_url": f"/ws/{project_id}"
    }

async def generate_video_task(project_id: int, client_id: str):
    """Background task for video generation with progress updates"""
    from app.database import SessionLocal
    
    db = SessionLocal()
    
    try:
        project = db.query(Project).filter(Project.id == project_id).first()
        
        # Step 1: Content Analysis (0-20%)
        await manager.send_progress(client_id, 5, "analyzing", "Analyzing content structure...")
        await asyncio.sleep(2)
        project.status = ProjectStatus.ANALYZING
        project.progress = 10
        db.commit()
        
        await manager.send_progress(client_id, 15, "analyzing", "Identifying key concepts...")
        await asyncio.sleep(2)
        
        # Step 2: Script Generation (20-40%)
        await manager.send_progress(client_id, 25, "generating_script", "Creating video script...")
        project.status = ProjectStatus.GENERATING_SCRIPT
        project.progress = 30
        db.commit()
        await asyncio.sleep(3)
        
        await manager.send_progress(client_id, 35, "generating_script", "Structuring scenes...")
        await asyncio.sleep(2)
        
        # Step 3: Visual Creation (40-60%)
        await manager.send_progress(client_id, 45, "creating_visuals", "Generating diagrams...")
        project.status = ProjectStatus.CREATING_VISUALS
        project.progress = 50
        db.commit()
        await asyncio.sleep(3)
        
        await manager.send_progress(client_id, 55, "creating_visuals", "Creating illustrations...")
        await asyncio.sleep(2)
        
        # Step 4: Audio Generation (60-75%)
        await manager.send_progress(client_id, 65, "generating_audio", "Synthesizing narration...")
        project.status = ProjectStatus.GENERATING_AUDIO
        project.progress = 70
        db.commit()
        await asyncio.sleep(3)
        
        # Step 5: Video Composition (75-95%)
        await manager.send_progress(client_id, 80, "composing_video", "Composing video...")
        project.status = ProjectStatus.COMPOSING_VIDEO
        project.progress = 85
        db.commit()
        await asyncio.sleep(4)
        
        await manager.send_progress(client_id, 90, "composing_video", "Adding transitions...")
        await asyncio.sleep(2)
        
        # Step 6: Upload (95-100%)
        await manager.send_progress(client_id, 95, "uploading", "Uploading to cloud...")
        project.status = ProjectStatus.UPLOADING
        project.progress = 98
        db.commit()
        await asyncio.sleep(2)
        
        # Create video record
        video = Video(
            project_id=project_id,
            title=project.title,
            file_url=f"https://storage.example.com/videos/{project_id}.mp4",
            thumbnail_url=f"https://storage.example.com/thumbnails/{project_id}.jpg",
            duration=300,
            file_size=50.5,
            quality="1080p",
            status="completed"
        )
        db.add(video)
        
        project.status = ProjectStatus.COMPLETED
        project.progress = 100
        db.commit()
        
        await manager.send_progress(client_id, 100, "completed", "Video generation completed!")
        
    except Exception as e:
        logger.error(f"Video generation error: {e}")
        project.status = ProjectStatus.FAILED
        project.progress = 0
        db.commit()
        await manager.send_progress(client_id, 0, "failed", f"Generation failed: {str(e)}")
    
    finally:
        db.close()

@router.get("/projects/{project_id}/videos")
async def get_project_videos(project_id: int, db: Session = Depends(get_db)):
    """Get all videos for a project"""
    videos = db.query(Video).filter(Video.project_id == project_id).all()
    return videos

@router.get("/videos/{video_id}/download")
async def download_video(video_id: int, db: Session = Depends(get_db)):
    """Get video download URL"""
    video = db.query(Video).filter(Video.id == video_id).first()
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    
    video.downloads += 1
    db.commit()
    
    return {
        "download_url": video.file_url,
        "filename": f"{video.title}.mp4",
        "size": video.file_size
    }
#================================================================================


# from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
# from sqlalchemy.orm import Session
# from app.database import get_db
# from app.models.project import Project, Video, ProjectStatus
# from app.main import manager
# import asyncio
# import logging

# router = APIRouter()
# logger = logging.getLogger(__name__)

# @router.post("/generate/{project_id}")
# async def generate_video(project_id: int, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
#     project = db.query(Project).filter(Project.id == project_id).first()
#     if not project:
#         raise HTTPException(status_code=404, detail="Project not found")
#     project.status = ProjectStatus.ANALYZING
#     project.progress = 0
#     db.commit()
#     background_tasks.add_task(generate_video_task, project_id, str(project_id))
#     return {"message": "Video generation started", "project_id": project_id, "websocket_url": f"/ws/{project_id}"}

# async def generate_video_task(project_id: int, client_id: str):
#     from app.database import SessionLocal
#     db = SessionLocal()
#     try:
#         project = db.query(Project).filter(Project.id == project_id).first()
#         await manager.send_progress(client_id, 10, "analyzing", "Analyzing content...")
#         await asyncio.sleep(2)
#         await manager.send_progress(client_id, 30, "generating_script", "Creating script...")
#         await asyncio.sleep(3)
#         await manager.send_progress(client_id, 50, "creating_visuals", "Generating visuals...")
#         await asyncio.sleep(3)
#         await manager.send_progress(client_id, 70, "generating_audio", "Synthesizing audio...")
#         await asyncio.sleep(3)
#         await manager.send_progress(client_id, 90, "composing_video", "Composing video...")
#         await asyncio.sleep(2)
#         video = Video(
#             project_id=project_id,
#             title=project.title,
#             file_url=f"https://example.com/videos/{project_id}.mp4",
#             thumbnail_url=f"https://example.com/thumbnails/{project_id}.jpg",
#             duration=300,
#             file_size=50.5,
#             quality="1080p",
#             status="completed"
#         )
#         db.add(video)
#         project.status = ProjectStatus.COMPLETED
#         project.progress = 100
#         db.commit()
#         await manager.send_progress(client_id, 100, "completed", "Video generation completed!")
#     except Exception as e:
#         logger.error(f"Generation error: {e}")
#         project.status = ProjectStatus.FAILED
#         db.commit()
#     finally:
#         db.close()

# @router.get("/projects/{project_id}/videos")
# async def get_project_videos(project_id: int, db: Session = Depends(get_db)):
#     videos = db.query(Video).filter(Video.project_id == project_id).all()
#     return videos

# @router.get("/videos/{video_id}/download")
# async def download_video(video_id: int, db: Session = Depends(get_db)):
#     video = db.query(Video).filter(Video.id == video_id).first()
#     if not video:
#         raise HTTPException(status_code=404, detail="Video not found")
#     video.downloads += 1
#     db.commit()
#     return {"download_url": video.file_url, "filename": f"{video.title}.mp4", "size": video.file_size}