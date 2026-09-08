from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

model = joblib.load("california_housing_pipeline.pkl")

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict", methods=["POST"])
def predict():
    try:
        med_inc = float(request.form.get("MedInc"))
        house_age = float(request.form.get("HouseAge"))
        ave_rooms = float(request.form.get("AveRooms"))
        ave_bedrms = float(request.form.get("AveBedrms"))
        population = float(request.form.get("Population"))
        ave_occup = float(request.form.get("AveOccup"))
        latitude = float(request.form.get("Latitude"))
        longitude = float(request.form.get("Longitude"))

        input_data = [[
            med_inc,
            house_age,
            ave_rooms,
            ave_bedrms,
            population,
            ave_occup,
            latitude,
            longitude
        ]]

        prediction = model.predict(input_data)

        predicted_price = prediction[0] * 100000

        return render_template(
            "index.html",
            prediction=predicted_price,
            med_inc=med_inc,
            house_age=house_age,
            ave_rooms=ave_rooms,
            ave_bedrms=ave_bedrms,
            population=population,
            ave_occup=ave_occup,
            latitude=latitude,
            longitude=longitude
        )

    except (TypeError, ValueError):
        return render_template(
            "index.html",
            error="Invalid input. Please enter valid numeric values.",
        )

if __name__ == "__main__":
    app.run(debug=True)