"""Video Rendering Service using MoviePy"""
from moviepy.editor import (
    VideoFileClip, ImageClip, TextClip, AudioFileClip,
    CompositeVideoClip, concatenate_videoclips
)
from app.services.azure_speech import AzureSpeechService
from app.services.azure_storage import AzureStorageService
import os
import logging
from typing import List, Dict

logger = logging.getLogger(__name__)

class VideoComposer:
    def __init__(self):
        self.speech_service = AzureSpeechService()
        self.storage_service = AzureStorageService()
        self.output_dir = "temp/videos"
        os.makedirs(self.output_dir, exist_ok=True)
    
    async def compose(
        self, 
        script: dict, 
        assets: List[Dict],
        visual_plan: dict
    ) -> str:
        """Compose final video from script and assets"""
        try:
            clips = []
            
            for scene in script.get("scenes", []):
                scene_clip = await self._create_scene_clip(scene, assets)
                if scene_clip:
                    clips.append(scene_clip)
            
            # Concatenate all clips
            if clips:
                final_video = concatenate_videoclips(clips, method="compose")
                
                # Export video
                output_filename = f"video_{os.urandom(8).hex()}.mp4"
                output_path = os.path.join(self.output_dir, output_filename)
                
                final_video.write_videofile(
                    output_path,
                    fps=24,
                    codec='libx264',
                    audio_codec='aac'
                )
                
                # Upload to Azure Storage
                blob_url = await self.storage_service.upload_file(
                    output_path,
                    output_filename
                )
                
                logger.info(f"Video composed and uploaded: {blob_url}")
                return blob_url
            
            raise Exception("No clips generated")
            
        except Exception as e:
            logger.error(f"Video composition error: {e}")
            raise
    
    async def _create_scene_clip(
        self, 
        scene: dict, 
        assets: List[Dict]
    ) -> VideoFileClip:
        """Create a video clip for a single scene"""
        try:
            duration = scene.get("duration", 5)
            narration = scene.get("narration", "")
            
            # Generate audio
            audio_path = await self._generate_audio(narration, scene["scene_number"])
            
            # Find matching visual asset
            scene_assets = [
                a for a in assets 
                if a.get("scene_number") == scene["scene_number"]
            ]
            
            if scene_assets:
                # Use first matching asset
                asset = scene_assets[0]
                image_clip = ImageClip(asset["path"]).set_duration(duration)
            else:
                # Create default background
                image_clip = self._create_default_background(duration)
            
            # Add text overlay
            text_clip = self._create_text_overlay(
                scene.get("key_points", [""])[0] if scene.get("key_points") else "",
                duration
            )
            
            # Combine visual and text
            video = CompositeVideoClip([image_clip, text_clip])
            
            # Add audio
            if os.path.exists(audio_path):
                audio = AudioFileClip(audio_path)
                video = video.set_audio(audio)
            
            return video
            
        except Exception as e:
            logger.error(f"Scene clip creation error: {e}")
            return None
    
    async def _generate_audio(self, text: str, scene_number: int) -> str:
        """Generate audio for narration"""
        audio_filename = f"audio_scene_{scene_number}.wav"
        audio_path = os.path.join(self.output_dir, audio_filename)
        
        await self.speech_service.text_to_speech(text, audio_path)
        return audio_path
    
    def _create_default_background(self, duration: int) -> ImageClip:
        """Create default background clip"""
        # Create a simple colored background
        from PIL import Image
        import numpy as np
        
        img = Image.new('RGB', (1920, 1080), color=(30, 30, 50))
        img_array = np.array(img)
        
        return ImageClip(img_array).set_duration(duration)
    
    def _create_text_overlay(self, text: str, duration: int) -> TextClip:
        """Create text overlay"""
        if not text:
            # Return transparent clip
            return TextClip("", fontsize=1, color='white').set_duration(duration)
        
        return TextClip(
            text,
            fontsize=40,
            color='white',
            font='Arial',
            size=(1600, None),
            method='caption'
        ).set_position(('center', 'bottom')).set_duration(duration)
