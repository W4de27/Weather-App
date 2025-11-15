import time, os, requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

# ================== Load API Key ==================
load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")

# ================== Functions ==================

def animate(word, repeats=3, delay=0.5):
    for i in range(repeats):
        dots = '.' * ((i % 3) + 1)
        print(f"\r{word}{dots}  ", end='', flush=True)
        time.sleep(delay)
    print()

def pause():
    print()
    input("Press Enter to continue...")
    time.sleep(0.5)

def error(msg):
    print()
    print(f"❌ {msg}")
    time.sleep(1.5)
    pause()

def get_data(city):
    try:
        base_url = "https://api.openweathermap.org/data/2.5/weather"
        key = f"&appid={api_key}&units=metric"
        url = f"{base_url}?q={city}{key}"
        response = requests.get(url, timeout=5)
        data = response.json()

        # ===== City Local Time =====
        tz_offset = data.get('timezone', 0)  # seconds
        city_time = datetime.utcnow() + timedelta(seconds=tz_offset)
        update_time = city_time.strftime("%Y-%m-%d %H:%M:%S")

        match response.status_code:
            case 200:
                animate("Loading", repeats=3, delay=0.5)
                print()
                print("=" * 46)
                print(f"{'🌦️   WEATHER SUMMARY  🌦️':^46}")
                print("-" * 46)
                print(f"📍 City        : {data['name']}")
                print(f"🌡️  Temperature : {data['main']['temp']:.2f}°C")
                print(f"☁️  Description : {data['weather'][0]['description']}")
                print(f"💧 Humidity    : {data['main']['humidity']}%")
                print(f"🕒 Local Time   : {update_time}")
                print('-' * 46)
                print("Thank you for checking the weather with us 🌦️")
                print('=' * 46)
                time.sleep(2)
                pause()
            case 400:
                animate("Checking", repeats=3, delay=0.5)
                error("Bad request. Please check your input.")
            case 401:
                animate("Checking", repeats=3, delay=0.5)
                error("Invalid API key. Please check your API key.")
            case 404:
                animate("Checking", repeats=3, delay=0.5)
                print()
                print(f"Status : {response.status_code}")
                print(f"Error: {data.get('message','City not found')}")
                pause()
            case 429:
                animate("Checking", repeats=3, delay=0.5)
                error("Too many requests. Please wait a moment before trying again.")
            case _:
                animate("Checking", repeats=3, delay=0.5)
                error("Server error. Please try again later.")

    except requests.exceptions.ConnectionError:
        animate("Checking", repeats=3, delay=0.5)
        error("Network error: Unable to connect. Please check your internet connection.")
    except requests.exceptions.Timeout:
        animate("Checking", repeats=3, delay=0.5)
        error("Request timed out: The server took too long to respond. Please try again.")
    except requests.exceptions.RequestException:
        animate("Checking", repeats=3, delay=0.5)
        error("An unexpected error occurred while fetching data. Please try again later.")

# ================== Main Program ==================

def main():
    is_running = True

    while is_running:
        print()
        print("#" * 56)
        print(f"## {'WEATHER APP 2.0':^50} ##")
        print(f"## {'Accurate • Fast • Real-Time Forecasts':^50} ##")
        print("#" * 56)
        print()

        city = input("Enter your city (type 'exit' to quit): ").title().strip()

        # ===== Input Validation =====
        if city == "":
            animate("Checking", repeats=3, delay=0.5)
            error("Please enter a city name!")
            continue

        if not any(char.isalpha() for char in city):
            animate("Checking", repeats=3, delay=0.5)
            error("City name must contain letters!")
            continue
        
        if len(city) < 2:
            animate("Checking", repeats=3, delay=0.5)
            error("City name is too short!")
            continue 

        # ===== Exit Command =====
        if city.lower() == 'exit':
            for i in range(3):
                print("Exiting" + "." * (i + 1))
                time.sleep(1)
                os.system("cls" if os.name == "nt" else "clear")
            print("🔶 Thank you for choosing our weather service. Stay prepared. 🌦️ \n")
            is_running = False
        else:
            get_data(city)

# ================== Entry Point ==================

if __name__ == "__main__":
    try:
        # ===== Startup Animation =====
        for i in range(3):
            print(" Starting" + "." * (i + 1))
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")
        main()
    except KeyboardInterrupt:
        print("\n\n 🔶 Thank you for choosing our weather service. Stay prepared. 🌦️ \n")
