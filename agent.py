import os

from langchain_ollama import ChatOllama
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from tool_weather import get_weather

llm = ChatOllama(
    model=os.getenv("OLLAMA_MODEL", "qwen3.5:0.8b"),
    temperature=0,
    base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
)

tools = [get_weather]

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "Eres un asistente meteorológico. Usa la herramienta get_weather "
        "siempre que la consulta pida información del clima actual. "
        "Si falta la ciudad, solicítala. Responde en español y no inventes datos.",
    ),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True,
)

if __name__ == "__main__":
    print("Agente meteorológico con Ollama. Escribe 'salir' para terminar.")
    while True:
        pregunta = input("\n¿En qué lugar quieres consultar el clima? ").strip()
        if pregunta.lower() in {"salir", "exit", "quit"}:
            break
        if not pregunta:
            continue

        respuesta = agent_executor.invoke({"input": pregunta})
        print(f"\n{respuesta['output']}")