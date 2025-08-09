from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from typing import Optional

# --- MongoDB (Motor) ---
# from motor.motor_asyncio import AsyncIOMotorClient

# --- Firebase ---
# import firebase_admin
# from firebase_admin import credentials, firestore

# --- OpenAI ---
# import openai

app = FastAPI(
    title="México Global AI Hackathon Starter Kit",
    description="API template para proyectos clásicos de IA con endpoints para subir archivos, prompts y conectar con modelos externos.",
    version="1.0.0"
)

# --- MongoDB INIT ---
# @app.on_event("startup")
# async def startup_db_client():
#     app.mongodb_client = AsyncIOMotorClient("mongodb://localhost:27017")
#     app.mongodb = app.mongodb_client["mi_base_de_datos"]
#
# @app.on_event("shutdown")
# async def shutdown_db_client():
#     app.mongodb_client.close()

# --- Firebase INIT ---
# cred = credentials.Certificate("ruta/a/tu/credencial.json")
# firebase_admin.initialize_app(cred)
# db = firestore.client()

@app.post("/upload/csv")
async def upload_csv(file: UploadFile = File(...)):
    content = await file.read()
    # --- MongoDB ejemplo ---
    # await app.mongodb["csv_uploads"].insert_one({"filename": file.filename, "content": content})
    # --- Firebase ejemplo ---
    # db.collection("csv_uploads").add({"filename": file.filename, "content": content.decode("utf-8")})
    return {"filename": file.filename, "status": "CSV recibido"}

@app.post("/upload/image")
async def upload_image(file: UploadFile = File(...)):
    content = await file.read()
    # --- MongoDB ejemplo ---
    # await app.mongodb["image_uploads"].insert_one({"filename": file.filename, "content": content})
    # --- Firebase ejemplo ---
    # db.collection("image_uploads").add({"filename": file.filename})
    return {"filename": file.filename, "status": "Imagen recibida"}

@app.post("/prompt")
async def send_prompt(prompt: str = Form(...)):
    # --- MongoDB ejemplo ---
    # await app.mongodb["prompts"].insert_one({"prompt": prompt})
    # --- Firebase ejemplo ---
    # db.collection("prompts").add({"prompt": prompt})
    # --- OpenAI ejemplo ---
    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[{"role": "user", "content": prompt}]
    # )
    # output = response.choices[0].message["content"]
    # return {"prompt": prompt, "output": output}
    return {"prompt": prompt, "status": "Prompt recibido"}

@app.get("/result/{task_id}")
async def get_result(task_id: str):
    # --- MongoDB ejemplo ---
    # result = await app.mongodb["results"].find_one({"task_id": task_id})
    # --- Firebase ejemplo ---
    # result = db.collection("results").document(task_id).get().to_dict()
    # return {"task_id": task_id, "result": result.get("output") if result else None}
    return {"task_id": task_id, "result": "Aquí va el resultado"}

@app.post("/transform")
async def transform_data(data: dict):
    # --- MongoDB ejemplo ---
    # await app.mongodb["transforms"].insert_one({"input": data})
    # --- Firebase ejemplo ---
    # db.collection("transforms").add({"input": data})
    return {"input": data, "output": "Transformación realizada"}

@app.get("/download/{file_id}")
async def download_file(file_id: str):
    # --- MongoDB ejemplo ---
    # file_doc = await app.mongodb["files"].find_one({"file_id": file_id})
    # --- Firebase ejemplo ---
    # file_doc = db.collection("files").document(file_id).get().to_dict()
    # download_url = file_doc.get("download_url") if file_doc else None
    # return {"file_id": file_id, "download_url": download_url}
    return {"file_id": file_id, "download_url": f"https://example.com/files/{file_id}"}