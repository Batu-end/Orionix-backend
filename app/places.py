import os
import httpx
from dotenv import load_dotenv

env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("GOOGLE_API_KEY")

# GOOGLE API CALL: https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lon}&radius=10000&type=park&keyword=hill%20viewpoint%20trail&key={API_KEY}


async def get_nearby_stargazing_spots(lat: float, lon: float):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{lat},{lon}",
        "radius": 10000,
        "type": "park",
        "keyword": "hill viewpoint trail nature",
        "key": API_KEY
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            print(data)
            return data.get("results", [])
        return []
