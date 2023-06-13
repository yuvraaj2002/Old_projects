import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
# from src.components.data_transformation import DataTransformation
# from src.components.data_transformation import DataTransformationConfig
# from src.components.model_trainer import ModelTrainerConfig
# from src.components.model_trainer import ModelTrainer


from dataclasses import dataclass
import os
import logging
import pandas as pd
from sklearn.model_selection import train_test_split

# Define a data class called DataIngestionConfig


@dataclass
class DataIngestionConfig:
    # Define three properties with default values using os.path.join
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

# Create a class called DataIngestion


class DataIngestion:
    def __init__(self):
        # Instantiate an instance of DataIngestionConfig
        self.ingestion_config = DataIngestionConfig()

    # Define a method to initiate data ingestion
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion component")
        try:
            # Read a CSV file into a dataframe
            df = pd.read_csv('notebook\data\data_science_job.csv')
            logging.info('Read the dataset as dataframe')

            # Create the directory structure for the train_data_path
            os.makedirs(os.path.dirname(
                self.ingestion_config.train_data_path), exist_ok=True)

            # Save the dataframe as a CSV file at raw_data_path
            df.to_csv(self.ingestion_config.raw_data_path,
                      index=False, header=True)

            logging.info("Train test split initiated")
            # Split the dataframe into train and test sets
            train_set, test_set = train_test_split(
                df, test_size=0.2, random_state=42)

            # Save the train set as a CSV file at train_data_path
            train_set.to_csv(
                self.ingestion_config.train_data_path, index=False, header=True)

            # Save the test set as a CSV file at test_data_path
            test_set.to_csv(self.ingestion_config.test_data_path,
                            index=False, header=True)

            logging.info("Ingestion of the data is completed")

            # Return the paths to the train and test data files
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            # Raise a custom exception with the original exception and sys information
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    # data_transformation = DataTransformation()
    # train_arr, test_arr, _ = data_transformation.initiate_data_transformation(
    #     train_data, test_data)

    # modeltrainer = ModelTrainer()
    # print(modeltrainer.initiate_model_trainer(train_arr, test_arr))
