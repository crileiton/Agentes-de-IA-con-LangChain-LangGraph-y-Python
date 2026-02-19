from dotenv import load_dotenv
load_dotenv()

from langchain_openai import AzureChatOpenAI

llm = AzureChatOpenAI(
    azure_deployment="gpt-4o",
    api_version="2024-08-01-preview",
    temperature=0.7,
)

pregunta = "¿En qué año llegó el ser humano a la Luna por primera vez?"
print("Pregunta: ", pregunta)

respuesta = llm.invoke(pregunta)
print("Respuesta del modelo: ", respuesta.content)