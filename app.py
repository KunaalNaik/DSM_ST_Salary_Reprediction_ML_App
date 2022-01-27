import streamlit as st
import pandas as pd
from sklearn import linear_model
import joblib

st.title('Predict Salary')
st.subheader('Predict Salary based Candidate details')

# User Input
name = st.text_input('Enter Name')
experience = st.number_input('Enter Experience')
skill = st.number_input('Enter Number of Skills')

# Create Input DataFrame
user_input = pd.DataFrame({
    'x1_Experience': [experience],
    'x2_Skills': [skill]
})

# Import Model Pickle
reg = joblib.load('model/predict_salary.pkl')

# Predict Salary
predicted_salary = reg.predict(user_input)

# Displaying the Predicted Output
st.write(name + 's Predicted Salary')
st.write(predicted_salary[0])
