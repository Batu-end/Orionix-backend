import json
from datetime import date, timedelta
import os

# Load events from JSON file
file_path = os.path.join(os.path.dirname(__file__), "events.json")

with open(file_path, "r") as f:
    EVENTS = json.load(f)


async def get_events_for_tonight():
    today = date.today().isoformat()
    tonight_events = [event for event in EVENTS if event["date"] == today]
    return tonight_events


# get future events up to 2 weeks from start date.
async def get_events_future():
    today = date.today()
    two_weeks_later = today + timedelta(days=14)
    future_events = [event for event in EVENTS if today.isoformat() <= event["date"] <= two_weeks_later.isoformat()]
    return future_events
