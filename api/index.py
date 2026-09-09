from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "California Housing Flask App is Working!"