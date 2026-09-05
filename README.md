# Employee Workforce Analytics & Salary Intelligence System

A Python-based workforce analytics project that combines employee data analysis, visualization, employee segmentation, and salary prediction into a Streamlit application.

## 📌 Project Overview

This project analyzes employee workforce data to understand salary patterns, team distribution, hiring trends, employee segments, and salary-related insights.

It also uses real-world UCOP public payroll data to perform salary analysis and build a machine learning model for gross pay prediction.

## 🚀 Features

- Employee data cleaning and preprocessing
- Exploratory data analysis (EDA)
- Salary distribution analysis
- Team-wise employee analysis
- Hiring trend analysis
- Bonus distribution analysis
- Employee segmentation using KMeans clustering
- UCOP public payroll salary analysis
- Salary prediction using Machine Learning
- Interactive Streamlit dashboard

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

## 🤖 Machine Learning

### Employee Segmentation

KMeans clustering is used to segment employees based on:

- Salary
- Bonus %
- Experience

The features are standardized using `StandardScaler` before clustering.

### Salary Prediction

A Linear Regression model is used to predict UCOP employee gross pay.

Features used:

- Year
- Location
- Job Title

Categorical features are handled using `OneHotEncoder` inside a Scikit-learn pipeline.

Model performance:

- MAE: 13,229.65
- RMSE: 27,723.06
- R²: 0.7210

## 📊 Datasets

### Employee Dataset

The employee dataset contains workforce information such as:

- Employee name
- Gender
- Start date
- Salary
- Bonus %
- Senior management status
- Team

### UCOP Dataset

The project also uses UCOP public employee wage data from 2010 for salary analysis and prediction.

## 📁 Project Structure

```text
Employee-Workforce-Analytics/
│
├── app.py
├── main.py
├── 02_eda_analysis.ipynb
├── employees(1).csv
├── UCOP_Data_2010.csv
├── pyproject.toml
├── requirements.txt
├── README.md
│
└── src/
    ├── __init__.py
    ├── analysis.py
    ├── cleaning.py
    ├── employee_segmentation.py
    ├── salary_Prediction.py
    ├── ucop_salary_analysis.py
    └── visualization.py
