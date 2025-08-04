# Mistral API Backend (FastAPI)

Este proyecto proporciona un backend sencillo en FastAPI que expone un endpoint para interactuar con el modelo `codestral-2405` de Mistral (vía endpoint de FIM: Fill-in-the-middle).

## 📂 Archivos incluidos

- `main.py`: Servidor FastAPI con un endpoint POST `/generate-code`.
- `requirements.txt`: Dependencias necesarias.
- `README.md`: Este documento.

## 🚀 Cómo ejecutar

### 1. Instala dependencias

```bash
pip install fastapi uvicorn requests
```

### 2. Agrega tu API Key de Mistral

Edita el archivo `main.py` y reemplaza:

```python
MISTRAL_API_KEY = "your_api_key_here"
```

por tu clave real de Mistral.

### 3. Ejecuta el servidor

```bash
uvicorn main:app --reload
```

Por defecto, estará disponible en: `http://127.0.0.1:8000`

## 🌐 Interfaz de prueba rápida (Swagger UI)

Abre tu navegador y entra a:

**http://127.0.0.1:8000/docs**

Ahí verás una interfaz donde puedes probar el endpoint **POST /generate-code**. Solo haz clic en "Try it out" y escribe tu prompt, por ejemplo:

```json
{
  "prompt": "def fibonacci(n):"
}
```

Haz clic en **Execute** para ver la respuesta del modelo.

## 📡 Endpoint disponible

### `POST /generate-code`

**Descripción**: Envía un `prompt` al modelo `codestral-2405` de Mistral para completar código.

**Body JSON de ejemplo**:

```json
{
  "prompt": "def fibonacci(n):"
}
```

**Respuesta esperada**:

```json
{
  "generated_code": "    if n <= 0:\n        return []\n    elif n == 1:\n        return [0]\n    ..."
}
```

## 🛠️ Notas

- Este ejemplo usa el endpoint FIM (fill-in-the-middle) de Mistral.
- Asegúrate de respetar los límites de uso de la API.

## 📬 Créditos

Desarrollado como parte de un hackathon colaborativo por el equipo Backend. Para dudas, contactar a Max o Adrián.
