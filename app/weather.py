import os
import httpx
from dotenv import load_dotenv

env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("OPENWEATHER_API_KEY")

# OPENWEATHER API CALL: https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}
# GEOCODER API CALL: http://api.openweathermap.org/geo/1.0/zip?zip={zip code},{country code}&appid={API key}
# 16-DAY CALL: http://api.openweathermap.org/data/2.5/forecast/daily??lat={lat}&lon={lon}&cnt={cnt}&appid={API key}
# async def get_coordinates(city: str = None, zip_code: str = None, country: str = "US"):


async def get_with_zip(zip_code: str):

    country = "US"
    async with httpx.AsyncClient() as client:

        if zip_code:
            api_url_zip = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},{country}&appid={API_KEY}"
            response = await client.get(api_url_zip)

            if response.status_code == 200:
                data = response.json()
                lat = data.get("lat")
                lon = data.get("lon")
                return lat, lon

            else:
                return None, None  # or raise error


async def get_with_coor(lat: float, lon: float):

    async with httpx.AsyncClient() as client:

        api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
        response = await client.get(api_url)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to fetch weather data."}


async def get_weather_condition(lat: float, lon: float):
    weather_data = await get_with_coor(lat, lon)

    if "weather" in weather_data and len(weather_data["weather"]) > 0:
        condition = weather_data["weather"][0]["main"]
        return condition
    else:
        return "Unknown"
