"""Diagram Generation Agent"""
import asyncio
from typing import List, Dict
from app.services.image_generator import ImageGeneratorService
from app.services.diagram_service import DiagramService

class DiagramGeneratorAgent:
    def __init__(self):
        self.image_service = ImageGeneratorService()
        self.diagram_service = DiagramService()
    
    async def generate_all(self, visual_plan: dict) -> List[Dict]:
        """Generate all visual assets based on the plan"""
        assets = []
        
        tasks = []
        for element in visual_plan.get("elements", []):
            if element["type"] == "diagram":
                tasks.append(self._generate_diagram(element))
            elif element["type"] == "illustration":
                tasks.append(self._generate_image(element))
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        for result in results:
            if isinstance(result, dict):
                assets.append(result)
        
        return assets
    
    async def _generate_diagram(self, element: dict) -> dict:
        """Generate a diagram"""
        diagram_path = await self.diagram_service.create_diagram(
            description=element["description"],
            style=element.get("style", "modern")
        )
        
        return {
            "type": "diagram",
            "scene_number": element["scene_number"],
            "path": diagram_path,
            "metadata": element
        }
    
    async def _generate_image(self, element: dict) -> dict:
        """Generate an AI image"""
        image_path = await self.image_service.generate_image(
            prompt=element["description"],
            style=element.get("style", "professional")
        )
        
        return {
            "type": "image",
            "scene_number": element["scene_number"],
            "path": image_path,
            "metadata": element
        }
