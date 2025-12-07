"""File Handling Utilities"""
import os
import logging

logger = logging.getLogger(__name__)

class FileHandler:
    @staticmethod
    def save_file(file_path: str, content: bytes):
        """Save file to disk"""
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'wb') as f:
                f.write(content)
            return True
        except Exception as e:
            logger.error(f"File save error: {str(e)}")
            return False
    
    @staticmethod
    def read_file(file_path: str):
        """Read file from disk"""
        try:
            with open(file_path, 'rb') as f:
                return f.read()
        except Exception as e:
            logger.error(f"File read error: {str(e)}")
            return None
    
    @staticmethod
    def delete_file(file_path: str):
        """Delete file from disk"""
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
            return True
        except Exception as e:
            logger.error(f"File delete error: {str(e)}")
            return False
