import streamlit as st
import pickle
import numpy as np

# Judul aplikasi
st.title("🌸 Prediksi Kategori Iris")
st.write("Masukkan nilai fitur di bawah untuk memprediksi jenis bunga iris.")

# Load model .pkl
with open("teori.pkcls", "br") as file:
    model = pickle.load(file)

# Input fitur dari pengguna
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, step=0.1)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, step=0.1)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, step=0.1)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, step=0.1)

# Tombol prediksi
if st.button("Prediksi"):
    # Membentuk array fitur
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    # Melakukan prediksi
    prediction = model.predict(features)

    # Menampilkan hasil
    st.success(f"🌼 Prediksi Kategori Iris: **{prediction[0]}**")
    st.balloons()
