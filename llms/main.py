from fastapi import FastAPI, Depends, HTTPException, status, Header
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

# Importaciones locales
import app.database
import app.llm_services
import app.auth

app = FastAPI(title="API de Aprendizaje con Login")

# --- ENDPOINTS DE AUTENTICACIÓN ---

from fastapi import FastAPI, Depends, HTTPException, status, Header
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

app = FastAPI(title="API de Aprendizaje Personalizado")

# --- Endpoints de Autenticación ---
@app.post("/register")
def register_user(form_data: OAuth2PasswordRequestForm = Depends()):
    db_user = database.get_user_by_username(form_data.username)
    if db_user:
        raise HTTPException(status_code=400, detail="El nombre de usuario ya existe.")
    hashed_password = auth.get_password_hash(form_data.password)
    database.create_user(form_data.username, hashed_password)
    return {"message": f"Usuario {form_data.username} registrado con éxito."}

@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = database.get_user_by_username(form_data.username)
    if not user or not auth.verify_password(form_data.password, user[1]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Nombre de usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(data={"sub": user[0]})
    return {"access_token": access_token, "token_type": "bearer"}

# --- Función Guardián para Proteger Endpoints ---
async def get_current_user(authorization: Annotated[str, Header()]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
    )
    try:
        token = authorization.split(" ")[1]
        payload = auth.jwt.decode(token, auth.SECRET_KEY, algorithms=[auth.ALGORITHM])
        username: str = payload.get("sub")
        if username is None: raise credentials_exception
    except (auth.JWTError, IndexError):
        raise credentials_exception
    user = database.get_user_by_username(username)
    if user is None: raise credentials_exception
    return user[0]

# --- Endpoint Principal Protegido ---
@app.post("/learn/")
def learn_topic(tema: str, current_user: Annotated[str, Depends(get_current_user)]):
    if not tema:
        raise HTTPException(status_code=400, detail="El tema es requerido.")
    
    username = current_user
    resumen = llm_services.generar_resumen(tema)
    database.add_topic_to_history(username, tema)
    historial_actualizado = database.get_user_history(username)
    sugerencias = llm_services.sugerir_temas_relacionados(tema, historial_actualizado)
    
    return {
        "usuario": username,
        "tema_aprendido": tema,
        "resumen": resumen,
        "sugerencias_para_ti": sugerencias
    }
