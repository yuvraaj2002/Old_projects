# Importing the libraries
import streamlit as st

# Let's write a title for the application
st.title("Data Science job prediction Web app")

# List of all the options
experience_options = ['No relevent experience', 'Has relevent experience']
Enrollement_options = ['no_enrollment', 'Part time course', 'Full time course']
eduLevel_options = ['Primary School', 'High School', 'Graduate', 'Masters', 'Phd']
Major_dis_options = ['STEM', 'Humanities', 'Other', 'Business Degree', 'Arts', 'No Major']
comp_size_options = ['<10', '10/49', '50-99', '100-500', '500-999', '1000-4999', '5000-9999', '10000+']
comp_type_options = ['Pvt Ltd', 'Funded Startup', 'Early Stage Startup', 'Other','Public Sector', 'NGO']

# Taking input from the user
city_dev_index = st.slider("Enter your City development index",0.0,1.0,0.2)
relevent_experience = st.selectbox('Do you have relevent experience ?', experience_options)
Enrolled_university = st.selectbox('Select your university enrollment level', Enrollement_options)
education_level = st.selectbox('Select your education level', eduLevel_options)
major_discipline = st.selectbox('Select your Major discipline', Major_dis_options)
Experience = st.slider("Enter your year of experience",0,60,3)
company_size = st.selectbox('Select company size', comp_size_options)
company_type = st.selectbox('Select your Major discipline', comp_type_options)
training_hours = st.number_input("Enter your training hours", value=0)


# Button
button_clicked = st.button("Click me!")
if button_clicked:
    st.write("Button clicked!")

