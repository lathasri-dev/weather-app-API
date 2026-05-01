import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# 🔑 Put your valid API key here from OpenWeather
API_KEY ="adf66c652d1a75d70e4ce52929cb6295"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form.get("city").strip()

        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            data = response.json()

            print("🔍 API Response:", data)  # Debugging

            if data.get("cod") != 200:
                error = f"❌ Error: {data.get('message', 'City not found')}"
            else:
                weather = {
                    "city": data["name"],
                    "temperature": data["main"]["temp"],
                    "description": data["weather"][0]["description"].title(),
                    "icon": data["weather"][0]["icon"]
                }
        else:
            error = "⚠ Please enter a city name."

    return render_template("index.html", weather=weather, error=error)


if __name__ == "__main__":
    app.run(debug=True)
