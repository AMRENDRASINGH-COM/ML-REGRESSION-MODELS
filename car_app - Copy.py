import streamlit as st
import pickle
import pandas as pd

# Load the model
model = pickle.load(open('final_model_XGBoost.pkl', 'rb'))

st.header('Car Price Prediction ML Model')

# Define car company mapping (as per Jupyter notebook)
COMPANY_MAPPING = {
    "toyota": 0.151220, "nissan": 0.063415, "mazda": 0.053659,
    "honda": 0.043902, "mitsubishi": 0.082927, "subaru": 0.039024,
    "peugeot": 0.0731, "volvo": 0.034146, "volkswagen": 0.058537,
    "dodge": 0.014634, "buick": 0.019512, "bmw": 0.009756,
    "audi": 0.029268, "plymouth": 0.004878, "saab": 0.0,  # Add missing companies
    "isuzu": 0.0, "porsche": 0.0, "alfa-romero": 0.0,
    "chevrolet": 0.0, "jaguar": 0.0
}

# Input fields
symboling = st.slider("Insurance Risk Rating (Symboling)", -2, 3, 0)
fueltype = st.selectbox("Fuel Type", ["gas", "diesel"])
aspiration = st.selectbox("Aspiration", ["std", "turbo"])
doornumber = st.selectbox("Door Number", ["two", "four"])
drivewheel = st.selectbox("Drive Wheel", ["fwd", "rwd", "4wd"])
enginelocation = st.selectbox("Engine Location", ["front", "rear"])
curbweight = st.number_input("Curb Weight (kg)", 500, 3000, 1500)
enginetype = st.selectbox("Engine Type", ["ohc", "ohcf", "ohcv", "dohc", "l", "rotor", "dohcv"])
cylindernumber = st.selectbox("Cylinder Number", [2, 3, 4, 5, 6, 8, 12])
enginesize = st.slider("Engine Size (cc)", 60, 105, 90)
fuelsystem = st.selectbox("Fuel System", ["mpfi", "2bbl", "idi", "1bbl", "spdi", "4bbl", "mfi", "spfi"])
horsepower = st.slider("Horsepower", 0, 100, 50)
carcompany = st.selectbox("Car Company", list(COMPANY_MAPPING.keys()))
car_area = st.slider("Car Area (sq cm)", 5, 1000, 500)

# Encoding mappings
ENGINE_TYPE_MAP = {
    "ohc": 0.72, "ohcf": 0.07, "ohcv": 0.06,
    "dohc": 0.06, "l": 0.72, "rotor": 0.02, "dohcv": 0.00
}

FUEL_SYSTEM_MAP = {
    "mpfi": 0.46, "2bbl": 0.32, "idi": 0.10,
    "1bbl": 0.05, "spdi": 0.04, "4bbl": 0.01,
    "mfi": 0.00, "spfi": 0.00
}

if st.button("Predict"):
    # Create DataFrame with EXACT feature names and order
    input_df = pd.DataFrame([[
        symboling,
        0 if fueltype == "gas" else 1,
        0 if aspiration == "std" else 1,
        0 if doornumber == "two" else 1,
        {"fwd": 0, "rwd": 1, "4wd": 2}[drivewheel],
        0 if enginelocation == "front" else 1,
        curbweight,
        ENGINE_TYPE_MAP[enginetype],
        cylindernumber,
        enginesize,
        FUEL_SYSTEM_MAP[fuelsystem],
        horsepower,
        COMPANY_MAPPING[carcompany],
        car_area
    ]], columns=model.feature_names_in_)

    try:
        prediction = model.predict(input_df)
        st.success(f"Predicted Car Price: ₹{prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"Prediction failed: {str(e)}")
