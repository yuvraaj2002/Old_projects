import streamlit as st

# Let's write a title for the application
st.title("Data Science job prediction Web app")

# Input regarding city development index
city_dev_index = st.slider("Enter your City development index",0.0,1.0,0.2)

# Input regarding experience
experience_options = ['No relevent experience', 'Has relevent experience']
relevent_experience = st.selectbox('Do you have relevent experience ?', experience_options)

Enrollement_options = ['no_enrollment', 'Part time course', 'Full time course']
Enrolled_university = st.selectbox('Select your university enrollment level', Enrollement_options)

eduLevel_options = ['Primary School', 'High School', 'Graduate', 'Masters', 'Phd']
education_level = st.selectbox('Select your education level', eduLevel_options)

Major_dis_options = ['STEM', 'Humanities', 'Other', 'Business Degree', 'Arts', 'No Major']
major_discipline = st.selectbox('Select your Major discipline', Major_dis_options)

# Input regarding city development index
Experience = st.slider("Enter your year of experience",0,60,3)

comp_size_options = ['<10', '10/49', '50-99', '100-500', '500-999', '1000-4999', '5000-9999', '10000+']
company_size = st.selectbox('Select company size', comp_size_options)

comp_type_options = ['Pvt Ltd', 'Funded Startup', 'Early Stage Startup', 'Other','Public Sector', 'NGO']
company_type = st.selectbox('Select your Major discipline', comp_type_options)

training_hours = st.number_input("Enter your training hours", value=0)


# Checkbox input
agree = st.checkbox("Do you want to continue ?")
if agree:
    st.write("Thank you for agreeing!")

# Button
button_clicked = st.button("Click me!")
if button_clicked:
    st.write("Button clicked!")

# Selectbox input
color = st.selectbox("Select your favorite color", ["Red", "Green", "Blue"])
st.write("Your favorite color is:", color)