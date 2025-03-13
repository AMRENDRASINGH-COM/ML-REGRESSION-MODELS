import streamlit as st
import numpy as np
import pandas as pd
import pickle
import sklearn.ensemble


with open('final_model_XGBoost.pkl', 'rb') as file:
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
gr.Interface(fn=prediction,inputs=[gr.Slider(minimum=-2, maximum=3, step=1,label = "SYMBOLING: INSURANCE RISK RATING"),
        gr.Dropdown(choices=[('gas',0), ("Diesel",1)], label="FUEL TYPE"),
        gr.Dropdown(choices=[("std",0), ("turbo",1)], label="ASPIRATION"),
        gr.Dropdown(choices=[('four',1),('two',0)], label="DOOR NUMBER"),
        gr.Dropdown(choices=[('fwd',0),('rwd',1),('4wd',2)], label="DRIVE WHEEL"),
        gr.Dropdown(choices=[('front',0),('rear',1)], label="ENGINE LOCATION"),
        gr.Number(label="CURB WEIGHT"),
        gr.Dropdown(choices=[("ohc",0.72),("ohcf",0.07),("ohcv",0.06),("dohc",0.06),('l',0.72),('rotor',0.02),('dohcv',0.00)],label="ENGINE TYPE"),
        gr.Dropdown(choices=[2,3,4,5,6,8,12], label="CYLINDER NUMBER"),
        gr.Slider(minimum=60, maximum=105, step=0.5,label="ENGINE SIZE"),
        gr.Dropdown(choices=[('mpfi',0.46),('2bbl',0.32),('idi',0.10),('1bbl',0.05),('spdi',0.04),('4bbl',0.01),('mfi',0.00),('spfi',0.00)],label="FUEL SYSTEM"),
        gr.Slider(minimum=0, maximum=100, step=1,label="HORSEPOWER"),
        gr.Dropdown(choices=[("toyota", 0.151220), ("nissan", 0.063415), ("mazda", 0.053659), 
                     ("honda", 0.043902), ("mitsubishi", 0.082927), ("subaru", 0.039024), 
                     ("peugeot", 0.0731), ("volvo", 0.034146), ("volkswagen", 0.058537), 
                     ("dodge", 0.014634), ("buick", 0.019512), ("bmw", 0.009756), 
                     ("audi", 0.029268), ("playmouth", 0.004878)], label="CARCOMPANY"),
        gr.Slider(minimum=5, maximum=1000, step=1,label="CAR AREA")],

# Prediction button
if st.button("Predict Price"):
    result = prediction(sym, fuel[1], aspi[1], door[1], carbody[1], drivewheel[1], engine_l[1], whel_b, car_l, car_w, car_h, cur_weg, eng_ty[1],
                        cylind_num, engi_siz, fuel_sys[1], strok, h_p, peak, citmp, highmp, companyName[1])
    st.success(result)
