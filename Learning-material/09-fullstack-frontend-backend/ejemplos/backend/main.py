from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import jwt, datetime, hmac, hashlib

SECRET = "clave_de_ejemplo_no_usar_en_produccion"
app = FastAPI()

# CORS: solo el frontend legítimo puede consumir la API desde el navegador
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# "base de datos" de ejemplo: usuario con contraseña hasheada
def hash_pw(p): return hashlib.sha256(p.encode()).hexdigest()  # demo; en real: bcrypt/argon2
USUARIOS = {"carlos@ejemplo.com": {"pw": hash_pw("secreto123"), "nombre": "Carlos", "rol": "user"}}

class Login(BaseModel):
    email: str
    password: str

def crear_token(email, rol):
    payload = {"sub": email, "rol": rol,
               "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}
    return jwt.encode(payload, SECRET, algorithm="HS256")

@app.post("/login")
def login(datos: Login):
    u = USUARIOS.get(datos.email)
    if not u or u["pw"] != hash_pw(datos.password):
        raise HTTPException(401, "credenciales invalidas")   # mensaje genérico
    return {"token": crear_token(datos.email, u["rol"])}

# dependencia que verifica el token en cada endpoint protegido
seguridad = HTTPBearer()
def usuario_actual(cred: HTTPAuthorizationCredentials = Depends(seguridad)):
    try:
        payload = jwt.decode(cred.credentials, SECRET, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(401, "token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(401, "token invalido")

@app.get("/perfil")
def perfil(user=Depends(usuario_actual)):
    email = user["sub"]
    return {"email": email, "nombre": USUARIOS[email]["nombre"], "rol": user["rol"]}
