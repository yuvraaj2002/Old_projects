import sys
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
import os
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, MinMaxScaler
import category_encoders as ce


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', "preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function is responsible for data transformation.
        '''
        try:

            impute_transformer = ColumnTransformer(transformers=[
                ('mean_imputer', SimpleImputer(strategy='mean'), [0, 6, 9]),
                ('mode_imputer', SimpleImputer(
                    strategy='most_frequent'), [3, 4])
            ], remainder='passthrough')

            encode_values = ColumnTransformer(transformers=[
                ('Encode_ordinal_Re', OrdinalEncoder(categories=[['No relevent experience', 'Has relevent experience']],
                                                     handle_unknown='use_encoded_value', unknown_value=np.nan), [6]),
                ('Encode_ordinal_eu', OrdinalEncoder(categories=[['no_enrollment', 'Part time course', 'Full time course']],
                                                     handle_unknown='use_encoded_value', unknown_value=np.nan), [3]),
                ('Encode_ordinal_el', OrdinalEncoder(categories=[['Primary School', 'High School', 'Graduate', 'Masters', 'Phd']],
                                                     handle_unknown='use_encoded_value', unknown_value=np.nan), [4]),
                ('Encode_ordinal_cs', OrdinalEncoder(categories=[['<10', '10/49', '50-99', '100-500', '500-999', '1000-4999', '5000-9999', '10000+']],
                                                     handle_unknown='use_encoded_value', unknown_value=np.nan), [8]),
                ('Encode_target_gen', ce.TargetEncoder(
                    smoothing=0.2, handle_missing='return_nan'), [5]),
                ('Encode_target_major', ce.TargetEncoder(
                    smoothing=0.2, handle_missing='return_nan'), [7]),
                ('Encode_target_ct', ce.TargetEncoder(
                    smoothing=0.2, handle_missing='return_nan'), [9])
            ], remainder='passthrough')

            knn_imputer = ColumnTransformer(transformers=[
                ('Knn_Imputer', KNNImputer(n_neighbors=5,
                 metric='nan_euclidean'), [3, 4, 5, 6])
            ], remainder='passthrough')

            scaling_transformer = ColumnTransformer(transformers=[
                ('scale_transformer', MinMaxScaler(), [7, 8, 9])
            ], remainder='passthrough')

            preprocessor = Pipeline(steps=[
                ('impute_transformer', impute_transformer),
                ('encode_values', encode_values),
                ('knn_imputer', knn_imputer),
                ('scaling', scaling_transformer)
            ])

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            # Reading the data from train and test csv files
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")
            logging.info("Obtaining preprocessing object")

            # Object of the pipeline
            preprocessing_obj = self.get_data_transformer_object()

            # Training data
            input_feature_train_df = train_df.drop(
                columns=['enrollee_id', 'city', 'target'], axis=1)
            target_feature_train_df = train_df['target']

            # Test data
            input_feature_test_df = test_df.drop(
                columns=['enrollee_id', 'city', 'target'], axis=1)
            target_feature_test_df = test_df['target']

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe.")

            # Passing the data through the pipeline
            input_feature_train_arr = preprocessing_obj.fit_transform(
                input_feature_train_df, target_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(
                input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr,
                              np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr,
                             np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e, sys)
