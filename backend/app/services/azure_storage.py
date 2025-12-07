"""Azure Blob Storage Service"""
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from app.config import settings
import os
import logging
from datetime import datetime, timedelta
from azure.storage.blob import generate_blob_sas, BlobSasPermissions

logger = logging.getLogger(__name__)

class AzureStorageService:
    def __init__(self):
        self.blob_service_client = BlobServiceClient.from_connection_string(
            settings.AZURE_STORAGE_CONNECTION_STRING
        )
        self.container_name = settings.AZURE_STORAGE_CONTAINER_NAME
        self._ensure_container()
    
    def _ensure_container(self):
        """Ensure container exists"""
        try:
            container_client = self.blob_service_client.get_container_client(
                self.container_name
            )
            if not container_client.exists():
                container_client.create_container()
                logger.info(f"Container created: {self.container_name}")
        except Exception as e:
            logger.error(f"Container creation error: {e}")
    
    async def upload_file(
        self, 
        file_path: str, 
        blob_name: str = None
    ) -> str:
        """Upload file to Azure Blob Storage"""
        try:
            if blob_name is None:
                blob_name = os.path.basename(file_path)
            
            blob_client = self.blob_service_client.get_blob_client(
                container=self.container_name,
                blob=blob_name
            )
            
            with open(file_path, "rb") as data:
                blob_client.upload_blob(data, overwrite=True)
            
            blob_url = blob_client.url
            logger.info(f"File uploaded: {blob_url}")
            return blob_url
            
        except Exception as e:
            logger.error(f"File upload error: {e}")
            raise
    
    async def download_file(self, blob_name: str, download_path: str) -> str:
        """Download file from Azure Blob Storage"""
        try:
            blob_client = self.blob_service_client.get_blob_client(
                container=self.container_name,
                blob=blob_name
            )
            
            with open(download_path, "wb") as file:
                blob_data = blob_client.download_blob()
                file.write(blob_data.readall())
            
            logger.info(f"File downloaded: {download_path}")
            return download_path
            
        except Exception as e:
            logger.error(f"File download error: {e}")
            raise
    
    async def get_blob_url(self, blob_name: str, expiry_hours: int = 24) -> str:
        """Generate SAS URL for blob"""
        try:
            blob_client = self.blob_service_client.get_blob_client(
                container=self.container_name,
                blob=blob_name
            )
            
            # Generate SAS token
            sas_token = generate_blob_sas(
                account_name=blob_client.account_name,
                container_name=self.container_name,
                blob_name=blob_name,
                account_key=settings.AZURE_STORAGE_CONNECTION_STRING.split(';')[2].split('=')[1],
                permission=BlobSasPermissions(read=True),
                expiry=datetime.utcnow() + timedelta(hours=expiry_hours)
            )
            
            return f"{blob_client.url}?{sas_token}"
            
        except Exception as e:
            logger.error(f"SAS URL generation error: {e}")
            raise
    
    async def delete_blob(self, blob_name: str) -> bool:
        """Delete blob from storage"""
        try:
            blob_client = self.blob_service_client.get_blob_client(
                container=self.container_name,
                blob=blob_name
            )
            blob_client.delete_blob()
            logger.info(f"Blob deleted: {blob_name}")
            return True
            
        except Exception as e:
            logger.error(f"Blob deletion error: {e}")
            return False
