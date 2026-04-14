from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load model & features
model = pickle.load(open("model.pkl", "rb"))
feature_names = pickle.load(open("feature_names.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.form.to_dict()

    # Convert values to numeric
    input_data = {
        "Age": int(data["age"]),
        "Sex": int(data["sex"]),
        "ChestPainType": int(data["cp"]),
        "RestingBP": int(data["bp"]),
        "Cholesterol": int(data["chol"]),
        "FastingBS": int(data["fbs"]),
        "RestingECG": int(data["ecg"]),
        "MaxHR": int(data["maxhr"]),
        "ExerciseAngina": int(data["exang"]),
        "Oldpeak": float(data["oldpeak"]),
        "ST_Slope": int(data["slope"])
    }

    df = pd.DataFrame([input_data])
    df = pd.get_dummies(df, drop_first=True)

    # Align columns
    for col in feature_names:
        if col not in df.columns:
            df[col] = 0

    df = df[feature_names]

    prediction = model.predict(df)[0]

    result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease"

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)