import requests

def get_weather(city):
    api_key = "c8a1d2cf87744f7cbeb54120252507"  
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"\n📍 City: {data['location']['name']}, {data['location']['country']}")
        print(f"🌡️ Temperature: {data['current']['temp_c']}°C")
        print(f"🌤️ Condition: {data['current']['condition']['text']}")
        print(f"💧 Humidity: {data['current']['humidity']}%")
        print(f"💨 Wind: {data['current']['wind_kph']} kph\n")
    else:
        print("❌ City not found or API error.")
        

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
