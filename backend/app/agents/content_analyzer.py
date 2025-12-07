"""Content Analysis Agent"""
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List

class ContentAnalysis(BaseModel):
    summary: str = Field(description="Brief summary of content")
    key_concepts: List[str] = Field(description="Main concepts to cover")
    difficulty_level: str = Field(description="beginner, intermediate, or advanced")
    estimated_duration: int = Field(description="Estimated video duration in seconds")
    topics: List[str] = Field(description="List of topics")
    target_audience: str = Field(description="Target audience description")

class ContentAnalyzerAgent:
    def __init__(self, llm: AzureChatOpenAI):
        self.llm = llm
        self.parser = PydanticOutputParser(pydantic_object=ContentAnalysis)
        
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an expert educational content analyzer. 
            Analyze the given content and extract key information for creating an educational video.
            
            {format_instructions}
            """),
            ("user", "{content}")
        ])
    
    async def analyze(self, content: str) -> dict:
        """Analyze content and extract structure"""
        chain = self.prompt | self.llm | self.parser
        
        result = await chain.ainvoke({
            "content": content,
            "format_instructions": self.parser.get_format_instructions()
        })
        
        return result.dict()
