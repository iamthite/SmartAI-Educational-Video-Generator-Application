"""Custom Exceptions"""

class VideoGenerationError(Exception):
    """Raised when video generation fails"""
    pass

class ContentParsingError(Exception):
    """Raised when content parsing fails"""
    pass

class AzureServiceError(Exception):
    """Raised when Azure service fails"""
    pass
