import os, sys 
import numpy as np 
import pandas as pd 
from pathlib import Path
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
from src.exception import CustomException
from src.logger import logging


class ModelTrainer:

    def __init__(self, model_trainer_config:ModelTrainerConfig, data_ingestion_artifact: DataIngestionArtifact):
        self.model_trainer_config = model_trainer_config
        self.data_ingestion_artifact = data_ingestion_artifact

    def preprocess_images(self)->dict:
        try:
            images_dir = self.data_ingestion_artifact.output_dir
            
            train_datagen = ImageDataGenerator(
                
                rescale=1/255.,
                shear_range=0.2,
                zoom_range=0.2,
                horizontal_flip=True,
                preprocessing_function=preprocess_input
            )

            test_datagen = ImageDataGenerator(
                rescale=1/255.,
                preprocessing_function=preprocess_input
            )

            val_datagen = ImageDataGenerator(
                rescale=1/255.,
                preprocessing_function=preprocess_input
            )


            self.train_data = train_datagen.flow_from_directory(
                directory = images_dir+'//train',
                target_size = self.model_trainer_config.IMAGE_SIZE,
                batch_size = self.model_trainer_config.BATCH_SIZE,
                class_mode='categorical'
            )
            
            self.test_data = test_datagen.flow_from_directory(
                directory = images_dir+'//test',
                target_size = self.model_trainer_config.IMAGE_SIZE,
                batch_size = self.model_trainer_config.BATCH_SIZE,
                class_mode='categorical'
            )

            self.val_data = val_datagen.flow_from_directory(
                directory = images_dir+'//val',
                target_size = self.model_trainer_config.IMAGE_SIZE,
                batch_size = self.model_trainer_config.BATCH_SIZE,
                class_mode='categorical'
            )

            logging.info(f"Labels for the Images are: {self.train_data.class_indices}")
            self.class_names = self.train_data.class_indices

            dataset = {
                'train_data':self.train_data,
                'test_data':self.test_data,
                'val_data':self.val_data,
                'class_labels':self.class_names
                
            }
            return dataset
            

        except Exception as e:
            raise CustomException(e, sys)
        
    @classmethod
    def create_model(self,)->object:
        try:
            clf = Sequential()
            clf.add(Conv2D(32, kernel_size=(3,3), activation='relu', input_shape=(256,256,3)))
            clf.add(BatchNormalization())
            clf.add(MaxPooling2D(pool_size=(2,2), strides=2, padding='valid'))

            clf.add(Conv2D(64, kernel_size=(3,3), padding='valid', activation='relu'))
            clf.add(BatchNormalization())
            clf.add(MaxPooling2D(pool_size=(2,2), strides=2, padding='valid'))

            clf.add(Conv2D(128, kernel_size=(3,3), activation='relu'))
            clf.add(BatchNormalization())
            clf.add(MaxPooling2D(pool_size=(2,2), strides=2, padding='valid'))

            clf.add(Flatten())
            clf.add(Dense(128, activation='relu'))
            clf.add(Dropout(0.1))
            clf.add(Dense(64,activation='relu'))
            clf.add(Dropout(0.1))
            clf.add(Dense(3, activation='softmax'))

            # logging.info(f"{clf.summary()}")
            clf.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
            return clf
        except Exception as e:
            raise CustomException(e, sys)

    @staticmethod
    def save_model(path:Path, model:tf.keras.Model):
        model.save(path)

    def train(self,)-> ModelTrainerArtifact:
        try:
            model = self.create_model()
            data = self.preprocess_images()
            training_data = data['train_data']
            validation_data = data['val_data']
            

            model.fit(training_data, epochs=self.model_trainer_config.EPOCHS, validation_data=validation_data)
            self.save_model(path=self.model_trainer_config.trained_model_dir, model=model)
            self.save_model(path=self.model_trainer_config.prod_model_dir, model=model)

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_dir= self.model_trainer_config.trained_model_dir,
                prod_model_dir=self.model_trainer_config.prod_model_dir
            )

            
            return model_trainer_artifact

        except Exception as e:
            raise CustomException(e, sys)

            




        


        

