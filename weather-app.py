import time
import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

# ================== Load API Key ==================
load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")

# ================== Icons Based on Weather ==================

WEATHER_ICONS = {
    "clear": "☀️",
    "clouds": "☁️",
    "rain": "🌧️",
    "drizzle": "🌦️",
    "thunderstorm": "⛈️",
    "snow": "❄️",
    "mist": "🌫️",
    "fog": "🌁",
    "haze": "🌤️",
    "smoke": "💨"
}

# ================== UI / Animation Helpers ==================

def animate(text, repeats=3, delay=0.4):
    for i in range(repeats):
        print(f"\r{text}{'.' * (i % 3 + 1)}  ", end='', flush=True)
        time.sleep(delay)
    print()

def pause():
    print()
    input("Press Enter to continue...")
    time.sleep(0.3)

def error(msg):
    print(f"\n❌ {msg}\n")
    time.sleep(1)
    pause()

# ================== Weather Data Handling ==================

def get_weather_icon(condition):
    condition = condition.lower()
    for key in WEATHER_ICONS:
        if key in condition:
            return WEATHER_ICONS[key]
    return "🌈"  # Default icon


def fetch_weather(city):
    try:
        url = (
            f"https://api.openweathermap.org/data/2.5/weather?"
            f"q={city}&appid={api_key}&units=metric"
        )

        response = requests.get(url, timeout=6)
        data = response.json()

        return response.status_code, data

    except requests.exceptions.ConnectionError:
        return None, "Network error"
    except requests.exceptions.Timeout:
        return None, "Timeout"
    except:
        return None, "Unknown error"

# ================== Display Weather ==================

def show_weather(city):
    animate("Fetching weather")

    status, data = fetch_weather(city)

    if status == 200:
        weather_desc = data['weather'][0]['description']
        icon = get_weather_icon(weather_desc)

        # Local Time
        tz_offset = data.get('timezone', 0)
        city_time = datetime.utcnow() + timedelta(seconds=tz_offset)
        local_time = city_time.strftime("%Y-%m-%d %H:%M:%S")

        # UI Block
        print("\n" + "=" * 52)
        print(f"{'🌦️  WEATHER SUMMARY  🌦️':^52}")
        print("=" * 52)

        print(f"📍 City          : {data['name']}")
        print(f"{icon}  Condition     : {weather_desc.capitalize()}")
        print(f"🌡️  Temperature   : {data['main']['temp']:.1f}°C")
        print(f"💧 Humidity      : {data['main']['humidity']}%")
        print(f"🕒 Local Time    : {local_time}")

        print("-" * 52)
        print("Thank you for checking the weather 🌦️")
        print("=" * 52)

        pause()

    elif status == 404:
        error("City not found! Please try again.")

    elif status == 401:
        error("Invalid API key! Check your .env file.")

    elif status == 429:
        error("Too many requests! Try again in a moment.")

    elif status is None:
        error("Network issue! Please check your connection.")

    else:
        error("Unexpected server error. Try again later!")

# ================== Main Program ==================

def main():

    running = True

    while running:
        print("\n" + "#" * 60)
        print(f"## {'WEATHER APP 3.0':^54} ##")
        print(f"## {'Fast • Clean • Real-Time Forecasts':^54} ##")
        print("#" * 60)
        print()

        city = input("🌍 Enter city name (or 'exit' to quit): ").strip()

        if city.lower() == "exit":
            for i in range(3):
                print("Exiting" + "." * (i + 1))
                time.sleep(1)
                os.system("cls" if os.name == "nt" else "clear")
            print("🔶 Thank you for using the Weather App. Stay safe! 🌦️\n")
            break

        if city == "":
            error("City name cannot be empty!")
            continue

        if len(city) < 2:
            error("City name is too short!")
            continue

        if not any(c.isalpha() for c in city):
            error("City name must contain letters!")
            continue

        # Valid city input → Fetch weather
        show_weather(city.title())


# ================== Entry Point ==================

if __name__ == "__main__":
    try:
        for i in range(3):
            print(" Starting" + "." * (i + 1))
            time.sleep(0.8)
            os.system("cls" if os.name == "nt" else "clear")
        main()
    except KeyboardInterrupt:
        print("\n\n🔶 Weather App closed. Stay prepared! 🌦️\n")
