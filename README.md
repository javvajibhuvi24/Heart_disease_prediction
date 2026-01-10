# 🫀 Heart Disease Prediction using Machine Learning

This project focuses on predicting the presence of heart disease in patients using various machine learning algorithms. The model is trained on a clinical dataset containing demographic and medical attributes and compares the performance of multiple classification techniques.

## 📌 Project Overview

Heart disease is one of the leading causes of mortality worldwide. Early prediction can help in timely diagnosis and treatment.
This project uses machine learning models to classify whether a patient is likely to have heart disease based on medical parameters.

## 📊 Dataset

- Source: Heart Disease Dataset

- Number of features: 11

- Target variable: HeartDisease

   - 1 → Presence of heart disease

   - 0 → No heart disease

- Features include:

  - Age

  - Sex

  - Chest Pain Type

  - Resting Blood Pressure

  - Cholesterol

  - Fasting Blood Sugar

  - Resting ECG

  - Maximum Heart Rate

  - Exercise-Induced Angina

  - Oldpeak

  - ST Slope

## ⚙️ Technologies Used

- Python

- Pandas, NumPy

- Matplotlib, Seaborn

- Scikit-learn

## 🔍 Exploratory Data Analysis (EDA)

- Distribution analysis of the target variable

- Analysis of categorical features like sex, chest pain type, and exercise-induced angina

- Correlation analysis to understand feature relationships

## 🧠 Machine Learning Models Implemented

- Logistic Regression

- Naive Bayes

- Support Vector Machine (SVM)

- K-Nearest Neighbors (KNN)

- Decision Tree

- Random Forest

- XGBoost (optional, environment dependent)

- Neural Network (skipped due to TensorFlow compatibility)

## 📈 Model Evaluation

- Train-test split (80:20)

- Accuracy score comparison

- Confusion matrix analysis

- Visualization of model accuracies using bar plots

## 🏆 Results

Among all the models tested, Random Forest achieved the highest accuracy, demonstrating strong performance in predicting heart disease compared to other algorithms.

## 📌 Conclusion

The project demonstrates that machine learning can effectively assist in predicting heart disease using clinical data. Ensemble models like Random Forest provided better accuracy due to their ability to capture complex patterns. This system can serve as a decision-support tool for healthcare professionals.
