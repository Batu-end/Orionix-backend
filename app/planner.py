from app.weather import get_with_coor
from app.events import get_events_for_tonight


async def generate_tonight_summary(lat, lon):
    # Fetch weather data for tonight
    weather_data = await get_with_coor(lat, lon)

    # Extract cloud cover from weather data
    cloud_cover = weather_data.get("clouds", {}).get("all", 100)
    

    # Determine quality and message based on cloud cover
    if cloud_cover <= 40:
        quality = "Excellent"
        weather_message = "Clear skies tonight — perfect for stargazing!"
    elif cloud_cover <= 70:
        quality = "Decent"
        weather_message = "Partly cloudy skies — some stars might be visible."
    else:
        quality = "Poor"
        weather_message = "Mostly cloudy skies — stargazing is unfortunately, unlikely."

    # Get tonight's events
    tonight_events = await get_events_for_tonight()

    if tonight_events:
        event_messages = []
        for event in tonight_events:
            event_messages.append(
                f"{event['name']} (rarity {event['rarity']}) at {event['time']}"
            )
        event_summary = "Tonight's event(s): " + ", ".join(event_messages)
    else:
        event_summary = "No major astronomical events tonight."

    return {
        ""
        "weather_quality": quality,
        "weather_message": weather_message,
        "event_message": event_summary
    }