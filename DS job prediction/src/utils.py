import numpy as np
import pandas as pd
import os
import sys
import dill
from src.exception import CustomException


def save_object(file_path, obj):

    # Check if the directory already exists.
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Save the object to the file.
    with open(file_path, "wb") as file_obj:
        dill.dump(obj, file_obj)
