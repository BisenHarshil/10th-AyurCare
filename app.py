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

@app.route("/habit_tracker", methods=["GET"])
def habit_tracker():
    return render_template("habit_tracker.html")

@app.route("/calculate_score", methods=["POST"])
def calculate_score():
    data = request.get_json()
    water = int(data["water"])
    sleep = int(data["sleep"])
    diet = data["diet"]
    
    score=0
    if water >=8:
        score+=40
    elif water >=5 and water <8:
        score+=25
    else:
        score+=10

    if sleep >=7 and sleep <=9:
        score+=35
    elif sleep >=5 and sleep <7:
        score+=20
    else:
        score+=10

    if diet == "balanced":
        score+=25
    elif diet == "average":
        score+=15
    else:
        score+=5

    if score >= 80:
        message = "Excellent! Your body is in balance today."
    elif score >= 60:
        message = "Good effort. Small improvements will make a big difference."
    elif score >= 40:
        message = "Your body needs more care today. Focus on water and sleep."
    else:
        message = "Your health needs urgent attention. Follow Ayurvedic basics."

    return jsonify({"score": score, "message": message})

@app.route("/herb_search", methods=["GET", "POST"])
def herb_search():
    if request.method == "POST":
        data = request.get_json()
        search_term = data["search_term"].lower()
        results = []
        for name, details in herbs_database.items():
            if search_term in name.lower() or search_term in details["uses"].lower() or any(search_term in t.lower() for t in details["treats"]):
                results.append({"name": name, "details": details})
        if results:
            return jsonify({"found": True, "results": results})
        else:
            return jsonify({"found": False, "message": "No herb found. Try Tulsi, Neem or Ginger."})
    return render_template("herb_search.html")

if __name__ == "__main__":
    app.run(debug=True)