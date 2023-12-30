import os, sys
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from src.pipeline.training_pipeline import initiate_training_pipeline


if __name__== "__main__":
    initiate_training_pipeline()