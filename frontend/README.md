# 🎨 Frontend - Spotify for Learning

Esta carpeta contiene la interfaz de usuario de la aplicación **Spotify for Learning**, desarrollada en **Streamlit**. Aquí los usuarios pueden escribir un tema de interés, obtener un resumen generado por IA, convertirlo en audio y escucharlo o descargarlo en formato podcast.

---

## 📌 Archivo principal

- `spotifyforlearning.py`  
  Interfaz completa en Streamlit con estilos personalizados en CSS, conexión al backend y generación dinámica de contenido educativo en texto y audio.

---

## 🚀 Funcionalidades

- Interfaz moderna y responsiva para cualquier dispositivo.
- Entrada de texto para temas de interés.
- Visualización del resumen generado.
- Botón para generar audio tipo podcast usando Eleven Labs.
- Reproductor de audio embebido y opción de descarga.
- Navbar personalizada y estilos consistentes con diseño profesional.

---

## ▶️ Cómo ejecutar

Asegúrate de tener el backend corriendo por separado (ver carpeta `backend/`), y luego ejecuta:

```bash
streamlit run spotifyforlearning.py
```

---

## 🔗 Requisitos

- Python 3.8+
- `streamlit`
- `requests`
- `base64`

Instálalos con:

```bash
pip install -r requirements.txt
```

> ℹ️ Este frontend espera que el backend esté disponible localmente en `http://localhost:8000`. Puedes modificar la variable `BACKEND_URL` si se aloja en otro lugar.

---

## 📁 Archivos de imagen

Asegúrate de que los siguientes archivos de imagen estén en la misma carpeta para que la interfaz se vea correctamente:

- `logo.png`
- `logo2.png` (favicon)

---

## 👥 Créditos

**Equipo México – Global AI Hackathon**  
Interfaz diseñada por **Esve**  

---
