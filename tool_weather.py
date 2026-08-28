import os
import requests
from langchain.tools import tool
from dotenv import load_dotenv

load_dotenv()

@tool
def get_weather(city: str) -> str:
    """Obtiene el clima actual para una ciudad especificada."""
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=es"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        return f"El clima en {city} es de {temp}°C con {desc}."
    return "No se pudo obtener la información del clima. Verifica el nombre de la ciudad o la API Key."