import streamlit as st
import requests

FASTAPI_URL = "http://127.0.0.1:8000"

st.title("Academic Performance Predictor")

# Collect input from the user
gender = st.selectbox("Gender", ["male", "female"])
race_ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
parental_level_of_education = st.selectbox("Parental Level of Education", ["some high school", "high school", "some college", "associate's degree", "bachelor's degree", "master's degree"])
lunch = st.selectbox("Lunch", ["free/reduced", "standard"])
test_preparation_course = st.selectbox("Test Preparation Course", ["none", "completed"])
writing_score = st.number_input("Writing Score",step=0.01)
reading_score = st.number_input("Reading Score",step=0.01)

# Send data to FastAPI backend and display the result
if st.button("Predict MATHS SCORE"):
    df = {
        "GENDER": 1 if gender=="male" else 0, 
        "READING SCORE": reading_score, 
        "WRITING SCORE": writing_score,  
        "RACE/ETHNICITY_group B": 1 if race_ethnicity=="group B" else 0,
        "RACE/ETHNICITY_group C": 1 if race_ethnicity=="group C" else 0, 
        "RACE/ETHNICITY_group D": 1 if race_ethnicity=="group D" else 0,
        "RACE/ETHNICITY_group E": 1 if race_ethnicity=="group E" else 0,
        "PARENTAL LEVEL OF EDUCATION_bachelor degree" :1 if parental_level_of_education=="bachelor's degree" else 0,
        "PARENTAL LEVEL OF EDUCATION_high school": 1 if parental_level_of_education=="high school" else 0,
        "PARENTAL LEVEL OF EDUCATION_master's degree":1 if parental_level_of_education=="master's degree" else 0,
        "PARENTAL LEVEL OF EDUCATION_some college":1 if parental_level_of_education=="some college" else 0,
        "PARENTAL LEVEL OF EDUCATION_some high school":1 if parental_level_of_education== "some high school" else 0, 
        "LUNCH_standard": 1 if lunch =="standard" else 0,
        "TEST PREPARATION COURSE_none":1 if test_preparation_course =="none" else 0,
    }
    response = requests.post(f"{FASTAPI_URL}/predict", json=df)
    print(response.json()) #deburging
    prediction = response.json()["predicted_math_score"]
    st.write(f"Predicted MATH SCORE: {prediction:.2f}")

