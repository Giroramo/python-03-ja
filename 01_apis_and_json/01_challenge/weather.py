import requests
import sys
import signal

# OpenWeatherMapのAPIキーを指定
API_KEY = "9fcdd68e98ec6a065d170f31c97f566b"

def search_city(query, api_key=API_KEY):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={query}&limit=5&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    
    if not data:
        print("City not found. Please try again.")
        return None

    if len(data) > 1:
        print("Multiple matches found, which city did you mean?")
        for idx, city in enumerate(data):
            print(f"{idx + 1}. {city['name']},{city['country']}")
        try:
            choice = int(input("> ")) - 1
            if choice < 0 or choice >= len(data):
                print("Invalid choice. Please try again.")
                return None
            return data[choice]
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None

    return data[0]

def weather_forecast(lat, lon, api_key=API_KEY):
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code != 200:
        print("Failed to retrieve weather data. Please try again.")
        return None

    forecast = []
    for entry in data['list']:
        date = entry['dt_txt'].split(' ')[0]
        if not any(f['date'] == date for f in forecast):
            forecast.append({
                'date': date,
                'weather': entry['weather'][0]['description'],
                'temp_max': entry['main']['temp_max']
            })

    return forecast

def main():
    def signal_handler(sig, frame):
        print("\nExiting the program. Goodbye!")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    
    while True:
        city_name = input("City?\n> ")
        city_data = search_city(city_name, API_KEY)
        if city_data:
            lat = city_data['lat']
            lon = city_data['lon']
            forecast = weather_forecast(lat, lon, API_KEY)
            if forecast:
                print(f"Here's the weather in {city_data['name']}")
                for info in forecast:
                    print(f"{info['date']}: {info['weather'].title()} {info['temp_max']}°C")
            print()

if __name__ == "__main__":
    main()
