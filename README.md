# 🏠 Prediksi Harga Rumah Sederhana - Boston Housing (Streamlit + Scikit-learn)

Proyek ini bertujuan untuk membangun model machine learning sederhana menggunakan regresi linier untuk memprediksi harga rumah berdasarkan fitur-fitur lingkungan dan demografi dari dataset **Boston Housing**. Selain itu, proyek ini juga menyediakan antarmuka demo interaktif menggunakan **Streamlit**.

---

## 📊 Dataset

Dataset yang digunakan adalah **Boston Housing Dataset**, berisi informasi mengenai berbagai fitur perumahan di daerah Boston, seperti:
- Tingkat kejahatan (`CRIM`)
- Proporsi lahan hunian (`ZN`)
- Nitrogen oksida (`NOX`)
- Rata-rata jumlah kamar (`RM`)
- Pajak properti (`TAX`)
- Dan lainnya...

📥 Sumber dataset: [Kaggle - Boston Housing Dataset](https://www.kaggle.com/datasets/altavish/boston-housing-dataset)

---

## ⚙️ Teknologi yang Digunakan

| Tool | Deskripsi |
|------|-----------|
| Python | Bahasa pemrograman utama |
| pandas | Manipulasi data |
| scikit-learn | Pemodelan machine learning |
| matplotlib & seaborn | Visualisasi data |
| joblib | Menyimpan model |
| Streamlit | Aplikasi web interaktif |

---

## 🚀 Cara Menjalankan Proyek

### 1. Clone repository:
git clone https://github.com/vierkzme/home-price-prediction
cd prediction-app

### 2. Install dependencies:
pip install -r requirements.txt

### 3. Jalankan aplikasi Streamlit:
streamlit run app.py

---

📈 Alur Kerja Model
1. Preprocessing Data:
- Membersihkan data dan mengisi nilai kosong
- Menentukan fitur (X) dan target (y)

2. Pelatihan Model:
- Menggunakan regresi linier (LinearRegression)
- Evaluasi dengan MSE dan R² score

3. Simpan Model:
- Model disimpan ke file model_prediksi_rumah.pkl menggunakan joblib

4. Deploy ke Streamlit:
- Form input dibuat untuk prediksi berdasarkan parameter real-time

🌐 Demo Aplikasi Streamlit
🔢 Masukkan parameter rumah (jumlah kamar, usia, lokasi, dll)
📊 Klik "Prediksi Harga Rumah"
💰 Hasil prediksi akan tampil langsung di layar

📁 Struktur Folder
├── app.py                       # Aplikasi Streamlit
├── model_prediksi_rumah.pkl     # File model hasil training
├── requirements.txt            # Daftar library
└── README.md                   # Dokumentasi proyek

🧠 Hasil & Kesimpulan
Model regresi linier menghasilkan R² Score ~ 0.74, yang berarti sekitar 74% variasi harga rumah dapat dijelaskan oleh model.
Streamlit mempermudah proses uji coba model secara real-time oleh pengguna non-teknis.
Proyek ini cocok untuk pemula dalam memahami alur kerja end-to-end machine learning.

📎 Lisensi
Proyek ini dirilis dengan MIT License — silakan digunakan, dimodifikasi, dan dibagikan dengan bebas.

Dibuat dengan ❤️ oleh Ardy Nugroho sebagai bagian dari portfolio data science pribadi.
