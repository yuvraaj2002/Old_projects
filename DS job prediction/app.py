import streamlit as st
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder, MinMaxScaler
import pickle

# Importing the model and dataframe
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))


# Let's write a title for the application
st.title("Data Science job prediction Web app")


# Taking input from the user
city_dev_index = st.slider("Enter your City development index", 0.0, 1.0, 0.2)
relevent_experience = st.selectbox(
    'Do you have relevent experience ?', df['relevent_experience'].unique())
Enrolled_university = st.selectbox(
    'Select your university enrollment level', df['enrolled_university'].unique())
education_level = st.selectbox(
    'Select your education level', df['education_level'].unique())
major_discipline = st.selectbox(
    'Select your Major discipline', df['major_discipline'].unique())
Experience = st.slider("Enter your year of experience", 0, 60, 3)
company_size = st.selectbox('Select company size', df['company_size'].unique())
company_type = st.selectbox(
    'Select your company type', df['company_type'].unique())
training_hours = st.number_input("Enter your training hours", value=0)


# Creating a numpy array so that we could feed it into the pipeline
Input_data = np.array([city_dev_index, relevent_experience, Enrolled_university, education_level,
                       major_discipline, Experience, company_size, company_type, training_hours])


# Button
button_clicked = st.button("Make Prediction")
if button_clicked:
    Input_data = Input_data.reshape(1, 9)
    result = int(pipe.predict(Input_data))
    if result == 1:
        st.write("Will Get Job")
    else:
        st.write("Will not get job")
