from fastapi import FastAPI
from pydantic import BaseModel
import requests, json

app = FastAPI()

MISTRAL_URL = "https://api.mistral.ai/v1/chat/completions"
MISTRAL_MODEL = "mistral-small-latest"  # or any available instruct-capable model
MISTRAL_API_KEY = "your_api_key_here"

class TopicRequest(BaseModel):
    topic: str

@app.post("/generate-text")
async def generate_text(req: TopicRequest):
    system_prompt = (
        f"Explica el tema '{req.topic}' en un texto educativo "
        "de aproximadamente 5 minutos de lectura, con lenguaje claro y estructurado."
    )
    payload = {
        "model": MISTRAL_MODEL,
        "messages": [
            {"role": "user", "content": system_prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 512
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {MISTRAL_API_KEY}"
    }
    res = requests.post(MISTRAL_URL, headers=headers, json=payload)
    data = res.json()
    return {"text": data["choices"][0]["message"]["content"]}
