import os 
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)

project_name = "src"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/config/configuration.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html", 
    "test.py"


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
