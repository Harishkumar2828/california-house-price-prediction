# 🏠 California House Price Prediction

An end-to-end Machine Learning project that predicts California house prices using a Random Forest Regression model and deploys the trained model as a Flask web application on Vercel.

## 🚀 Live Demo

🔗 **Live Application:**  
https://california-house-price-prediction-delta.vercel.app/

---

## 📌 Project Overview

This project demonstrates a complete Machine Learning workflow, starting from data exploration and model development to model serialization and deployment as a web application.

The model predicts the median house value based on eight features from the California Housing dataset:

- Median Income
- House Age
- Average Rooms
- Average Bedrooms
- Population
- Average Occupancy
- Latitude
- Longitude

The final model is integrated with a Flask application where users can enter property details through a web interface and receive a predicted house value.

---

## 🎯 Objective

The main objective of this project is to build and deploy an end-to-end Machine Learning solution capable of:

- Analyzing the California Housing dataset
- Training multiple regression models
- Comparing model performance
- Tuning the best-performing model
- Saving the trained model
- Integrating the model with Flask
- Creating a web-based prediction interface
- Deploying the application to the cloud

---

## 🧠 Machine Learning Workflow

The project follows the following workflow:

1. Load the California Housing dataset
2. Perform exploratory data analysis
3. Inspect dataset shape, columns, data types and statistics
4. Separate features and target variable
5. Split the dataset into training and testing sets
6. Train a Linear Regression model
7. Train a Decision Tree Regressor
8. Tune the Decision Tree using GridSearchCV
9. Train a Random Forest Regressor
10. Tune the Random Forest using GridSearchCV
11. Evaluate models using R², MSE and RMSE
12. Select the best-performing Random Forest model
13. Save the trained model using Joblib
14. Compress the model using Gzip
15. Build a Flask web application
16. Connect the web interface to the trained model
17. Deploy the application using Vercel

---

## 🤖 Machine Learning Model

Several regression algorithms were evaluated during development:

### Linear Regression

Used as the baseline regression model.

### Decision Tree Regressor

Used to capture nonlinear relationships between the features and target variable.

### Random Forest Regressor

The Random Forest model produced the strongest performance and was selected as the final model.

The final model uses:

```text
RandomForestRegressor
n_estimators = 50
max_depth = 20
min_samples_split = 2
random_state = 42
