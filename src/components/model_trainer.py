import os, sys 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import tensorflow as tf 
from tensorflow import keras 
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.vgg16 import preprocess_input
from keras import Sequential
from keras.layers import Dense,Conv2D,MaxPooling2D,Flatten,BatchNormalization,Dropout
from src.entity.config_entity import  ModelTrainerConfig
from src.entity.artifacts_entity import DataIngestionArtifact, ModelTrainerArtifact



class ModelTrainer:

    def __init__(self, model_trainer_config:ModelTrainerConfig, data_ingestion_artifact: DataIngestionArtifact):
        self.model_trainer_config = model_trainer_config
        self.data_ingestion_artifact = data_ingestion_artifact

    def preprocess_images(self):
        try:
            images_dir = self.data_ingestion_artifact.output_dir
            
            self.train_datagen = ImageDataGenerator(
                rescale=1/255.,
                shear_range=0.2,
                zoom_range=0.2,
                horizontal_flip=True,
                preprocessing_function=preprocess_input
            )

            self.test_datagen = ImageDataGenerator(
                rescale=1/255.,
                preprocessing_function=preprocess_input
            )

            self.val_datagen = ImageDataGenerator(
                rescale=1/255.,
                preprocessing_function=preprocess_input
            )


            train_data = self.train_datagen.flow_from_directory(
                directory = images_dir+'//train',
                target_size = self.model_trainer_config.IMAGE_SIZE,
                batch_size = self.model_trainer_config.BATCH_SIZE,
                class_mode='categorical'
            )
            
            test_data = self.test_datagen.flow_from_directory(
                directory = images_dir+'//test',
                target_size = self.model_trainer_config.IMAGE_SIZE,
                batch_size = self.model_trainer_config.BATCH_SIZE,
                class_mode='categorical'
            )

            val_data = self.val_datagen.flow_from_directory(
                directory = images_dir+'//val',
                target_size = self.model_trainer_config.IMAGE_SIZE,
                batch_size = self.model_trainer_config.BATCH_SIZE,
                class_mode='categorical'
            )

            train_data_path = os.path.join(self.model_trainer_config.train_data_dir, train_data)
            test_data_path = os.path.join(self.model_trainer_config.train_data_dir, test_data)
            val_data_path = os.path.join(self.model_trainer_config.train_data_dir, val_data)


        except Exception as e:
            raise CustomException(e, sys)
        