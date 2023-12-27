import os, sys 
import gdown
import zipfile
import splitfolders
from src.exception import CustomException
from src.logger import logging 
from src.entity.config_entity import ZIP_FILE_NAME,DataIngestionConfig
from src.entity.artifacts_entity import DataIngestionArtifact


class DataIngestion:

    def __init__(self, data_ingestion_config:DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config

    def download_file(self)-> str:
        try:
            dataset_id = self.data_ingestion_config.file_id
            zip_file_dir = self.data_ingestion_config.feature_store_dir
            os.makedirs(self.data_ingestion_config.feature_store_dir, exist_ok=True)
            output_file_path = os.path.join(zip_file_dir, ZIP_FILE_NAME)

            logging.info(f"Downloading Data from {self.data_ingestion_config.prefix+dataset_id} into file {output_file_path}")

            gdown.download(self.data_ingestion_config.prefix+dataset_id, output_file_path)
            logging.info(f"Zip File extracted from link: {self.data_ingestion_config.prefix+dataset_id} into {output_file_path}")
            return output_file_path
        except Exception as e:
            raise CustomException(e, sys)

    
    def extract_zip_file(self, zip_file_path: str):
        unzip_file_dir = self.data_ingestion_config.data_unzip_dir
        os.makedirs(unzip_file_dir, exist_ok=True)
        logging.info(zip_file_path)
        with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
            zip_file.extractall(unzip_file_dir)

        return unzip_file_dir

    def train_test_val_split(self, image_directory:str):
        output_dir = os.path.join(self.data_ingestion_config.train_test_val_dir)
        splitfolders.ratio(image_directory, output=output_dir, seed=42, ratio=self.data_ingestion_config.split_ratio)
        return output_dir

    def initiate_data_ingestion(self,)-> DataIngestionArtifact:
        try:
            zip_file_path = self.download_file()
            feature_store_path = self.extract_zip_file(zip_file_path)
            train_test_val_path = self.train_test_val_split(feature_store_path)


            data_ingestion_artifact = DataIngestionArtifact(
                data_unzip_dir = feature_store_path,
                output_dir = train_test_val_path
            )   

            return data_ingestion_artifact    
        except Exception as e:
            raise CustomException(e, sys)
        