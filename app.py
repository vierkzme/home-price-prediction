import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('model_prediksi_rumah.pkl')

# Judul
st.title("Prediksi Harga Rumah - Boston Housing")

# Input fitur
crim = st.number_input("CRIM - Per capita crime rate", value=0.1)
zn = st.number_input("ZN - Proportion of residential land zoned", value=0.0)
indus = st.number_input(
    "INDUS - Non-retail business acres per town", value=8.0)
chas = st.selectbox("CHAS - Charles River dummy (1 jika dekat sungai)", [0, 1])
nox = st.number_input("NOX - Nitrogen oxide concentration", value=0.5)
rm = st.number_input("RM - Rata-rata jumlah kamar", value=6.0)
age = st.number_input(
    "AGE - Proporsi rumah yang dibangun sebelum 1940", value=60.0)
dis = st.number_input("DIS - Jarak ke pusat kerja", value=4.0)
rad = st.number_input("RAD - Index akses ke jalan raya", value=1.0)
tax = st.number_input("TAX - Pajak properti per $10.000", value=300.0)
ptratio = st.number_input("PTRATIO - Rasio siswa-guru", value=15.0)
b = st.number_input("B - 1000(Bk - 0.63)^2", value=390.0)
lstat = st.number_input("LSTAT - Persentase status sosial rendah", value=12.0)

# Prediksi saat tombol diklik
if st.button("Prediksi Harga Rumah"):
    input_data = np.array(
        [[crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat]])
    prediksi = model.predict(input_data)[0]
    st.success(f"Perkiraan harga rumah: ${prediksi * 1000:.2f}")
