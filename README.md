# Multiple Disease Detection Using Machine Learning and Streamlit

This project aims to predict multiple diseases using machine learning algorithms and Streamlit, a Python library for creating web applications. The system allows users to input health parameters such as pulse rate, cholesterol, blood pressure, and heart rate, and predicts diseases such as diabetes, heart disease, and Parkinson’s disease. The model utilizes logistic regression and SVM classifiers for prediction.

## Table of Contents

- [Introduction](#introduction)
- [Literature Survey](#literature-survey)
- [Proposed Methodology](#proposed-methodology)
  - [Data Pre-Processing](#data-pre-processing)
  - [Model Selection](#model-selection)
  - [Model Building](#model-building)
  - [System Analysis](#system-analysis)
  - [Future Scope](#future-scope)
  - [How to Run](#how-to-run)
  - [Contributors](#contributors)
  - [License](#license)

## Introduction <a name="introduction"></a>

A person's well-being is crucial, and healthcare plays a vital role in society. This project focuses on predicting various diseases using machine learning techniques to assist healthcare professionals in making informed decisions. By analyzing health parameters, the system predicts diseases like diabetes, heart disease, and Parkinson’s disease. The aim is to reduce mortality rates by early detection and intervention.

## Literature Survey <a name="literature-survey"></a>

Healthcare analytics have become more precise and sophisticated with the advent of artificial intelligence and machine learning. Various studies have explored using AI algorithms for disease detection. For instance, Alsharif et al. (2021) achieved an accuracy rate of 82.1% in predicting three different diseases using an AI algorithm. Zhang et al. (2020) proposed a deep learning model that could diagnose chest X-ray images for diseases like pneumonia, tuberculosis, and lung cancer with high accuracy rates.

## Proposed Methodology <a name="proposed-methodology"></a>

### Data Pre-Processing <a name="data-pre-processing"></a>

The project utilizes datasets from sources like the UCI Machine Learning Repository and Kaggle for diseases like diabetes, heart disease, and Parkinson’s disease. Data pre-processing involves cleaning and normalizing the data, handling missing values, and selecting relevant features.

### Model Selection <a name="model-selection"></a>

Three algorithms are employed for disease prediction: SVM Classifier and Logistic Regression. The models are trained and compared to select the one with the highest accuracy.

### Model Building <a name="model-building"></a>

The selected model is built and saved using the pickle module. The Streamlit framework is used to create a user-friendly web interface for disease prediction.

### System Analysis <a name="system-analysis"></a>

The system comprises modules for data pre-processing, feature extraction, model training, and web application development. It cleans and normalizes data, extracts relevant features, trains AI models on large datasets, and presents results through a Streamlit web application.

## Future Scope <a name="future-scope"></a>

While the project shows promising results, it has some limitations such as reliance on small datasets and limited disease coverage. Future improvements could include training models on larger datasets, incorporating more diseases, and making the system more interactive with features like a chatbot.

## How to Run <a name="how-to-run"></a>

To run the project:

1. Clone the repository.
2. Install the required Python libraries (streamlit, scikit-learn, etc.).
3. Run the Streamlit app using the command streamlit run app.py.
4. Open the provided URL in your web browser to access the application.

## Contributors <a name="contributors"></a>

- Shivam Rawat
