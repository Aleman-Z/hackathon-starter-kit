from fastapi import FastAPI, Request
from pydantic import BaseModel
import requests
import json
import base64

app = FastAPI()

# Configuración de Mistral
MISTRAL_URL = "https://api.mistral.ai/v1/chat/completions"
MISTRAL_MODEL = "mistral-small-latest"
MISTRAL_API_KEY = ""

# Configuración de ElevenLabs
ELEVENLABS_API_KEY = ""
VOICE_ID = "21m00Tcm4TlvDq8ikWAM"

class TopicRequest(BaseModel):
    topic: str

class TextRequest(BaseModel):
    text: str

@app.post("/generate-text")
async def generate_text(req: TopicRequest):
    system_prompt = (
        f"Explica el tema '{req.topic}' en un texto educativo "
        "de aproximadamente 5 minutos de lectura, con lenguaje claro y estructurado."
    )
    payload = {
        "model": MISTRAL_MODEL,
        "messages": [{"role": "user", "content": system_prompt}],
        "temperature": 0.7,
        "max_tokens": 2048,
        "top_p": 1,
        "stream": False
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {MISTRAL_API_KEY}"
    }
    res = requests.post(MISTRAL_URL, headers=headers, json=payload)
    data = res.json()
    return {"text": data["choices"][0]["message"]["content"]}

@app.post("/generate-audio")
async def generate_audio(req: TextRequest):
    def format_text_with_ssml(text):
        paragraphs = text.strip().split("\\n")
        ssml = "<speak>"
        for para in paragraphs:
            clean_para = para.strip()
            if clean_para:
                ssml += f"<p>{clean_para}</p><break time='500ms'/>"
        ssml += "</speak>"
        return ssml

    ssml_text = format_text_with_ssml(req.text)

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": ssml_text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        },
        "text_type": "ssml"
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        audio_base64 = base64.b64encode(response.content).decode("utf-8")
        return {"audio_base64": audio_base64}
    else:
        return {"error": response.text}
