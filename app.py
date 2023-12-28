import os, sys 
from src.entity import config_entity, artifacts_entity
from src.components.data_ingestion import DataIngestion
from src.components.model_trainer import ModelTrainer


if __name__ == '__main__':
    training_pipeline_config = config_entity.TrainingPipelineConfig()

    data_ingestion_config =config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
    data_ingestion = DataIngestion(data_ingestion_config)
    data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
    print(data_ingestion_artifact)

    model_trainer_config = config_entity.ModelTrainerConfig(training_pipeline_config=training_pipeline_config)
    model_trainer = ModelTrainer(model_trainer_config, data_ingestion_artifact)
    model_trainer_artifact = model_trainer.train() 
    print(model_trainer_artifact)