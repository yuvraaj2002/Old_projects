import numpy as np
import pandas as pd
import os
import sys
import dill
import pickle
from src.exception import CustomException

# Function for saving


def save_object(file_path, obj):

    # Check if the directory already exists.
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Save the object to the file.
    with open(file_path, "wb") as file_obj:
        dill.dump(obj, file_obj)

# Function for loading


def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
