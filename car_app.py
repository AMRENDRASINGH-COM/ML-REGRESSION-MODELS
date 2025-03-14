import streamlit as st
import pickle
import pandas as pd

# Load the model
model = pickle.load(open('final_model_XGBoost.pkl', 'rb'))

st.header('Car Price Prediction ML Model')

# Define input fields matching the model's expected features
symboling = st.slider("Insurance Risk Rating (Symboling)", -2, 3, 0, step=1)
fueltype = st.selectbox("Fuel Type", ["gas", "diesel"])
aspiration = st.selectbox("Aspiration", ["std", "turbo"])
doornumber = st.selectbox("Door Number", ["two", "four"])
drivewheel = st.selectbox("Drive Wheel", ["fwd", "rwd", "4wd"])
enginelocation = st.selectbox("Engine Location", ["front", "rear"])
curbweight = st.number_input("Curb Weight (kg)", min_value=500, max_value=3000, value=1500)
enginetype = st.selectbox("Engine Type", ["ohc", "ohcf", "ohcv", "dohc", "l", "rotor", "dohcv"])
cylindernumber = st.selectbox("Cylinder Number", [2, 3, 4, 5, 6, 8, 12])
enginesize = st.slider("Engine Size (cc)", 60, 105, 90)
fuelsystem = st.selectbox("Fuel System", ["mpfi", "2bbl", "idi", "1bbl", "spdi", "4bbl", "mfi", "spfi"])
horsepower = st.slider("Horsepower", 0, 100, 50)
carcompany = st.selectbox("Car Company", [
    "toyota", "nissan", "mazda", "honda", "mitsubishi", "subaru", 
    "peugeot", "volvo", "volkswagen", "dodge", "buick", "bmw", 
    "audi", "plymouth", "saab", "isuzu", "porsche", "alfa-romero", 
    "chevrolet", "jaguar"
])
car_area = st.slider("Car Area (sq cm)", 5, 1000, 500)

# Map categorical values to model's expected encoding
fuel_enc = 0 if fueltype == "gas" else 1
aspiration_enc = 0 if aspiration == "std" else 1
doornumber_enc = 0 if doornumber == "two" else 1
drivewheel_enc = {"fwd": 0, "rwd": 1, "4wd": 2}[drivewheel]
enginelocation_enc = 0 if enginelocation == "front" else 1
enginetype_enc = {
    "ohc": 0.72, "ohcf": 0.07, "ohcv": 0.06, 
    "dohc": 0.06, "l": 0.72, "rotor": 0.02, "dohcv": 0.00
}[enginetype]
fuelsystem_enc = {
    "mpfi": 0.46, "2bbl": 0.32, "idi": 0.10, 
    "1bbl": 0.05, "spdi": 0.04, "4bbl": 0.01, 
    "mfi": 0.00, "spfi": 0.00
}[fuelsystem]

if st.button("Predict"):
    input_data = [[
        symboling, fuel_enc, aspiration_enc, doornumber_enc, drivewheel_enc,
        enginelocation_enc, curbweight, enginetype_enc, cylindernumber,
        enginesize, fuelsystem_enc, horsepower, carcompany, car_area
    ]]
    
    prediction = model.predict(input_data)
    st.success(f"Predicted Car Price: ₹{prediction[0]:.2f}")
