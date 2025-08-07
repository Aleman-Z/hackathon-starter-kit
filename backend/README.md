# 🧠 Backend API - Generación de Texto y Audio Educativo

Este backend en **FastAPI** permite generar textos educativos usando el modelo de lenguaje de **Mistral** y convertirlos en audio tipo podcast usando la API de **ElevenLabs**. Es parte del prototipo de una app llamada **"Spotify for Learning"** desarrollado durante el hackathon.

## 📂 Estructura del repositorio

- `main.py`: Servidor FastAPI con dos endpoints:
  - `POST /generate-text`: Genera un texto educativo a partir de un tema.
  - `POST /generate-audio`: Convierte el texto en audio tipo podcast.
- `requirements.txt`: Lista de dependencias.
- `README.md`: Este archivo.

## ⚙️ Requisitos

Instala las dependencias necesarias:

```bash
pip install fastapi uvicorn requests pydantic
```

## 🔐 Configura tus claves API

Edita el archivo `main.py` y reemplaza los valores vacíos con tus claves reales:

```python
MISTRAL_API_KEY = "TU_API_KEY_MISTRAL"
ELEVENLABS_API_KEY = "TU_API_KEY_ELEVENLABS"
```

También puedes cambiar el `VOICE_ID` si deseas usar una voz diferente.

## 🚀 Cómo ejecutar el servidor

En la raíz del backend, ejecuta:

```bash
uvicorn main:app --reload
```

Por defecto estará disponible en: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 🧪 Prueba rápida con Swagger UI

Abre tu navegador en: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
Aquí podrás probar los endpoints fácilmente.

## 📡 Endpoints disponibles

### `POST /generate-text`

**Descripción**: Genera un texto educativo de ~5 minutos basado en un tema.

**JSON de entrada**:

```json
{
  "topic": "La fotosíntesis"
}
```

**Respuesta**:

```json
{
  "text": "La fotosíntesis es el proceso mediante el cual..."
}
```

---

### `POST /generate-audio`

**Descripción**: Convierte un texto a audio estilo podcast utilizando ElevenLabs.

**JSON de entrada**:

```json
{
  "text": "La fotosíntesis es el proceso mediante el cual..."
}
```

**Respuesta**:

```json
{
  "audio_base64": "UklGRtYAAABXQVZFZm10IBAAAAABAAEA..."
}
```

Puedes decodificar este audio base64 para obtener un archivo `.mp3` o reproducirlo en frontend.

---

## 📝 Notas adicionales

- El texto se convierte a SSML (Speech Synthesis Markup Language) para mejorar la entonación y pausas.
- ElevenLabs requiere una cuenta y API key activa.
- Mistral también requiere una clave válida para uso de su API.

## 👥 Créditos

Desarrollado por el equipo **Backend** durante el hackathon:  
[@Aleman-Z](https://github.com/Aleman-Z), Joaquín (Nai), Max – Endpoints y lógica del servidor  
[@Aleman-Z](https://github.com/Aleman-Z) – Conversión de texto a audio  

Para dudas, contactar a Max o Adrián.
