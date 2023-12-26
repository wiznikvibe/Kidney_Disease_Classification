import os, sys 
from src.entity.config_entity import  ModelTrainerConfig
from src.entity.artifacts_entity import DataIngestionArtifact, ModelTrainerArtifact


class ModelTrainer:

    def __init__(self, model_trainer_config:ModelTrainerConfig, data_ingestion_artifact: DataIngestionArtifact):
        self.model_trainer_config = model_trainer_config
        self.data_ingestion_artifact = data_ingestion_artifact

    def preprocess_images(data_path: str) :
        pass 