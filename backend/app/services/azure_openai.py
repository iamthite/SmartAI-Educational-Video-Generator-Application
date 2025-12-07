"""Azure OpenAI Service"""
from openai import AzureOpenAI
from app.config import settings
import logging

logger = logging.getLogger(__name__)

class AzureOpenAIService:
    def __init__(self):
        self.client = AzureOpenAI(
            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
            api_key=settings.AZURE_OPENAI_API_KEY,
            api_version=settings.AZURE_OPENAI_API_VERSION
        )
    
    async def generate_text(self, prompt: str, max_tokens: int = 2000) -> str:
        """Generate text using Azure OpenAI"""
        try:
            response = self.client.chat.completions.create(
                model=settings.AZURE_OPENAI_DEPLOYMENT_NAME,
                messages=[
                    {"role": "system", "content": "You are an expert educational content creator."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Azure OpenAI error: {e}")
            raise
    
    async def generate_image_prompt(self, description: str) -> str:
        """Generate optimized DALL-E prompt"""
        prompt = f"""Create a detailed DALL-E prompt for an educational illustration:
        Description: {description}
        
        The prompt should be:
        - Clear and specific
        - Suitable for educational content
        - Professional and clean style
        - High quality and detailed
        """
        return await self.generate_text(prompt, max_tokens=150)
