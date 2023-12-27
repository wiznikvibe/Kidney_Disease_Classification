from dataclasses import dataclass 

@dataclass
class DataIngestionArtifact:
    data_unzip_dir: str
    output_dir: str

@dataclass 
class ModelTrainerArtifact:
    
    trained_model_dir: str
    prod_model_dir: str