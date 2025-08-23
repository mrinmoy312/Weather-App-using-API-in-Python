# 🌦️ Weather App (Python + WeatherAPI)  
[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/)  
[![WeatherAPI](https://img.shields.io/badge/API-WeatherAPI-orange.svg)](https://www.weatherapi.com/)  

A simple **command-line weather app** built with Python. It fetches **real-time weather data** using the [WeatherAPI](https://www.weatherapi.com/) and displays details like temperature, condition, humidity, and wind speed in the terminal.  

---

## 🚀 Features
- Fetches live weather for any city  
- Displays:  
  - 📍 City & Country  
  - 🌡️ Temperature (°C)  
  - 🌤️ Weather condition  
  - 💧 Humidity (%)  
  - 💨 Wind speed (kph)  
- Handles errors if city is not found  

---

## 🛠️ Requirements
- Python 3.6+  
- `requests` module

## 📖 What’s Happening in the Code?

- We use `requests.get()` to call the WeatherAPI.  
- The response is returned in **JSON format**, which we parse using `.json()`.  
- The weather details are then printed in a clean format.  
- If an error occurs (like entering the wrong city), it is handled gracefully. 

Install the dependency:  
```bash
pip install requests
