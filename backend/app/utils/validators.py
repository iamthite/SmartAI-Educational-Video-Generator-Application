"""Validation Utilities"""

class Validators:
    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate email format"""
        return "@" in email and "." in email
    
    @staticmethod
    def validate_file_extension(filename: str, allowed: list) -> bool:
        """Validate file extension"""
        ext = filename.split('.')[-1].lower()
        return f".{ext}" in allowed
    
    @staticmethod
    def validate_file_size(file_size: int, max_size: int) -> bool:
        """Validate file size"""
        return file_size <= max_size
