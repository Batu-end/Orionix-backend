import os
from fastapi import FastAPI, Query
import httpx
from dotenv import load_dotenv

env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '.env'))
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("OPENWEATHER_API_KEY")

app = FastAPI()

# weather, date, location, event type are


@app.get("/getEventsByCoordinates") # route identification
async def get_event_by_coor(lat, lon):
    # get lat, lon from allow
    # return json
    print(lat, lon)


@app.get("/getEventsByZip")
async def get_event_by_zip(zip_code):
    print(zip_code)