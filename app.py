from flask import Flask, render_template, request, jsonify
import random

from data import symptoms_remedies, herbs_database, daily_tips

app = Flask(__name__)

@app.route("/")
def home():
    tips = random.choice(daily_tips)

    return render_template("ayur_index.html",
                            tips=tips)

@app.route("/check_remedies", methods=["POST"])
def check_remedies():
    data = request.get_json()
    symptoms = data["symptoms"]
    remedies = []
    herbs = []
    lifestyle = []
    for symptom in symptoms:
        if symptom in symptoms_remedies:
            remedies.extend(symptoms_remedies[symptom]["remedies"])
            herbs.extend(symptoms_remedies[symptom]["herbs"])
            lifestyle.append(symptoms_remedies[symptom]["lifestyle"])
    return jsonify({"remedies": remedies, "herbs": herbs, "lifestyle": lifestyle})

@app.route("/check_symptoms")
def check_symptoms():
    return render_template("check_symptoms.html")

@app.route("/browse_herbs")    
def browse_herbs():
    return render_template("herbs.html", herbs=herbs_database)

if __name__ == "__main__":
    app.run(debug=True)