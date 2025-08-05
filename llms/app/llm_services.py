import os
import json
from mistralai import Mistral
import re
from dotenv import load_dotenv
from app import database
load_dotenv()

def consultar_llm(prompt: str):
    """
    Función base para enviar cualquier prompt a la API de Mistral.
    """
    try:
        # MISTRAL_API_KEY está en .env
        api_key = os.environ.get("MISTRAL_API_KEY")
        if not api_key:
            print("Error: La MISTRAL_API_KEY no fue encontrada.")
            return None

        client = Mistral(api_key=api_key)
        messages = [{"role": "user", "content": prompt}]
        
        respuesta = client.chat.complete(
            model="mistral-small-latest", 
            messages=messages
        )
        return respuesta.choices[0].message.content
        
    except Exception as e:
        print(f"Error en la API de Mistral (tipo {type(e)}): {e}")
        return None

def recuperar_conocimiento(tema: str) -> str | None:
    """
    Paso de "Recuperación" (Retrieval) de RAG.
    Busca en la base de datos un artículo sobre el tema.
    """
    # Convierte un tema como "Agujeros Negros" en una clave como "agujeros_negros"
    topic_key = tema.lower().replace(" ", "_")
    
    # Llama a la función que hemos creado en database.py
    contenido = database.get_knowledge_by_topic(topic_key)
    
    if contenido:
        print(f"✅ Conocimiento encontrado para '{tema}' en la base de datos.")
        return contenido
    else:
        print(f"❌ No se encontró conocimiento en la DB para '{tema}'. Usando conocimiento general del LLM.")
        return None

def generar_resumen(tema: str):
    """
    Paso de "Generación" (Generation) de RAG.
    Genera un resumen usando el conocimiento recuperado si existe.
    """
    conocimiento_recuperado = recuperar_conocimiento(tema)
    
    if conocimiento_recuperado:
        # --- Prompt Aumentado con RAG ---
        # Si encontramos información en nuestra DB, le pedimos al LLM que la resuma.
        prompt = f"""
        Actúa como un experto que resume textos de forma clara y concisa para un podcast.
        Basándote ÚNICAMENTE en el siguiente texto, genera un resumen de 25-50 palabras.
        No uses ninguna información externa.

        ### TEXTO PROPORCIONADO:
        {conocimiento_recuperado}
        
        ### RESUMEN:
        """
    else:
        # --- Prompt Original (Fallback) ---
        # Si no encontramos información, le pedimos al LLM que use su memoria.
        prompt = f"""
        Actúa como un narrador experto de podcasts. Tu tarea es generar un guion corto y atractivo.
        REQUISITOS:
        1. Tono: Conversacional y entusiasta.
        2. Estructura: "¿Qué es?, ¿Por qué es importante?, ¿Cómo funciona/ocurrió?".
        3. Longitud: 25-50 palabras.
        4. Formato: Solo el texto del guion, sin títulos.
        TEMA: {tema}
        """
        
    return consultar_llm(prompt)

def sugerir_temas_relacionados(tema_actual: str, historial_temas: list):
    historial_str = ", ".join(historial_temas)
    prompt_sugerencias = f"""
    Actúa como un curador de contenido experto.
    Un usuario acaba de aprender sobre: "{tema_actual}".
    Su historial de temas es: {historial_str}.
    Sugiere 5 nuevos temas relacionados.
    Devuelve tu respuesta únicamente como una lista en formato JSON.
    Formato estricto: ["Tema 1", "Tema 2", "Tema 3", "Tema 4", "Tema 5"]
    """
    respuesta_str = consultar_llm(prompt_sugerencias)
    if not respuesta_str: return []
    match = re.search(r'\[.*\]', respuesta_str, re.DOTALL)
    if not match: return []
    try:
        return json.loads(match.group(0))
    except json.JSONDecodeError:
        return []
