import os 

ZIP_FILE_NAME = "kidney_image.zip"
MODEL_FILE_NAME = "classifier.h5"



class TrainingPipelineConfig:

    def __init__(self):
        self.artifact_dir = os.path.join(os.getcwd(), 'artifact')

class DataIngestionConfig:

    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        self.prefix = "https://drive.google.com/uc?/export=download&id="
        self.file_id = "1FbNVvl_QW2A2eeK8f0ho2OasEOdf2iL6"
        self.split_ratio = (0.7, 0.2, 0.1)
        self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir, "data_ingestion")
        self.feature_store_dir = os.path.join(self.data_ingestion_dir,"feature_store",ZIP_FILE_NAME)
        self.data_unzip_dir = os.path.join(self.data_ingestion_dir, "data")
        self.train_test_val_dir = os.path.join(self.data_ingestion_dir,"train_test_val")
        

        
class ModelTrainerConfig:

    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        self.model_trainer_dir = os.path.join(training_pipeline_config.artifact_dir, "model_trainer")
        self.trained_model_dir = os.path.join(self.model_trainer_dir, 'model', MODEL_FILE_NAME)
        self.prod_model_dir = os.path.join(os.getcwd(), 'saved_model', MODEL_FILE_NAME)
        self.train_data_dir = os.path.join(self.model_trainer_dir,"training_data")
        self.categories = ['Cyst','Normal', 'Tumor']
        self.IMAGE_SIZE = (256, 256)
        self.BATCH_SIZE = 32
        self.EPOCHS = 5

