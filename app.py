import streamlit as st     # framework  gives  dummy ui and flask gives real ui
import joblib
import numpy as np

# Load the saved regression model
model=joblib.load('regression_model.joblib')

#streamlit app UI
st.title(" job Package prediction Based on CGPA")
st.write("Enter your CGPA to predict the expected job package")

# User input for CGPA
cgpa= st.number_input("CGPA",min_value=0.0,max_value=10.0, step=0.1)


#predict button
if st.button("Predict Package"):
  #prepare input data for a model
  input_data=np.array([[cgpa]])

  #predict the package
  prediction= model.predict(input_data)
  predicted_value=float(prediction[0]) # convert numpy value to float

  #show the result
  st.success(f"Predicted Package: Rs.{predicted_value:,.2f} LPA")
