from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
import numpy as np
from io import BytesIO
import tensorflow as tf
from PIL import Image

app = FastAPI()

model = tf.keras.models.load_model('./saved_model/classifier.h5')

CLASS_LABELS = ['Cyst', 'Normal', 'Tumor']

def preprocess_image(img):
    img = img.resize((256,256))
    img_array = np.array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array



@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile=File(...)):
    try:
        contents = await file.read()
        img = Image.open(BytesIO(contents))

        img_array = preprocess_image(img)

        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions[0])
        confidence = predictions[0][predicted_class]
        
        return {"Classified as":f"{CLASS_LABELS[predicted_class]}", "Confidence level":f"{confidence:.2%}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))






if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)