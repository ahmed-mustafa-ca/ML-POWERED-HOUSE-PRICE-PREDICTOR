import streamlit as st
import joblib
import numpy as np 

model = joblib.load("model.pkl")

st.title("House Price Predictor App")

st.divider()

st.write("This app uses machine learning for predicting house prices with given features of the house.For using this app you can enter the inputs from this user interface and then press the predict button.")

st.divider()

bedrooms = st.number_input("Number Of BedRooms", min_value = 0, value  = 0)
bathrooms = st.number_input("Number Of BathRooms",min_value = 0 ,value = 0)
livingarea = st.number_input("Living Area",min_value = 0 , value = 2000)
condition = st.number_input("Condition",min_value = 0, value = 3)
number_of_schools = st.number_input("Number Of School Nearby",min_value = 0, value = 0)

st.divider()

x= [[bedrooms,bathrooms,livingarea,condition,number_of_schools]]

predict_buttun = st.button("Predict!")

if predict_buttun:

    st.balloons()

    x_array = np.array(x)

    prediction = model.predict(x_array)[0]

    st.write(f"Price Prediction is: ₹{prediction:,.2f}")

else:
    st.write("Please press the predict buttun after entering values!")