# 10 · Backend SQL, de 0 hasta el deploy

Cómo armar un backend con base de datos relacional desde cero, hasta dejar una base Postgres funcionando en internet. Fundamentos, SQL, diseño de esquema, CRUD por API, migraciones, seguridad (inyección SQL) y deploy en un servicio gestionado.

## Qué hay acá
- `manual.html` — 15 capítulos: qué es una base relacional, el lenguaje SQL, diseñar el esquema, elegir motor (SQLite/Postgres/MySQL), ORM vs SQL crudo, CRUD paso a paso (Python y Node), migraciones, seguridad (inyección SQL demostrada de verdad), índices, deploy de una Postgres gestionada (Neon/Supabase), backups, y construir con IA.
- `ejemplos/backend/app.py` — FastAPI + SQLAlchemy + SQLite, CRUD de /tareas. Mismo código anda con Postgres cambiando la URL.
- `ejemplos/backend/server.js` — el mismo CRUD en Express + better-sqlite3.
- `ejemplos/salida/pruebas.txt` — salida real: CRUD completo y la demo de inyección SQL (concatenar vs parametrizar).

## Probar (Python)
```
cd ejemplos/backend
pip install fastapi uvicorn sqlalchemy
uvicorn app:app --reload
```
