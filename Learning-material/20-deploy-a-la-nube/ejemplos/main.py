"""App lista para producción: lee la config del entorno, no hardcodeada."""
import os
from fastapi import FastAPI

app = FastAPI(title="App para deploy")

# TODO lo configurable viene del entorno (librito 09, 10, 16...)
ENTORNO = os.getenv("ENTORNO", "development")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./local.db")

@app.get("/")
def raiz():
    return {"app": "tienda", "entorno": ENTORNO}

@app.get("/health")
def health():
    return {"estado": "ok"}
