import streamlit as st

st.title('First Application - Sum, Subtract 2 Numbers')

operation = st.selectbox('Select Operation', ['Sum', 'Subtract'])
num1 = st.number_input('Enter first Number')
num2 = st.number_input('Enter second number Number')

if operation == "Sum":
    operation_two_numbers = num1 + num2
else:
    operation_two_numbers = num1 - num2


st.write(operation_two_numbers)
