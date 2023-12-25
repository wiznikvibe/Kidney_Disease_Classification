import os 

ZIP_FILE_NAME = "kidney_image.zip"

class TrainingPipelineConfig:

    def __init__(self):
        self.artifact_dir = os.path.join(os.getcwd(), 'artifact')

class DataIngestionConfig:

    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        self.prefix = "https://drive.google.com/uc?/export=download&id="
        self.file_id = "1FbNVvl_QW2A2eeK8f0ho2OasEOdf2iL6"
        self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir, "data_ingestion")
        self.feature_store_dir = os.path.join(self.data_ingestion_dir,"feature_store",ZIP_FILE_NAME)
        self.data_unzip_dir = os.path.join(self.data_ingestion_dir, "data")
        
    