from flask import Flask, render_template, request, jsonify
import random
import requests

from data import symptoms_remedies, herbs_database, daily_tips, weather_tips

app = Flask(__name__)

@app.route("/")
def home():
    tip = random.choice(daily_tips)
    weather_tip, temp, weather_desc = get_weather_tip("Delhi")
    
    return render_template("ayur_index.html",
                            tips=tip,
                            weather_tip=weather_tip,
                            temp=temp,
                            weather_desc=weather_desc)

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

    if water == 0 or sleep == 0:
        return jsonify({"score": 0, "message": "Please enter valid water and sleep values."})
    
    if water > 20:
        return jsonify({"score": 0, "message": "Please enter a realistic water intake value."})
    if sleep > 24:
        return jsonify({"score": 0, "message": "Please enter a realistic sleep value."})
    
    if score >= 80:
        message = "Excellent! Your body is in balance today."
        basics = []
    elif score >= 60:
        message = "Good effort. Small improvements will make a big difference."
        basics = ["Drink warm water every morning", "Sleep before 10pm"]
    elif score >= 40:
        message = "Your body needs more care today. Focus on water and sleep."
        basics = ["Drink at least 8 glasses of water", "Sleep 7-8 hours", "Eat one meal with vegetables today"]
    else:
        message = "Your health needs urgent attention. Follow Ayurvedic basics."
        basics = ["Start with warm water and lemon every morning", "Sleep by 10pm — this is critical", "Eat simple home cooked food today", "Take 10 deep breaths before each meal", "Avoid cold drinks completely"]

    return jsonify({"score": score, "message": message, "basics": basics})

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

def get_weather_tip(city="Delhi"):
    try:
        response = requests.get(f"https://wttr.in/{city}?format=j1", timeout=5)
        data = response.json()
        print("API call succeeded")
        
        temp = int(data["current_condition"][0]["temp_C"])
        print(f"Temp: {temp}")
        
        desc = data["current_condition"][0]["weatherDesc"][0]["value"].lower()
        print(f"Desc: {desc}")
        
        if temp < 15:
            condition = "cold"
        elif temp > 32:
            condition = "hot"
        elif "rain" in desc or "drizzle" in desc:
            condition = "rainy"
        else:
            condition = "normal"
        
        print(f"Condition: {condition}")
        return weather_tips[condition], temp, desc
        
    except Exception as e:
        print(f"ERROR: {e}")
        return random.choice(daily_tips), None, None

@app.route("/about")
def about():
    return render_template("about.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
