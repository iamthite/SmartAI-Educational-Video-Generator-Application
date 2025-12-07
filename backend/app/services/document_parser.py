"""Document Parser Service"""
from fastapi import UploadFile
import PyPDF2
from docx import Document
import io
import logging

logger = logging.getLogger(__name__)

class DocumentParser:
    async def parse_file(self, file: UploadFile) -> str:
        """Parse uploaded document"""
        try:
            content = await file.read()
            
            if file.filename.endswith('.pdf'):
                return self._parse_pdf(content)
            elif file.filename.endswith('.docx'):
                return self._parse_docx(content)
            elif file.filename.endswith('.txt'):
                return content.decode('utf-8')
            else:
                raise ValueError("Unsupported file type")
        except Exception as e:
            logger.error(f"Document parsing error: {e}")
            raise
    
    def _parse_pdf(self, content: bytes) -> str:
        """Parse PDF content"""
        try:
            pdf_file = io.BytesIO(content)
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            
            return text
        except Exception as e:
            logger.error(f"PDF parsing error: {e}")
            raise
    
    def _parse_docx(self, content: bytes) -> str:
        """Parse DOCX content"""
        try:
            docx_file = io.BytesIO(content)
            doc = Document(docx_file)
            
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            
            return text
        except Exception as e:
            logger.error(f"DOCX parsing error: {e}")
            raise
