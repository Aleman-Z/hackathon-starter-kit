# 🎧 "Spotify for Learning" Personalizado con IA 🤖

Este proyecto contiene la lógica de backend para una aplicación de aprendizaje personalizado. El sistema utiliza un Modelo de Lenguaje Grande (LLM) y una arquitectura de Generación Aumentada por Recuperación (RAG) para generar resúmenes educativos y sugerir nuevos temas basados en el historial del usuario.

---

## 🌟 Estado Actual del Proyecto

Este repositorio está organizado en dos ramas principales:

* **`main`**: Contiene la estructura final y la lógica de negocio modularizada dentro de la carpeta `app/`. Está preparada para ser conectada a una API web con FastAPI, pero **aún no está integrada**.

* **`simulaciones`** (Rama de Pruebas): Esta es la **rama activa para probar la funcionalidad actual**. Contiene un script (`full_simulation.py`) que simula el comportamiento de un usuario y prueba toda la lógica del backend (LLMs, RAG, Base de Datos) sin necesidad de una API web.

---

## 🏛️ Arquitectura y Lógica

El backend está construido con una arquitectura modular para separar responsabilidades.

* **🗃️ Base de Datos**: **SQLite** para almacenar usuarios, historial de aprendizaje y una base de conocimiento interna para RAG.

* **🧠 Modelo de Lenguaje (LLM)**: **Mistral** para la generación de texto.

* **📚 Generación Aumentada por Recuperación (RAG)**: Se utiliza un enfoque híbrido para generar resúmenes precisos y sugerencias personalizadas.

---

## 📂 Estructura del Proyecto (en `main` y `simulaciones`)

* `app/`: Paquete que contiene toda la lógica de negocio.

    * `llm_services.py`: Lógica para interactuar con la API de Mistral.

    * `database.py`: Funciones para interactuar con la base de datos SQLite.

    * `create_db.py`: Script para inicializar la base de datos.

    * `seed_db.py`: Script para poblar la base de conocimiento.

* `full_simulation.py`: (Solo en la rama `simulaciones`) Script para probar la lógica sin una API.

* `.env`: Archivo para guardar claves secretas.

---

## 🚀 Cómo Probar el Proyecto (Usando la Rama `simulaciones`)

Para probar la funcionalidad actual, primero clona el repositorio y muévete a la rama de simulación.

### 1. Preparación Inicial

1.  **Clona el repositorio:**

    ```bash
    git clone [https://tu-repositorio.git](https://tu-repositorio.git)
    cd tu-proyecto
    ```

2.  **Cambia a la rama de simulación:**

    ```bash
    git checkout simulaciones
    ```

3.  **(Recomendado) Crea y activa un entorno virtual:**

    ```bash
    python -m venv venv
    # En Windows
    venv\Scripts\activate
    # En macOS/Linux
    source venv/bin/activate
    ```

4.  **Instala las dependencias:**

    ```bash
    pip install "mistralai" "python-dotenv" "passlib[bcrypt]" "python-jose[cryptography]" fastapi[all]
    ```

    *(Nota: Las dependencias de FastAPI y seguridad no son estrictamente necesarias para la simulación, pero se pueden instalar para preparar el siguiente paso).*

5.  **Configura tus variables de entorno:**
    Crea un archivo llamado `.env` en la raíz del proyecto y añade tu clave de Mistral.

    ```env
    # .env
    MISTRAL_API_KEY="tu_api_key_de_mistral_aqui"
    ```

### 2. Configuración de la Base de Datos

1.  **Inicializa la Base de Datos:**
    Ejecuta este comando una sola vez desde la raíz del proyecto.

    ```bash
    python app/create_db.py
    ```

2.  **(Opcional) Puebla la Base de Conocimiento:**
    Para probar la funcionalidad RAG, ejecuta este script.

    ```bash
    python app/seed_db.py
    ```

### 3. Ejecutar la Simulación

Ahora, ejecuta el script de simulación para ver toda la lógica en acción directamente en tu terminal.

```bash
python full_simulation.py

---

## 📈 Próximos Pasos (En la rama `main`)

El siguiente gran objetivo es conectar toda la lógica probada a una API web.

-   [ ] **Integrar con FastAPI:** Mover la lógica de `full_simulation.py` a los endpoints en `main.py`.
-   [ ] **Implementar Autenticación:** Activar la lógica de `auth.py` para los endpoints `/register` y `/token`.
-   [ ] **Proteger Endpoints:** Asegurar el endpoint `/learn/` para que solo usuarios autenticados puedan acceder.
-   [ ] **Conectar con Frontend:** Permitir que una aplicación web interactúe con la API.
