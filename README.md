# California House Price Prediction

An end-to-end Machine Learning project that predicts California house prices using a trained Random Forest regression model and deploys the model as a Flask web application.

## Project Overview

This project uses the California Housing dataset to build a regression model that predicts the median house value based on eight features:

- Median Income
- House Age
- Average Rooms
- Average Bedrooms
- Population
- Average Occupancy
- Latitude
- Longitude

The trained machine learning Pipeline is saved using Joblib and integrated into a Flask application.

## Machine Learning Workflow

The project follows this workflow:

1. Load the California Housing dataset
2. Separate features and target
3. Split the dataset into training and testing sets
4. Build a preprocessing Pipeline
5. Train Decision Tree and Random Forest models
6. Evaluate models using R² score
7. Tune the Random Forest model
8. Select the best-performing model
9. Save the trained Pipeline using Joblib
10. Build a Flask API
11. Create an HTML frontend
12. Connect the frontend to the trained ML model

## Model Performance

The final model is a tuned Random Forest Regressor.

**Test R² Score: 0.8047**

The tuned Random Forest achieved an R² score of 0.8047 on the test set.

## Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn
- Joblib
- Flask
- HTML
- CSS

## Project Structure

```text
California Housing Project
│
├── templates/
│   └── index.html
│
├── app.py
├── california_housing_pipeline.pkl
├── requirements.txt
└── README.md
Flask Application

The Flask application:

->Loads the trained ML Pipeline
->Accepts eight house-related input features
->Sends the data to the trained model
->Generates a predicted house value
->Displays the prediction through the web interface
->Handles invalid input using error handling


How to Run
1. Clone the repository

git clone <your-github-repository-url>

2. Open the project directory

cd California-Housing-Project

3. Install dependencies

pip install -r requirements.txt

4. Run the Flask application

python app.py

5. Open the application

Open your browser and visit:

http://127.0.0.1:5000
Example Prediction

Example input:

Median Income: 10
House Age: 15
Average Rooms: 5
Average Bedrooms: 2
Population: 1200
Average Occupancy: 3
Latitude: 34
Longitude: -134

The application returns the predicted house value in dollars.

->Future Improvements
->Add stronger input validation
->Improve frontend design
->Add prediction confidence/explanation
->Deploy the application to a cloud platform
->Add automated testing
->Add API documentation