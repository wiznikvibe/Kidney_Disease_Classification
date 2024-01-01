from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image

app = FastAPI()

def read_file_as_image(data)->np.ndarray:
    imagebytes = np.array(Image.open(BytesIO(data)))
    return imagebytes


@app.get("/")
async def home():
    return "This is Home"


@app.post("/predict")
async def predict(file: UploadFile=File(...)):
    image = read_file_as_image(await file.read())
    
    return f"{image}"






if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)