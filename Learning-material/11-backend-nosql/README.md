# 11 · Backend NoSQL, de 0 hasta el deploy

Cómo armar un backend con base de datos NoSQL (MongoDB) desde cero, hasta dejar una base funcionando en MongoDB Atlas. Fundamentos, pensar en documentos, CRUD por API, modelado (embeber vs referenciar), agregación, seguridad y deploy.

## Qué hay acá
- `manual.html` — 15 capítulos: qué es NoSQL y sus tipos, pensar en documentos, usar MongoDB (local y Atlas), operaciones y operadores ($gt, $in), CRUD paso a paso (Python y Node), modelado (embeber vs referenciar), índices y agregación, SQL vs NoSQL (cuándo cada uno), seguridad (inyección NoSQL), deploy en Atlas, y construir con IA.
- `ejemplos/backend/app.py` — FastAPI + pymongo + MongoDB, CRUD de /tareas. Mismo código anda con Atlas cambiando la URL.
- `ejemplos/backend/server.js` — el mismo CRUD en Express + driver oficial de MongoDB.
- `ejemplos/salida/pruebas.txt` — salida real corrida contra un MongoDB 7.0: CRUD completo y queries crudas con operadores y agregación.

## Probar (Python)
```
# necesitás un MongoDB corriendo en local (mongod) o una URL de Atlas
cd ejemplos/backend
pip install fastapi uvicorn pymongo
uvicorn app:app --reload
```
