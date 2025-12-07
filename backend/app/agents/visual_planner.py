"""Visual Planning Agent"""
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from typing import List, Dict

class VisualPlannerAgent:
    def __init__(self, llm: AzureChatOpenAI):
        self.llm = llm
        
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an expert in educational visual design.
            Plan visual elements for each scene in the video script.
            
            For each scene, determine:
            1. Type of visual (diagram, illustration, text overlay, chart)
            2. Specific elements to show
            3. Color scheme and style
            4. Animations or transitions
            
            Script: {script}
            Analysis: {analysis}
            """),
            ("user", "Create a detailed visual plan.")
        ])
    
    async def plan(self, script: dict, analysis: dict) -> dict:
        """Plan visual elements for the video"""
        chain = self.prompt | self.llm
        
        result = await chain.ainvoke({
            "script": str(script),
            "analysis": str(analysis)
        })
        
        return self._parse_visual_plan(result.content, script)
    
    def _parse_visual_plan(self, plan_text: str, script: dict) -> dict:
        """Parse visual plan into structured format"""
        elements = []
        
        for scene in script.get("scenes", []):
            elements.append({
                "scene_number": scene["scene_number"],
                "type": "diagram",
                "description": scene.get("visual_description", ""),
                "style": "modern",
                "color_scheme": "blue_gradient"
            })
        
        return {
            "elements": elements,
            "overall_style": "professional",
            "transitions": "smooth_fade"
        }
