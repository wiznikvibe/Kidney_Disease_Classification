import os, sys 
import gdown
import zipfile
from src.exception import CustomException
from src.logger import logging 
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifacts_entity import DataIngestionArtifact


class DataIngestion:

    def __init__(self, data_ingestion_config:DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config

    def download_file(self)-> str:
        try:
            dataset_url = self.data_ingestion_config.dataset_link
            zip_file_dir = self.data_ingestion_config.feature_store_dir
            os.makedirs(self.data_ingestion_config.feature_store_dir, exist_ok=True)

            logging.info(f"Downloading Data from {dataset_url} into file {zip_file_dir}")
            gdown.download(dataset_url, zip_file_dir)
            logging.info(f"Zip File extracted from link: {dataset_url} into {zip_file_dir}")
            return zip_file_dir
        except Exception as e:
            raise CustomException(e, sys)

    
    def extract_zip_file(self, zip_file_path: str):
        unzip_file_dir = self.data_ingestion_config.data_unzip_dir
        os.makedirs(unzip_file_dir, exist_ok=True)
        with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
            zip_file.extractall(unzip_file_dir)

        return unzip_file_dir

    def initiate_data_ingestion(self,)-> DataIngestionArtifact:
        try:
            zip_file_path = self.download_file()
            feature_store_path = self.extract_zip_file(zip_file_path)

            data_ingestion_artifact = DataIngestionArtifact(
                data_unzip_dir = feature_store_path
            )   

            return data_ingestion_artifact    
        except Exception as e:
            raise CustomException(e, sys)
        