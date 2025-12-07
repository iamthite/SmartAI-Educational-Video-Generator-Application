"""Main API Router"""
from fastapi import APIRouter
from app.api.v1 import content, video, status, auth

router = APIRouter()

router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
router.include_router(content.router, prefix="/content", tags=["Content"])
router.include_router(video.router, prefix="/video", tags=["Video"])
router.include_router(status.router, prefix="/status", tags=["Status"])




#=====================================================================

# from fastapi import APIRouter
# from app.api.v1 import content, video

# router = APIRouter()
# router.include_router(content.router, prefix="/content", tags=["Content"])
# router.include_router(video.router, prefix="/video", tags=["Video"])