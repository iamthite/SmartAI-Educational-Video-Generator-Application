

# ============================================
# backend/app/api/v1/content.py - ENHANCED
# ============================================
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.video import ContentUpload, ProjectCreate, ProjectResponse
from app.models.project import Project, ProjectStatus
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/upload")
async def upload_content(content: ContentUpload, db: Session = Depends(get_db)):
    """Upload text content"""
    try:
        config_dict = content.config.dict() if content.config else {}
        
        project = Project(
            user_id=1,
            title=content.title,
            description=content.description,
            content=content.content,
            status=ProjectStatus.CREATED,
            progress=0,
            config=config_dict
        )
        
        db.add(project)
        db.commit()
        db.refresh(project)
        
        return {
            "message": "Content uploaded successfully",
            "project_id": project.id,
            "status": project.status
        }
    except Exception as e:
        logger.error(f"Upload error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/upload-file")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """Upload document file"""
    try:
        from app.services.document_parser import DocumentParser
        
        content = await file.read()
        parser = DocumentParser()
        
        if file.filename.endswith('.pdf'):
            text = parser._parse_pdf(content)
        elif file.filename.endswith('.docx'):
            text = parser._parse_docx(content)
        elif file.filename.endswith('.txt'):
            text = content.decode('utf-8')
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type")
        
        project = Project(
            user_id=1,
            title=file.filename,
            content=text,
            status=ProjectStatus.CREATED
        )
        
        db.add(project)
        db.commit()
        db.refresh(project)
        
        return {
            "message": "File uploaded successfully",
            "project_id": project.id,
            "filename": file.filename,
            "content_length": len(text)
        }
    except Exception as e:
        logger.error(f"File upload error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/projects")
async def get_projects(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    """Get all projects"""
    projects = db.query(Project).order_by(Project.created_at.desc()).offset(skip).limit(limit).all()
    return projects

@router.get("/projects/{project_id}")
async def get_project(project_id: int, db: Session = Depends(get_db)):
    """Get project by ID"""
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.delete("/projects/{project_id}")
async def delete_project(project_id: int, db: Session = Depends(get_db)):
    """Delete project"""
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    db.delete(project)
    db.commit()
    
    return {"message": "Project deleted successfully"}

#================================================================================

# from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app.database import get_db
# from app.models.project import Project, ProjectStatus
# import logging

# router = APIRouter()
# logger = logging.getLogger(__name__)

# @router.post("/upload")
# async def upload_content(
#     title: str,
#     content: str,
#     description: str = None,
#     db: Session = Depends(get_db)
# ):
#     try:
#         project = Project(
#             user_id=1,
#             title=title,
#             description=description,
#             content=content,
#             status=ProjectStatus.CREATED,
#             progress=0
#         )
#         db.add(project)
#         db.commit()
#         db.refresh(project)
#         return {"message": "Content uploaded successfully", "project_id": project.id}
#     except Exception as e:
#         logger.error(f"Upload error: {e}")
#         raise HTTPException(status_code=500, detail=str(e))

# @router.get("/projects")
# async def get_projects(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
#     projects = db.query(Project).order_by(Project.created_at.desc()).offset(skip).limit(limit).all()
#     return projects

# @router.get("/projects/{project_id}")
# async def get_project(project_id: int, db: Session = Depends(get_db)):
#     project = db.query(Project).filter(Project.id == project_id).first()
#     if not project:
#         raise HTTPException(status_code=404, detail="Project not found")
#     return project