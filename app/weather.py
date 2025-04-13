import os
import httpx
from dotenv import load_dotenv

env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '.env'))
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("OPENWEATHER_API_KEY")

# OPENWEATHER API CALL: https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}
# GEOCODER API CALL: http://api.openweathermap.org/geo/1.0/zip?zip={zip code},{country code}&appid={API key}

# async def get_coordinates(city: str = None, zip_code: str = None, country: str = "US"):


async def get_with_zip(zip_code: str):

    country = "US"
    async with httpx.AsyncClient() as client:

        if zip_code:
            api_url_zip = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},{country}&appid={API_KEY}"
            zip_response = await client.get(api_url_zip)
            # if zip_response.status_code == 200:
            data = zip_response.json()

    lat = data.get("lat")
    lon = data.get("lon")

    return lat, lon


async def get_with_coor(lat: float, lon: float):

    async with httpx.AsyncClient() as client:

        api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
        response = await client.get(api_url)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to fetch weather data."}