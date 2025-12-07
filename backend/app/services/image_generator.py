"""Image Generator Service using DALL-E"""
from openai import AzureOpenAI
from app.config import settings
import os
import httpx
import logging

logger = logging.getLogger(__name__)

class ImageGeneratorService:
    def __init__(self):
        self.client = AzureOpenAI(
            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
            api_key=settings.AZURE_OPENAI_API_KEY,
            api_version=settings.AZURE_OPENAI_API_VERSION
        )
        self.output_dir = "temp/images"
        os.makedirs(self.output_dir, exist_ok=True)
    
    async def generate_image(
        self, 
        prompt: str, 
        style: str = "professional",
        size: str = "1024x1024"
    ) -> str:
        """Generate image using DALL-E"""
        try:
            # Enhance prompt based on style
            enhanced_prompt = self._enhance_prompt(prompt, style)
            
            # Generate image
            result = self.client.images.generate(
                model="dall-e-3",
                prompt=enhanced_prompt,
                size=size,
                quality="standard",
                n=1
            )
            
            image_url = result.data[0].url
            
            # Download image
            image_path = await self._download_image(image_url)
            
            logger.info(f"Image generated: {image_path}")
            return image_path
            
        except Exception as e:
            logger.error(f"Image generation error: {e}")
            raise
    
    def _enhance_prompt(self, prompt: str, style: str) -> str:
        """Enhance prompt with style guidelines"""
        style_guides = {
            "professional": "professional, clean, modern design, high quality",
            "academic": "academic, educational, clear diagrams, technical",
            "casual": "friendly, approachable, colorful, engaging",
            "minimalist": "minimalist, simple, clean lines, white background"
        }
        
        style_guide = style_guides.get(style, style_guides["professional"])
        return f"{prompt}, {style_guide}, educational illustration"
    
    async def _download_image(self, url: str) -> str:
        """Download image from URL"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                response.raise_for_status()
                
                # Save image
                filename = f"img_{os.urandom(8).hex()}.png"
                filepath = os.path.join(self.output_dir, filename)
                
                with open(filepath, "wb") as f:
                    f.write(response.content)
                
                return filepath
                
        except Exception as e:
            logger.error(f"Image download error: {e}")
            raise
