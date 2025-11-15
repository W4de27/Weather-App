# 🌦️ Weather App 2.0

![Python](https://img.shields.io/badge/Python-3.7+-blue?style=flat-square)
![Requests](https://img.shields.io/badge/Requests-✓-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

A **professional Python CLI Weather App** that fetches **real-time weather data** for any city worldwide using the **OpenWeather API**.  
Provides temperature, weather description, humidity, and **local city time** in a **beautiful CLI display with emojis and animations**.

---

## 🌟 Features

- Fetch weather for **any city globally** 🌍  
- Displays:
  - **Temperature** 🌡️  
  - **Weather description** ☁️  
  - **Humidity** 💧  
  - **Local city time** 🕒  
- Animated **loading effects** for smooth user experience  
- Robust **error handling**:
  - Invalid city input  
  - Network issues  
  - API request limits (429)  
  - Invalid API key  
- **Cross-platform CLI support** (Windows 10+, Linux, Mac)  
- Easy to **customize and extend**  

---

## 💻 Tech Stack

- **Python 3.7+**
- `requests` for API requests  
- `python-dotenv` for secure API key management  
- Optional: `colorama` for colored CLI output  

---

## 🚀 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/W4de27/weather-app.git
cd weather-app
```

2. **Create a virtual environment (recommended):**
```bash
python -m venv venv
# Activate
# Windows:
venv\Scripts\activate
# Linux / Mac:
source venv/bin/activate
```
3. **Install dependencies:**
```bash
pip install -r requirements.txt
```
4. **Set up your API key:**
- Create a `.env` file in the project root:
```env
OPENWEATHER_API_KEY=your_api_key_here
```
