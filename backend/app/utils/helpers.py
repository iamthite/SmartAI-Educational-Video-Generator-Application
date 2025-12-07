"""Helper Utility Functions"""
import uuid
import logging

logger = logging.getLogger(__name__)

def generate_unique_id():
    """Generate unique ID"""
    return str(uuid.uuid4())

def log_info(message: str):
    """Log info message"""
    logger.info(message)

def log_error(message: str):
    """Log error message"""
    logger.error(message)
