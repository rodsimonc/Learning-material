"""
Backend NoSQL de 0: FastAPI + MongoDB (pymongo).
CRUD de 'tareas' guardadas como documentos.
Mismo codigo anda con MongoDB Atlas cambiando solo la URL de conexion.
"""
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
from bson.errors import InvalidId

# --- Conexion ---
# Local para desarrollo. En produccion (Atlas) seria algo asi:
# MONGO_URL = "mongodb+srv://usuario:pass@cluster0.xxxx.mongodb.net/?retryWrites=true"
MONGO_URL = os.getenv("MONGO_URL", "mongodb://127.0.0.1:27017")
cliente = MongoClient(MONGO_URL)
base = cliente["miapp"]          # la base de datos
tareas = base["tareas"]          # la coleccion (equivale a una tabla)


class TareaIn(BaseModel):
    titulo: str
    hecha: bool = False


def a_salida(doc):
    # Mongo guarda el id como ObjectId; lo pasamos a texto para el JSON
    return {"id": str(doc["_id"]), "titulo": doc["titulo"], "hecha": doc["hecha"]}


def oid(tid):
    try:
        return ObjectId(tid)
    except InvalidId:
        raise HTTPException(400, "id invalido")


app = FastAPI(title="Backend NoSQL demo")


@app.post("/tareas")
def crear(t: TareaIn):
    r = tareas.insert_one(t.model_dump())
    return a_salida(tareas.find_one({"_id": r.inserted_id}))


@app.get("/tareas")
def listar():
    return [a_salida(d) for d in tareas.find()]


@app.get("/tareas/{tid}")
def ver(tid: str):
    d = tareas.find_one({"_id": oid(tid)})
    if not d:
        raise HTTPException(404, "no existe")
    return a_salida(d)


@app.put("/tareas/{tid}")
def actualizar(tid: str, t: TareaIn):
    r = tareas.update_one({"_id": oid(tid)}, {"$set": t.model_dump()})
    if r.matched_count == 0:
        raise HTTPException(404, "no existe")
    return a_salida(tareas.find_one({"_id": oid(tid)}))


@app.delete("/tareas/{tid}")
def borrar(tid: str):
    r = tareas.delete_one({"_id": oid(tid)})
    if r.deleted_count == 0:
        raise HTTPException(404, "no existe")
    return {"borrada": tid}
