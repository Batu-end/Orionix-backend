import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.weather import get_with_zip, get_with_coor, get_weather_condition
from app.events import get_events_future
from app.planner import generate_tonight_summary

env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("OPENWEATHER_API_KEY")

app = FastAPI()

origins = [
    "http://localhost:8081",  # Replace with your React Native development server URL  # If your backend is on this origin
    # Add other origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# weather, date, location, event type are


@app.get("/getWeatherByCoordinates/") # route identification
async def get_weather_by_coor(lat, lon):
    # get lat, lon from allow
    # return json
    res = await get_with_coor(lat, lon)
    print(lat, lon)

    return res


@app.get("/getWeatherByZip")
async def get_weather_by_zip(zip_code):

    lat, lon = await get_with_zip(zip_code)

    res = await get_with_coor(lat, lon)
    print(zip_code)

    return res


@app.get("/futureEvents")
async def future_events():
    res = await get_events_future()
    return res


@app.get("/weatherTypeByCoordinates")
async def weather_type(lat, lon):
    res = await generate_tonight_summary(lat, lon)
    return res

@app.get('/weatherTypeByZip')
async def weather_type_by_zip(zip_code):
    print(zip_code)
    lat, lon = await get_with_zip(zip_code)
    res = await generate_tonight_summary(lat, lon)
    print(res)
    return res