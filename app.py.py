import streamlit as st
import numpy as np
import pandas as pd
import pickle
import sklearn.ensemble


with open('final_model_Gradient.pkl', 'rb') as file:
    model = pickle.load(file)

def prediction(sym, fuel, aspi, door, carbody, drivewheel, engine_l, whel_b, car_l, car_w, car_h, cur_weg, eng_ty, cylind_num, engi_siz,
               fuel_sys, strok, h_p, peak, citmp, highmp, companyName):
    input_data = np.array([[sym, fuel, aspi, door, carbody, drivewheel, engine_l, whel_b, car_l, car_w, car_h, cur_weg, eng_ty, cylind_num, engi_siz,
                            fuel_sys, strok, h_p, peak, citmp, highmp, companyName]])
    pred = model.predict(input_data)
    return f'Price of car = ₹{pred[0]}'

# Streamlit UI Components

st.title("Car Price Prediction App")
st.write("This application predicts the price of a car based on various features.")

# Creating input fields
sym = st.slider("SYMBOLING: INSURANCE RISK RATING", min_value=-2, max_value=3, step=1)
fuel = st.selectbox("FUEL TYPE", [('gas', 0), ("Diesel", 1)])
aspi = st.selectbox("ASPIRATION", [("std", 0), ("turbo", 1)])
door = st.selectbox("DOOR NUMBER", [('four', 1), ('two', 0)])
carbody = st.selectbox("CAR BODY", [("Sedan", 0.47), ("convertible", 0.03), ("Hatchback", 0.34), ("hardtop", 0.16)])
drivewheel = st.selectbox("DRIVE WHEEL", [('fwd', 0), ('rwd', 1), ('4wd', 2)])
engine_l = st.selectbox("ENGINE LOCATION", [('front', 0), ('rear', 1)])
companyName = st.selectbox("Company Name", [('alfa-romero', 0.01), ('audi', 0.03), ('bmw', 0.04), ('chevrolet', 0.01), ('dodge', 0.04),
                                            ('honda', 0.06), ('isuzu', 0.02), ('jaguar', 0.01), ('maxda', 0.01), ('mazda', 0.07),
                                            ('buick', 0.04), ('mitsubishi', 0.06), ('Nissan', 0.00), ('peugeot', 0.05),
                                            ('porsche', 0.02), ('toyota', 0.15), ('volkswagen', 0.04), ('volvo', 0.05)])
whel_b = st.slider("WHEELBASE", min_value=60.0, max_value=120.0, step=0.5)
car_l = st.slider("CAR LENGTH", min_value=1.0, max_value=200.0, step=0.5)
car_w = st.slider("CAR WIDTH", min_value=1.0, max_value=100.0, step=0.5)
car_h = st.slider("CAR HEIGHT", min_value=50.0, max_value=100.0, step=0.5)
cur_weg = st.number_input("CURB WEIGHT", min_value=500, max_value=5000)
eng_ty = st.selectbox("ENGINE TYPE", [("ohc", 0.72), ("ohcf", 0.07), ("ohcv", 0.06), ("dohc", 0.06), ('l', 0.72), ('rotor', 0.02), ('dohcv', 0.00)])
cylind_num = st.selectbox("CYLINDER NUMBER", [2, 3, 4, 5, 6, 8, 12])
engi_siz = st.slider("ENGINE SIZE", min_value=60.0, max_value=105.0, step=0.5)
fuel_sys = st.selectbox("FUEL SYSTEM", [('mpfi', 0.46), ('2bbl', 0.32), ('idi', 0.10), ('1bbl', 0.05), ('spdi', 0.04), ('4bbl', 0.01), ('mfi', 0.00), ('spfi', 0.00)])
strok = st.slider("STROKE", min_value=0.0, max_value=20.0, step=1.0)
h_p = st.slider("HORSEPOWER", min_value=0.0, max_value=100.0, step=1.0)
peak = st.slider("PEAK RPM", min_value=0.0, max_value=30.0, step=1.0)
citmp = st.slider("CITY MPG", min_value=5, max_value=70, step=1)
highmp = st.slider("HIGHWAY MPG", min_value=5, max_value=100, step=1)

# Prediction button
if st.button("Predict Price"):
    result = prediction(sym, fuel[1], aspi[1], door[1], carbody[1], drivewheel[1], engine_l[1], whel_b, car_l, car_w, car_h, cur_weg, eng_ty[1],
                        cylind_num, engi_siz, fuel_sys[1], strok, h_p, peak, citmp, highmp, companyName[1])
    st.success(result)
