"""Video Composition Agent"""
from app.services.video_service import VideoService
import logging

logger = logging.getLogger(__name__)

class VideoComposer:
    def __init__(self):
        self.video_service = VideoService()
    
    async def compose(self, script: dict, assets: list, visual_plan: dict) -> str:
        """Compose final video from assets"""
        try:
            logger.info("Starting video composition...")
            
            # Compose video from script, assets and visual plan
            video_path = await self.video_service.render(
                script=script,
                assets=assets,
                visual_plan=visual_plan
            )
            
            logger.info(f"Video composition completed: {video_path}")
            return video_path
            
        except Exception as e:
            logger.error(f"Video composition error: {e}")
            raise
