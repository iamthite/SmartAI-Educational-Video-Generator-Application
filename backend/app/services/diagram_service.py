"""Diagram Service for creating educational diagrams"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont
import os
import logging

logger = logging.getLogger(__name__)

class DiagramService:
    def __init__(self):
        self.output_dir = "temp/diagrams"
        os.makedirs(self.output_dir, exist_ok=True)
    
    async def create_diagram(
        self, 
        description: str, 
        style: str = "modern"
    ) -> str:
        """Create a diagram based on description"""
        try:
            # Simple diagram creation
            # In production, use more sophisticated diagram generation
            filename = f"diagram_{os.urandom(8).hex()}.png"
            filepath = os.path.join(self.output_dir, filename)
            
            # Create simple diagram using matplotlib
            fig, ax = plt.subplots(figsize=(10, 6))
            
            # Add text
            ax.text(
                0.5, 0.5, 
                description[:100],
                ha='center', 
                va='center',
                fontsize=14,
                wrap=True
            )
            
            # Style the diagram
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.axis('off')
            
            plt.tight_layout()
            plt.savefig(filepath, dpi=150, bbox_inches='tight')
            plt.close()
            
            logger.info(f"Diagram created: {filepath}")
            return filepath
            
        except Exception as e:
            logger.error(f"Diagram creation error: {e}")
            raise
    
    async def create_flowchart(self, steps: list) -> str:
        """Create a flowchart"""
        filename = f"flowchart_{os.urandom(8).hex()}.png"
        filepath = os.path.join(self.output_dir, filename)
        
        fig, ax = plt.subplots(figsize=(8, len(steps) * 2))
        
        y_pos = 0.9
        for i, step in enumerate(steps):
            # Draw box
            rect = patches.FancyBboxPatch(
                (0.2, y_pos), 0.6, 0.1,
                boxstyle="round,pad=0.01",
                edgecolor='blue',
                facecolor='lightblue'
            )
            ax.add_patch(rect)
            
            # Add text
            ax.text(0.5, y_pos + 0.05, step, ha='center', va='center')
            
            # Draw arrow
            if i < len(steps) - 1:
                ax.arrow(0.5, y_pos, 0, -0.15, head_width=0.05, head_length=0.02)
            
            y_pos -= 0.2
        
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        
        plt.tight_layout()
        plt.savefig(filepath, dpi=150, bbox_inches='tight')
        plt.close()
        
        return filepath
