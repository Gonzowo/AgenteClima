from langchain_ollama import ChatOllama
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from tool_weather import get_weather

# Configurar el modelo de Ollama apuntando al puerto 11434
llm = ChatOllama(
    model="llama3", 
    temperature=0,
    base_url="http://localhost:11434" # Ajusta a la IP de tu servidor si no es local
)

# Lista de herramientas disponibles para el agente
tools = [get_weather]

# Crear el prompt del agente
prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un asistente meteorológico. Utiliza tus herramientas para responder preguntas sobre el clima."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

# Inicializar el agente y el ejecutor
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

if __name__ == "__main__":
    pregunta = "¿Cómo está el clima en Talca, Chile?"
    respuesta = agent_executor.invoke({"input": pregunta})
    print("\nRespuesta Final:")
    print(respuesta["output"])