from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json

app = FastAPI()

MISTRAL_URL = "https://api.mistral.ai/v1/fim/completions"
MISTRAL_API_KEY = "your_api_key_here"  # Reemplaza con tu clave real


class PromptRequest(BaseModel):
    prompt: str


@app.post("/generate-code")
async def generate_code(request: PromptRequest):
    payload = {
        "model": "codestral-2405",
        "temperature": 1.5,
        "top_p": 1,
        "stream": False,
        "stop": "string",
        "random_seed": 0,
        "prompt": request.prompt
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {MISTRAL_API_KEY}"
    }

    response = requests.post(MISTRAL_URL, headers=headers, data=json.dumps(payload))

    try:
        result = response.json()
        return {"generated_code": result["choices"][0]["message"]["content"]}
    except Exception:
        return {"error": "Invalid response from Mistral API", "raw": response.text}
