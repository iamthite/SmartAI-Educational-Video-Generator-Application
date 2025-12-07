"""Main Agent Orchestrator using LangGraph"""
from typing import TypedDict, Annotated, Sequence
from langgraph.graph import StateGraph, END
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
import operator
from app.config import settings
from app.agents.content_analyzer import ContentAnalyzerAgent
from app.agents.script_generator import ScriptGeneratorAgent
from app.agents.visual_planner import VisualPlannerAgent
from app.agents.diagram_generator import DiagramGeneratorAgent
from app.core.celery_app import celery_app
from celery import shared_task
import logging

logger = logging.getLogger(__name__)

# Define the state for our graph
class VideoGenerationState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    content: str
    analysis: dict
    script: dict
    visual_plan: dict
    assets: list
    video_path: str
    status: str
    error: str | None

class VideoGeneratorOrchestrator:
    def __init__(self):
        self.llm = AzureChatOpenAI(
            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
            api_key=settings.AZURE_OPENAI_API_KEY,
            azure_deployment=settings.AZURE_OPENAI_DEPLOYMENT_NAME,
            api_version=settings.AZURE_OPENAI_API_VERSION,
            temperature=0.7
        )
        
        self.content_analyzer = ContentAnalyzerAgent(self.llm)
        self.script_generator = ScriptGeneratorAgent(self.llm)
        self.visual_planner = VisualPlannerAgent(self.llm)
        self.diagram_generator = DiagramGeneratorAgent()
        
        self.workflow = self.create_workflow()
    
    def create_workflow(self) -> StateGraph:
        """Create the LangGraph workflow"""
        workflow = StateGraph(VideoGenerationState)
        
        # Add nodes
        workflow.add_node("analyze_content", self.analyze_content_node)
        workflow.add_node("generate_script", self.generate_script_node)
        workflow.add_node("plan_visuals", self.plan_visuals_node)
        workflow.add_node("generate_assets", self.generate_assets_node)
        workflow.add_node("compose_video", self.compose_video_node)
        
        # Define edges
        workflow.set_entry_point("analyze_content")
        workflow.add_edge("analyze_content", "generate_script")
        workflow.add_edge("generate_script", "plan_visuals")
        workflow.add_edge("plan_visuals", "generate_assets")
        workflow.add_edge("generate_assets", "compose_video")
        workflow.add_edge("compose_video", END)
        
        return workflow.compile()
    
    async def analyze_content_node(self, state: VideoGenerationState) -> VideoGenerationState:
        """Analyze input content"""
        logger.info("Starting content analysis...")
        try:
            analysis = await self.content_analyzer.analyze(state["content"])
            state["analysis"] = analysis
            state["status"] = "content_analyzed"
            state["messages"].append(
                AIMessage(content=f"Content analyzed: {analysis['summary']}")
            )
        except Exception as e:
            logger.error(f"Content analysis error: {e}")
            state["error"] = str(e)
            state["status"] = "failed"
        
        return state
    
    async def generate_script_node(self, state: VideoGenerationState) -> VideoGenerationState:
        """Generate video script"""
        logger.info("Generating script...")
        try:
            script = await self.script_generator.generate(
                content=state["content"],
                analysis=state["analysis"]
            )
            state["script"] = script
            state["status"] = "script_generated"
            state["messages"].append(
                AIMessage(content=f"Script generated with {len(script['scenes'])} scenes")
            )
        except Exception as e:
            logger.error(f"Script generation error: {e}")
            state["error"] = str(e)
            state["status"] = "failed"
        
        return state
    
    async def plan_visuals_node(self, state: VideoGenerationState) -> VideoGenerationState:
        """Plan visual elements"""
        logger.info("Planning visuals...")
        try:
            visual_plan = await self.visual_planner.plan(
                script=state["script"],
                analysis=state["analysis"]
            )
            state["visual_plan"] = visual_plan
            state["status"] = "visuals_planned"
            state["messages"].append(
                AIMessage(content=f"Visual plan created with {len(visual_plan['elements'])} elements")
            )
        except Exception as e:
            logger.error(f"Visual planning error: {e}")
            state["error"] = str(e)
            state["status"] = "failed"
        
        return state
    
    async def generate_assets_node(self, state: VideoGenerationState) -> VideoGenerationState:
        """Generate all visual assets"""
        logger.info("Generating assets...")
        try:
            assets = await self.diagram_generator.generate_all(
                visual_plan=state["visual_plan"]
            )
            state["assets"] = assets
            state["status"] = "assets_generated"
            state["messages"].append(
                AIMessage(content=f"Generated {len(assets)} assets")
            )
        except Exception as e:
            logger.error(f"Asset generation error: {e}")
            state["error"] = str(e)
            state["status"] = "failed"
        
        return state
    
    async def compose_video_node(self, state: VideoGenerationState) -> VideoGenerationState:
        """Compose final video"""
        logger.info("Composing video...")
        try:
            from app.services.video_service import VideoComposer
            composer = VideoComposer()
            video_path = await composer.compose(
                script=state["script"],
                assets=state["assets"],
                visual_plan=state["visual_plan"]
            )
            state["video_path"] = video_path
            state["status"] = "completed"
            state["messages"].append(
                AIMessage(content=f"Video completed: {video_path}")
            )
        except Exception as e:
            logger.error(f"Video composition error: {e}")
            state["error"] = str(e)
            state["status"] = "failed"
        
        return state
    
    async def generate_video(self, content: str, config: dict = None) -> dict:
        """Main entry point for video generation"""
        initial_state = VideoGenerationState(
            messages=[HumanMessage(content=content)],
            content=content,
            analysis={},
            script={},
            visual_plan={},
            assets=[],
            video_path="",
            status="started",
            error=None
        )
        
        final_state = await self.workflow.ainvoke(initial_state)
        
        return {
            "status": final_state["status"],
            "video_path": final_state.get("video_path"),
            "error": final_state.get("error"),
            "script": final_state.get("script"),
            "assets": final_state.get("assets")
        }

@shared_task
def orchestrate_video_generation(project_id: int, content: str):
    """Celery task for video generation"""
    orchestrator = VideoGeneratorOrchestrator()
    return {"project_id": project_id, "status": "processing"}
