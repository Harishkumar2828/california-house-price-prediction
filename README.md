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
---

## 📊 Model Performance

The final Random Forest model achieved an R² score of approximately **0.80** on the test dataset.

This indicates that the model explains approximately 80% of the variation in California house values in the evaluation dataset.

---

## 🖥️ Web Application

The trained Machine Learning model is integrated into a Flask web application.

Users can enter the following property information:

- Median Income
- House Age
- Average Rooms
- Average Bedrooms
- Population
- Average Occupancy
- Latitude
- Longitude

The application processes the input through the trained Random Forest model and returns the predicted house value.

---

## 🏗️ Project Architecture

```text
California Housing Dataset
          │
          ▼
   Data Exploration
          │
          ▼
   Train/Test Split
          │
          ▼
   Model Development
          │
          ├── Linear Regression
          │
          ├── Decision Tree
          │
          └── Random Forest
                    │
                    ▼
              GridSearchCV
                    │
                    ▼
               Best Model
                    │
                    ▼
              Joblib + Gzip
                    │
                    ▼
              Flask Backend
                    │
                    ▼
             HTML + CSS UI
                    │
                    ▼
                 Vercel
                    │
                    ▼
             Live Prediction
## Project Structure
california-house-price-prediction/
│
├── api/
│   └── index.py
│
├── templates/
│   └── index.html
│
├── app.py
├── california_housing_pipeline.pkl.gz
├── requirements.txt
├── vercel.json
├── README.md
└── .gitignore

🛠️ Tech Stack
Programming Language
Python

Data Science & Machine Learning
NumPy
Pandas
Scikit-learn
Random Forest Regression
Decision Tree Regression
Linear Regression
GridSearchCV

Model Evaluation
R² Score
Mean Squared Error (MSE)
Root Mean Squared Error (RMSE)

Backend & Deployment
Flask
Joblib
Gzip
Vercel

Frontend
HTML5
CSS3

Version Control
Git
GitHub

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Harishkumar2828/california-house-price-prediction.git

Navigate to Project Directory:
```bash
cd california-house-price-prediction

Install the required dependencies:
```bash
pip install -r requirements.txt

▶️ Run Locally
Start the Flask application:
```bash
python app.py

Then open:
http://127.0.0.1:5000

🔮 Example Prediction

Example input:

Feature	Value
Median Income	5.0
House Age	20
Average Rooms	5.0
Average Bedrooms	1.0
Population	1000
Average Occupancy	3.0
Latitude	34.0
Longitude	-118.0

The application processes these values through the trained Random Forest model and returns the predicted house value.

💡 Key Learning Outcomes

Through this project, I gained practical experience with:

End-to-end Machine Learning workflows
Regression algorithms
Model comparison
Hyperparameter tuning
Cross-validation
Model evaluation
Scikit-learn pipelines
Model serialization
Flask web application development
Git and GitHub
Cloud deployment
Integrating Machine Learning models into a web application
🔮 Future Improvements
Improve input validation
Improve the user interface
Add feature importance visualization
Add prediction explanations
Add automated testing
Add API documentation
Improve model performance
Add application monitoring and logging
👨‍💻 Author

Harish Kumar

GitHub:
https://github.com/Harishkumar2828

⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.
