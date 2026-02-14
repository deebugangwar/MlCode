from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    
    area = float(request.form["area"])
    bedrooms = float(request.form["bedrooms"])
    bathrooms = float(request.form["bathrooms"])
    stories = float(request.form["stories"])
    parking = float(request.form["parking"])
    mainroad = float(request.form["mainroad"])
    guestroom = float(request.form["guestroom"])
    basement = float(request.form["basement"])
    hotwaterheating = float(request.form["hotwater"])
    airconditioning = float(request.form["ac"])
    prefarea = float(request.form["prefarea"])

    features = np.array([[area, bedrooms, bathrooms, stories,
                          parking, mainroad, guestroom,
                          basement, hotwaterheating,
                          airconditioning, prefarea]])

    prediction = model.predict(features)

    # return f"Predicted Price: {round(prediction[0],2)}"
    return render_template("index.html",prediction_text=f"Prediction Price:{round(prediction[0],2)}")


if __name__ == "__main__":
    app.run(debug=True)