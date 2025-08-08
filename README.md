# 🎧 Hackathon Starter Kit – *Spotify para el Aprendizaje*

Este repositorio contiene una estructura modular de proyecto diseñada para construir una aplicación educativa basada en audio, inspirada en la idea de *Spotify para el aprendizaje*. Fue creado para facilitar el desarrollo rápido durante hackatones y contiene archivos base para todos los componentes principales de la aplicación.

## 🧠 Descripción del Proyecto

El objetivo de esta app es ofrecer a los usuarios resúmenes educativos de 5 minutos en formato de audio, adaptados a sus intereses — como un asistente de aprendizaje estilo podcast. El backend integra modelos de lenguaje, procesamiento de texto a voz y seguimiento de preferencias. El frontend permite la selección de temas y la exploración de recomendaciones mediante una interfaz intuitiva.

## 📁 Estructura del Repositorio

Cada carpeta corresponde a un equipo o módulo funcional:

- **`audio/`**  
  Herramientas y scripts para convertir texto educativo en audio natural, usando APIs como Eleven Labs u otros servicios TTS.

- **`backend/`**  
  Backend basado en FastAPI que orquesta la interacción entre los LLMs, el módulo de audio y el frontend. Incluye endpoints y lógica de integración.

- **`comunicación/`**  
  Material compartido para la coordinación del equipo, como documentación, planeación de tareas y protocolos de comunicación.

- **`frontend/`**  
  Interfaz de usuario construida en Streamlit para ingresar temas, recibir sugerencias y reproducir los audios generados.

- **`llms/`**  
  Scripts para generar contenido educativo a partir de temas seleccionados por el usuario, usando modelos de lenguaje como Mistral o GPT.

## 🚀 Cómo empezar

Para comenzar, clona el repositorio y explora cada módulo según tu rol (frontend, backend, LLMs, etc.). El proyecto está diseñado para que los equipos trabajen de forma independiente pero dentro de una arquitectura unificada.

```bash
git clone https://github.com/Aleman-Z/hackathon-starter-kit.git
```

Cada carpeta contiene su propio README o un `main.py`/`app.py` para facilitar la puesta en marcha.

## 🙌 Créditos

Este kit fue desarrollado por **Team México** para el **Global AI Hackathon HackNation 2025**.

**Equipo y roles principales:**

| Módulo          | Integrantes                                                                 | Rol principal                                      |
|------------------|----------------------------------------------------------------------------|----------------------------------------------------|
| **Frontend**     | [@EsveBavi](https://github.com/EsveBavi), Guadalupe Vásquez                                                    | Diseño e implementación de la interfaz             |
| **Backend**      | [@Aleman-Z](https://github.com/Aleman-Z), Joaquín (Nai), Max                                                         | Creación de endpoints y conexiones                 |
| **LLMs**         | [@Brandon331](https://github.com/Brandon331)        | Generación de texto y sugerencias                 |
| **Audio**        | [@Aleman-Z](https://github.com/Aleman-Z), Deya                             | Conversión de texto a audio tipo podcast           |
| **Comunicación** | [@AlfonsoGovela](https://github.com/AlfonsoGovela), Deya                  | Documentación, narrativa, visibilidad              |
