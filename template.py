import os 
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)

project_name = "src"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/s3_operations.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training_pipeline/__init__.py",
    f"{project_name}/constant/application.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifacts_entity.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/exception.py",
    f"{project_name}/logger.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/utils.py",
    "template/index.html",
    ".dockerignore",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"


]

for component in list_of_files:
    file_path = Path(component)
    filedir, filename =  os.path.split(file_path)

    if filedir != "" :
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory for: {filename}")

    if not(os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path, "w") as file:
            pass 

    else:
        logging.info("File Structure Generated")
