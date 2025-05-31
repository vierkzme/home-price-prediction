import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('model.pkl')

# Judul
st.title("House Price Prediction - Boston Housing")

# Input fitur
crim = st.number_input("CRIM - Per capita crime rate", value=0.1)
zn = st.number_input("ZN - Proportion of residential land zoned", value=0.0)
indus = st.number_input(
    "INDUS - Non-retail business acres per town", value=8.0)
chas = st.selectbox("CHAS - Charles River dummy (1 if near a river)", [0, 1])
nox = st.number_input("NOX - Nitrogen oxide concentration", value=0.5)
rm = st.number_input("RM - Average number of rooms", value=6.0)
age = st.number_input(
    "AGE - Proportion of houses built before 1940", value=60.0)
dis = st.number_input("DIS - Distance to work center", value=4.0)
rad = st.number_input("RAD - Index access to highway", value=1.0)
tax = st.number_input("TAX - Property tax per $10,000", value=300.0)
ptratio = st.number_input("PTRATIO - Student-teacher ratio", value=15.0)
b = st.number_input("B - 1000(Bk - 0.63)^2", value=390.0)
lstat = st.number_input("LSTAT - Percentage of low social status", value=12.0)

# Prediksi saat tombol diklik
if st.button("House Price Prediction"):
    input_data = np.array(
        [[crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat]])
    prediksi = model.predict(input_data)[0]
    st.success(f"Estimated house price: ${prediksi * 1000:.2f}")
