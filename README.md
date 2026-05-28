
# Insurance Charges Prediction System

A Machine Learning based web application that predicts medical insurance charges using customer information such as age, BMI, smoking habits, region, and number of children.

---

# Live Demo

## Deployed Application
https://predictinscharges.streamlit.app/

# Google Drive Project Files

Contains:

- Trained `.pkl` model files
- Local project files
- UI project files
- Additional resources

## Drive Link
https://drive.google.com/drive/folders/1dxWUY2fvjdyw-QZGKhB6GIEbR2A67TBK?usp=sharing
---

# Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib

---
# Machine Learning Workflow

The project includes:

1. Data preprocessing
2. Feature engineering
3. Feature scaling
4. Model training using Linear Regression
5. Model saving using Joblib
6. Frontend integration using Streamlit
7. Online deployment

---

# Important Note

The project consists of two separate parts:

## 1. Model Training Code

The Machine Learning training notebook/code is separate and should preferably be run on:

- Google Colab
- Jupyter Notebook

This part is responsible for:

- Training the model
- Preprocessing the dataset
- Creating `.pkl` files

Generated files:

text
insurance_model.pkl
scaler.pkl


---

## 2. Streamlit Web Application

The Streamlit application uses the already trained `.pkl` files for prediction.

This allows the UI application to run directly without retraining the model every time.

---

# Local Setup Instructions

## Step 1 — Clone Repository

```bash
git clone https://github.com/neoqasim/insuranceModel.git
```

Or download ZIP manually from GitHub.

---

## Step 2 — Open Project Folder

```bash
cd insuranceModel
```

---

## Step 3 — Create Virtual Environment

### Windows

```bash
python -m venv venv
```

---

## Step 4 — Activate Virtual Environment

### CMD

```bash
venv\Scripts\activate
```

### PowerShell

```bash
.\venv\Scripts\Activate.ps1
```

---

## Step 5 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 6 — Run Streamlit Application

```bash
streamlit run app.py
```

---

# Running Model Training Code on Colab

## Steps

1. Open Google Colab
2. Upload the model training notebook/code
3. Upload the insurance dataset
4. Run all notebook cells
5. Model files will be generated automatically

Generated files:

```text
insurance_model.pkl
scaler.pkl
```

These files are then used by the Streamlit frontend application.

---

# Project Structure

```text
insuranceModel/
│
├── app.py
├── insurance_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
└── model_training_notebook.ipynb


---

# Developed By

## Qasim

Student ID: 0000674916



# License

This project is developed for educational and learning purposes.

