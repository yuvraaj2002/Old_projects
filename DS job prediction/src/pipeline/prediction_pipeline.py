import sys
import pandas as pd
import os
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            # Path for the model and preprocessor pickle file
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')

            # Loading the model and preprocessor using the path
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            # Applying transformation
            data_scaled = preprocessor.transform(features)

            # Making predictions
            preds = model.predict(data_scaled)
            return preds

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self,
                 city_development_index: float,
                 gender: str,
                 relevent_experience: str,
                 enrolled_university: str,
                 education_level: str,
                 major_discipline: str,
                 experience: int,
                 company_size: str,
                 company_type: str,
                 training_hours: int):

        self.city_development_index = city_development_index
        self.gender = gender
        self.relevent_experience = relevent_experience
        self.enrolled_university = enrolled_university
        self.education_level = education_level
        self.major_discipline = major_discipline
        self.experience = experience
        self.company_size = company_size
        self.company_type = company_type
        self.training_hours = training_hours

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "city_development_index": [self.city_development_index],
                "gender": [self.gender],
                "relevent_experience": [self.relevent_experience],
                "enrolled_university": [self.enrolled_university],
                "education_level": [self.education_level],
                "major_discipline": [self.major_discipline],
                "experience": [self.experience],
                "company_size": [self.company_size],
                "company_type": [self.company_type],
                "training_hours": [self.training_hours],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
