# Weather-
🌦️ Weather App (Python + WeatherAPI)

A simple command-line weather app built with Python. It fetches real-time weather data using the WeatherAPI
 and displays details like temperature, condition, humidity, and wind speed in the terminal.

🚀 Features

Fetches live weather for any city

Displays:

📍 City & Country

🌡️ Temperature (°C)

🌤️ Weather condition

💧 Humidity (%)

💨 Wind speed (kph)

Handles errors if city is not found

🛠️ Requirements

Python 3.6+

requests module

Install the dependency:

pip install requests

🔑 Setup API Key

Sign up at WeatherAPI
 for a free account.

Copy your API key.

Replace it in the code here:

api_key = "your_api_key"

▶️ Usage

Run the script in your terminal:

python weather.py


Enter a city name when prompted:

Enter city name: Paris


Example Output:

📍 City: Paris, France
🌡️ Temperature: 21°C
🌤️ Condition: Sunny
💧 Humidity: 45%
💨 Wind: 15 kph

📂 Project Structure
weather-app/
│-- weather.py        # Main Python script
│-- README.md         # Documentation

🔮 Future Improvements

Add weekly forecast support

Add GUI (Tkinter/PyQt)

Convert to a web app (Flask/Django)

Voice input integration

📝 License

This project is open-source and available under the MIT License
