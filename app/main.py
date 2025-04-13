from fastapi import FastAPI
from app.routes import app as routes_app

app = FastAPI()

# Include all routes from routes.py
app.mount("/", routes_app)