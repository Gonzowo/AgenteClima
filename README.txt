# Agente Meteorológico con Ollama y LangChain Tools

1. Activa tu entorno virtual: `.venv\Scripts\activate` (Windows) o `source .venv/bin/activate` (Mac/Linux).
2. Instala dependencias: `pip install -r requirements.txt`.
3. Crea un archivo `.env` con tu API key:
	`OPENWEATHERMAP_API_KEY=tu_api_key`
4. Instala y descarga el modelo de Ollama:
	`ollama pull qwen3.5:9b-mlx`
5. Asegúrate de que Ollama esté corriendo en `http://localhost:11434`.
6. Ejecuta `python agent.py` y escribe una ciudad, por ejemplo `Talca, Chile`.

`get_weather` es una LangChain Tool creada con `@tool`. El agente decide cuándo
invocarla y usa la API de OpenWeatherMap para consultar el clima actual.
