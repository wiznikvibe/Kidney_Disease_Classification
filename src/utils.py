import os, sys 
from box.exceptions import BoxValueError
import yaml 
from src.logger import logging
from src.exception import CustomException
import json
import joblib 
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path 
from typing import Any 
import base64


@ensure_annotations
def read_yaml(file_path: Path)-> ConfigBox:

    try:
        with open(file_path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml_file: {file_path} loaded successfully")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise CustomException(e, sys)


@ensure_annotations
def create_directories(path_list: list, verbose=True):
    
    for path in path_list:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path:Path, data:dict):

    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logging.info(f"Json File Saved At: { path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:

    with open(path) as f:
        content = json.load(f)

    logging.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content) 

@ensure_annotations
def save_bin(data:Any, path: Path):
    joblib.dump(value=data, filename=path)
    logging.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bins(path:Path)-> Any:
    data = joblib.load(path)
    logging.info(f"Binary file loaded from: {path}")
    return data 

@ensure_annotations
def get_size(path: Path) -> str:
    size_kbs = round(os.path.getsize(path)/1024)
    return f"~ {size_kbs} KB"

def decodeImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, "wb") as f:
        f.write(imgdata)
        f.close()

def encodeImgIntoBase64(croppedImgPath):
    with open(croppedImgPath, "rb") as f:
        return base64.b64encode(f.read())