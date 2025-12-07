"""Script Generation Agent"""
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from typing import List

class Scene(BaseModel):
    scene_number: int
    narration: str = Field(description="What the narrator says")
    duration: int = Field(description="Duration in seconds")
    visual_description: str = Field(description="Description of visual elements needed")
    key_points: List[str] = Field(description="Key points covered")

class VideoScript(BaseModel):
    title: str
    introduction: str
    scenes: List[Scene]
    conclusion: str
    total_duration: int

class ScriptGeneratorAgent:
    def __init__(self, llm: AzureChatOpenAI):
        self.llm = llm
        
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an expert educational video scriptwriter.
            Create an engaging, clear, and well-structured script for an educational video.
            
            Requirements:
            - Clear introduction that hooks the viewer
            - Well-paced narration (around 150 words per minute)
            - Logical flow between concepts
            - Visual descriptions for each scene
            - Strong conclusion that reinforces learning
            
            Content: {content}
            Analysis: {analysis}
            
            Generate a detailed script with scenes.
            """),
            ("user", "Generate the video script.")
        ])
    
    async def generate(self, content: str, analysis: dict) -> dict:
        """Generate video script"""
        chain = self.prompt | self.llm
        
        result = await chain.ainvoke({
            "content": content,
            "analysis": str(analysis)
        })
        
        # Parse the result into structured format
        # In production, use structured output or JSON mode
        return self._parse_script(result.content)
    
    def _parse_script(self, script_text: str) -> dict:
        """Parse script text into structured format"""
        # Simplified parsing - in production use LLM JSON mode
        return {
            "title": "Educational Video",
            "introduction": script_text[:200],
            "scenes": [
                {
                    "scene_number": 1,
                    "narration": script_text,
                    "duration": 30,
                    "visual_description": "Relevant visuals",
                    "key_points": ["Main concept"]
                }
            ],
            "conclusion": "Summary",
            "total_duration": 300
        }
