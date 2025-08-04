from fastapi import FastAPI, Request
import requests
import json

app = FastAPI()

MISTRAL_URL = "https://api.mistral.ai/v1/fim/completions"
MISTRAL_API_KEY = "your_api_key_here"  # Reemplaza con tu clave real

@app.post("/generate-code")
async def generate_code(request: Request):
    body = await request.json()
    prompt = body.get("prompt", "def")

    payload = {
        "model": "codestral-2405",
        "temperature": 1.5,
        "top_p": 1,
        "stream": False,
        "stop": "string",
        "random_seed": 0,
        "prompt": prompt
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {MISTRAL_API_KEY}"
    }

    response = requests.post(MISTRAL_URL, headers=headers, data=json.dumps(payload))

    try:
        return response.json()
    except Exception:
        return {"error": "Invalid response from Mistral API", "raw": response.text}
