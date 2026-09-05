"""
Sistema de autenticación con FastAPI.
- Registro con contraseña hasheada (bcrypt)
- Login que devuelve access token (corto) + refresh token (largo)
- Endpoints protegidos y control por rol
- Refresh: renovar el access token sin volver a loguearse
"""
from datetime import datetime, timedelta, timezone
import bcrypt
import jwt
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel

SECRET = "cambiar-esto-en-produccion-y-guardarlo-en-variable-de-entorno"
ALGO = "HS256"
ACCESS_MIN = 15          # el access token dura 15 minutos
REFRESH_DIAS = 7         # el refresh token dura 7 días

app = FastAPI(title="Auth demo")
seguridad = HTTPBearer()

# "base de datos" en memoria para el ejemplo (en real, Postgres, librito 10)
USUARIOS: dict[str, dict] = {}


# ---------- Contraseñas ----------
def hash_pw(pw: str) -> str:
    return bcrypt.hashpw(pw.encode(), bcrypt.gensalt()).decode()

def verificar_pw(pw: str, hashed: str) -> bool:
    return bcrypt.checkpw(pw.encode(), hashed.encode())


# ---------- Tokens ----------
def crear_token(email: str, rol: str, tipo: str, minutos: int) -> str:
    ahora = datetime.now(timezone.utc)
    payload = {"sub": email, "rol": rol, "tipo": tipo,
               "iat": ahora, "exp": ahora + timedelta(minutes=minutos)}
    return jwt.encode(payload, SECRET, algorithm=ALGO)

def decodificar(token: str) -> dict:
    try:
        return jwt.decode(token, SECRET, algorithms=[ALGO])
    except jwt.ExpiredSignatureError:
        raise HTTPException(401, "token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(401, "token invalido")


# ---------- Dependencias de protección ----------
def usuario_actual(cred: HTTPAuthorizationCredentials = Depends(seguridad)) -> dict:
    datos = decodificar(cred.credentials)
    if datos.get("tipo") != "access":
        raise HTTPException(401, "se requiere un access token")
    return datos

def requiere_rol(rol: str):
    def check(u: dict = Depends(usuario_actual)) -> dict:
        if u["rol"] != rol:
            raise HTTPException(403, f"requiere rol '{rol}'")
        return u
    return check


# ---------- Modelos ----------
class Registro(BaseModel):
    email: str
    password: str
    rol: str = "cliente"

class Login(BaseModel):
    email: str
    password: str

class Refresh(BaseModel):
    refresh_token: str


# ---------- Endpoints ----------
@app.post("/registro")
def registro(r: Registro):
    if r.email in USUARIOS:
        raise HTTPException(409, "el email ya está registrado")
    USUARIOS[r.email] = {"email": r.email, "pw": hash_pw(r.password), "rol": r.rol}
    return {"email": r.email, "rol": r.rol, "mensaje": "registrado"}

@app.post("/login")
def login(l: Login):
    u = USUARIOS.get(l.email)
    if not u or not verificar_pw(l.password, u["pw"]):
        # mismo error para "no existe" y "clave mala": no revelar cuál
        raise HTTPException(401, "credenciales invalidas")
    return {
        "access_token": crear_token(u["email"], u["rol"], "access", ACCESS_MIN),
        "refresh_token": crear_token(u["email"], u["rol"], "refresh", REFRESH_DIAS * 1440),
        "token_type": "bearer",
    }

@app.post("/refresh")
def refresh(r: Refresh):
    datos = decodificar(r.refresh_token)
    if datos.get("tipo") != "refresh":
        raise HTTPException(401, "se requiere un refresh token")
    return {"access_token": crear_token(datos["sub"], datos["rol"], "access", ACCESS_MIN),
            "token_type": "bearer"}

@app.get("/perfil")
def perfil(u: dict = Depends(usuario_actual)):
    return {"email": u["sub"], "rol": u["rol"]}

@app.get("/admin")
def admin(u: dict = Depends(requiere_rol("admin"))):
    return {"mensaje": f"bienvenido admin {u['sub']}", "panel": "interno"}
