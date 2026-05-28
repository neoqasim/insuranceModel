import streamlit as st
import pandas as pd
import joblib


# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Insurance Charges Predictor",
    page_icon="💰",
    layout="centered"
)


# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.main {
    padding-top: 2rem;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #4CAF50;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #888888;
    margin-bottom: 30px;
}

.prediction-box {
    background-color: #111827;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    margin-top: 25px;
    border: 1px solid #333;
}

.prediction-text {
    font-size: 22px;
    color: white;
    font-weight: bold;
}

.small-text {
    color: #BBBBBB;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# =========================
# LOAD MODEL
# =========================

model = joblib.load("insurance_model.pkl")
scaler = joblib.load("scaler.pkl")


# =========================
# HEADER
# =========================

st.markdown(
    '<div class="title">💰 Insurance Charges Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Machine Learning Based Insurance Cost Estimation System</div>',
    unsafe_allow_html=True
)


# =========================
# SIDEBAR
# =========================

st.sidebar.header("📌 About Project")

st.sidebar.write("""
This project predicts medical insurance charges using a trained Machine Learning model.

### Technologies Used:
- Python
- Scikit-learn
- Pandas
- Streamlit

### Model:
Linear Regression
""")


# =========================
# INPUT SECTION
# =========================

st.subheader("📋 Enter Customer Information")

col1, col2 = st.columns(2)

with col1:

    age = st.slider(
        "Age",
        min_value=18,
        max_value=100,
        value=25
    )

    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=60.0,
        value=25.0
    )

    children = st.number_input(
        "Children",
        min_value=0,
        max_value=10,
        value=0
    )

with col2:

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    smoker = st.selectbox(
        "Smoker",
        ["No", "Yes"]
    )

    region = st.selectbox(
        "Region",
        [
            "Northeast",
            "Northwest",
            "Southeast",
            "Southwest"
        ]
    )


# =========================
# PREPROCESSING
# =========================

isfemale = 1 if gender == "Female" else 0

is_smoker = 1 if smoker == "Yes" else 0

bmi_category_Obese = 1 if bmi >= 30 else 0


# Region Encoding
region_northeast = 1 if region == "Northeast" else 0
region_northwest = 1 if region == "Northwest" else 0
region_southeast = 1 if region == "Southeast" else 0
region_southwest = 1 if region == "Southwest" else 0


# =========================
# CREATE DATAFRAME
# =========================

sample = pd.DataFrame({
    'age': [age],
    'isfemale': [isfemale],
    'is_smoker': [is_smoker],
    'bmi': [bmi],
    'children': [children],
    'bmi_category_Obese': [bmi_category_Obese],
    'region_northeast': [region_northeast],
    'region_northwest': [region_northwest],
    'region_southeast': [region_southeast],
    'region_southwest': [region_southwest]
})


# =========================
# SCALE NUMERICAL FEATURES
# =========================

sample[['age', 'bmi', 'children']] = scaler.transform(
    sample[['age', 'bmi', 'children']]
)


# =========================
# PREDICTION
# =========================

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🔍 Predict Insurance Charges", use_container_width=True):

    prediction = model.predict(sample)[0]

    st.markdown(f"""
    <div class="prediction-box">
        <div class="prediction-text">
            Estimated Insurance Charges
        </div>

   
            ${prediction:,.2f}
         
 
            Prediction generated using Machine Learning
      
    </div>
    """, unsafe_allow_html=True)


# =========================
# FOOTER
# =========================

st.markdown("<br><hr>", unsafe_allow_html=True)

st.caption("Developed using Streamlit and Scikit-learn")
