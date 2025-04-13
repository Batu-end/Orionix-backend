import os
from fastapi import FastAPI
from dotenv import load_dotenv
from app.weather import get_with_zip, get_with_coor

env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '.env'))
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("OPENWEATHER_API_KEY")

app = FastAPI()

# weather, date, location, event type are


@app.get("/getEventsByCoordinates/") # route identification
async def get_event_by_coor(lat, lon):
    # get lat, lon from allow
    # return json
    res = await get_with_coor(lat, lon)
    print(lat, lon)

    return res


@app.get("/getEventsByZip")
async def get_event_by_zip(zip_code):

    lat, lon = await get_with_zip(zip_code)

    res = await get_with_coor(lat, lon)
    print(zip_code)

    return res
