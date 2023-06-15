import os
import sys
from dataclasses import dataclass
from sklearn.ensemble import RandomForestClassifier
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Split training and test input data")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            y_train = y_train.astype('int')
            y_test = y_test.astype('int')

            # Only use Random Forest classifier
            model = RandomForestClassifier()
            model.fit(X_train, y_train)

            logging.info(
                f"Trained the model")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=model
            )

            # Encode the target variable

            predicted = model.predict(X_test)

            # Calculate accuracy, precision, recall, and F1-score
            accuracy = accuracy_score(y_test, predicted)
            precision = precision_score(y_test, predicted, average='macro')
            recall = recall_score(y_test, predicted, average='macro')
            f1 = f1_score(y_test, predicted, average='macro')

            return accuracy

        except Exception as e:
            raise CustomException(e, sys)
