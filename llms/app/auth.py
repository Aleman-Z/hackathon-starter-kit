from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
import os
#Modulo de autenticacion
# --- Configuración de Seguridad ---
SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Contexto para hashear contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# --- Funciones de Seguridad ---
def verify_password(plain_password, hashed_password):
    """Verifica una contraseña plana contra su hash."""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    """Genera el hash de una contraseña."""
    return pwd_context.hash(password)

def create_access_token(data: dict):
    """Crea un Token de Acceso JWT."""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt