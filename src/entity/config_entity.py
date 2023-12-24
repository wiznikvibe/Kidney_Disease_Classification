import os 

ZIP_FILE_NAME = "KidneyData.csv.zip"

class TrainingPipelineConfig:

    def __init__(self):
        self.artifact_dir = os.path.join(os.getcwd(), 'artifact')

class DataIngestionConfig:

    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        self.dataset_link = "https://drive.google.com/uc?/export=download&id=1bFoB56I-fUhNz25DZY7xoLODUj6HE9qQ"
        self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir, "data_ingestion")
        self.feature_store_dir = os.path.join(self.data_ingestion_dir,"feature_store",ZIP_FILE_NAME)
        self.data_unzip_dir = self.data_ingestion_dir
        
    