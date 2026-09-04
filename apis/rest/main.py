from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
# "base de datos" en memoria
usuarios = {42: {"id": 42, "nombre": "Carlos", "email": "carlos@ejemplo.com"}}

class UsuarioNuevo(BaseModel):
    nombre: str
    email: str

@app.get("/usuarios/{uid}")
def leer_usuario(uid: int):
    if uid not in usuarios:
        raise HTTPException(404, "no existe")
    return usuarios[uid]

@app.post("/usuarios", status_code=201)
def crear_usuario(u: UsuarioNuevo):
    nuevo_id = max(usuarios) + 1
    usuarios[nuevo_id] = {"id": nuevo_id, **u.model_dump()}
    return usuarios[nuevo_id]
