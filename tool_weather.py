import os
import requests
from langchain.tools import tool
from dotenv import load_dotenv

load_dotenv()

@tool
def get_weather(city: str) -> str:
    """Obtiene el clima actual para una ciudad especificada usando OpenWeatherMap."""
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    if not api_key:
        return "Falta configurar OPENWEATHERMAP_API_KEY en el archivo .env."

    try:
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={
                "q": city,
                "appid": api_key,
                "units": "metric",
                "lang": "es",
            },
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as error:
        return f"No se pudo consultar el clima para {city}: {error}"

    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind_speed = data.get("wind", {}).get("speed", 0)
    location = data.get("name", city)

    return (
        f"Clima actual en {location}: {temperature:.1f} °C, {description}. "
        f"Sensación térmica: {feels_like:.1f} °C. "
        f"Humedad: {humidity}%. Viento: {wind_speed} m/s."
    )