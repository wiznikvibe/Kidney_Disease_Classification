import os, sys 
from src.entity import config_entity, artifacts_entity
from src.components.data_ingestion import DataIngestion


if __name__ == '__main__':
    training_pipeline_config = config_entity.TrainingPipelineConfig()

    data_ingestion_config =config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
    data_ingestion = DataIngestion(data_ingestion_config)
    print(data_ingestion.initiate_data_ingestion())