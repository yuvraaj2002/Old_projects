# Importing the libraries
import streamlit as st
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import pickle

# Let's write a title for the application
st.title("Data Science job prediction Web app")

# List of all the options
experience_options = ['No relevent experience', 'Has relevent experience']
Enrollement_options = ['no_enrollment', 'Part time course', 'Full time course']
eduLevel_options = ['Primary School',
                    'High School', 'Graduate', 'Masters', 'Phd']
Major_dis_options = ['STEM', 'Humanities',
                     'Other', 'Business Degree', 'Arts', 'No Major']
comp_size_options = ['<10', '10/49', '50-99', '100-500',
                     '500-999', '1000-4999', '5000-9999', '10000+']
comp_type_options = ['Pvt Ltd', 'Funded Startup',
                     'Early Stage Startup', 'Other', 'Public Sector', 'NGO']

# Taking input from the user
city_dev_index = st.slider("Enter your City development index", 0.0, 1.0, 0.2)
relevent_experience = st.selectbox(
    'Do you have relevent experience ?', experience_options)
Enrolled_university = st.selectbox(
    'Select your university enrollment level', Enrollement_options)
education_level = st.selectbox('Select your education level', eduLevel_options)
major_discipline = st.selectbox(
    'Select your Major discipline', Major_dis_options)
Experience = st.slider("Enter your year of experience", 0, 60, 3)
company_size = st.selectbox('Select company size', comp_size_options)
company_type = st.selectbox('Select your Major discipline', comp_type_options)
training_hours = st.number_input("Enter your training hours", value=0)

# Creating a numpy array so that we could feed it in the pipeline
Input_data = np.array([city_dev_index, relevent_experience, Enrolled_university, education_level,
                       major_discipline, Experience, company_size, company_type, training_hours])


# Loading all the saved pickle files during the training phase
with open('Impute_mean.pkl', 'rb') as f:
    Impute_mean = pickle.load(f)
with open('Impute_mode.pkl', 'rb') as f:
    Impute_mode = pickle.load(f)

# Loading all pickle files saved during training to deal with categorical values
with open('Oe_Relev_exp.pkl', 'rb') as f:
    Oe_Relev_exp = pickle.load(f)
with open('Oe_Enrolled_uni.pkl', 'rb') as f:
    Oe_Enrolled_uni = pickle.load(f)
with open('Oe_Edu_level.pkl', 'rb') as f:
    Oe_Edu_level = pickle.load(f)
with open('Oe_Company_size.pkl', 'rb') as f:
    Oe_Company_size = pickle.load(f)
with open('Oh_Major.pkl', 'rb') as f:
    Oh_Major = pickle.load(f)
with open('Oh_Company_type.pkl', 'rb') as f:
    Oh_Company_type = pickle.load(f)

# Loding pickle file for scaling
with open('Scale.pkl', 'rb') as f:
    Scale = pickle.load(f)

# Column transformer to deal with missing values
Impute_values = ColumnTransformer(transformers=[
    ('mean_imputer', Impute_mean, [0, 8]),
    ('mode_imputer', Impute_mode, [1, 2, 3, 4, 5, 6, 7])
], remainder='passthrough')

# Column transformer to deal with the categorical values
Handle_categories = ColumnTransformer(transformers=[
    ('Encode_ordinal_Re', Oe_Relev_exp, [2]),
    ('Encode_ordinal_eu', Oe_Enrolled_uni, [3]),
    ('Encode_ordinal_el', Oe_Edu_level, [4]),
    ('Encode_ordinal_cs', Oe_Company_size, [7]),
    ('Encode_nominal_md', Oh_Major, [5]),
    ('Encode_nominal_ct', Oh_Company_type, [8])
], remainder='passthrough')

# Column transformer to scale the values
Scale_values = ColumnTransformer(transformers=[(
    'scale_transformer', Scale, [16, 17, 18])], remainder='passthrough')


# Pipeline to process the data
pipe = Pipeline(steps=[
    ('Impute_Nan_Values', Impute_values),
    ('Encode_values', Handle_categories),
    ('Feature_Scaling', Scale_values)
])

# Passing the data through the pipeline
Process_data = pipe.fit_transform(Input_data)

# Button
button_clicked = st.button("Click me!")
if button_clicked:
    st.write("Button clicked!")
