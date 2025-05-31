# 🏡 Simple House Price Prediction - Boston Housing (Streamlit + Scikit-learn)

This project builds a simple machine learning model using linear regression to predict house prices based on demographic and environmental features from the **Boston Housing** dataset. It also includes an interactive web demo using **Streamlit**.

---

## 📉 Dataset

The dataset used is the classic **Boston Housing Dataset**, containing information about housing characteristics and neighborhoods in Boston, such as:

* `CRIM`: Per capita crime rate
* `ZN`: Proportion of residential land zoned
* `INDUS`: Proportion of non-retail business acres
* `CHAS`: Charles River dummy variable
* `NOX`: Nitric oxide concentration
* `RM`: Average number of rooms
* `AGE`: Proportion of owner-occupied units built before 1940
* `DIS`: Distance to employment centers
* `RAD`: Index of accessibility to radial highways
* `TAX`: Property tax rate
* `PTRATIO`: Pupil-teacher ratio
* `B`: Racial composition
* `LSTAT`: % lower status population
* `MEDV`: Median value of owner-occupied homes (target)

---

## ⚙️ Technologies Used

* **Python**
* **pandas** & **numpy** for data preprocessing
* **scikit-learn** for building the model
* **matplotlib** & **seaborn** for visualization
* **joblib** for saving the model
* **Streamlit** for creating the web demo

---

## 🚀 How to Run This Project

### 1. Clone this repository:

```bash
git clone https://github.com/vierkzme/house-price-prediction
cd house-price-prediction
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App:

```bash
streamlit run app.py
```

---

## 📊 Model Workflow

1. **Preprocessing**:

   * Handle missing values
   * Define features (`X`) and target (`y`)

2. **Train/Test Split**:

   * Use `train_test_split()` from scikit-learn

3. **Model Training**:

   * Fit `LinearRegression()` model
   * Evaluate with MSE and R^2

4. **Save Model**:

   * Save the trained model with `joblib`

5. **Web App Interface**:

   * Built using Streamlit to allow real-time predictions

---

## 🌐 Streamlit App

* Input housing data manually through form inputs.
* Press "Predict" to get an estimated house price.
* Results displayed instantly.

---

## 📁 Project Structure

```
.
├── housing.csv                 # Boston Housing dataset
├── app.py                      # Streamlit web app
├── model_prediksi_rumah.pkl   # Trained model
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## 🧠 Results & Conclusion

* The linear regression model achieved **R^2 score of \~0.74**, which is good for a basic model.
* The Streamlit app makes the model accessible for end-users.
* This is a great beginner project to understand the end-to-end machine learning process from data to deployment.

---

## 📄 License

MIT License © 2025 – vierkzme
Please feel free to use, modify and share freely.
