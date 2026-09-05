# 09 · Conectar frontend y backend, seguro

Cómo unir un frontend y un backend de forma correcta y segura: las arquitecturas recomendadas, el contrato de la API, autenticación con JWT, CORS, manejo de config y secretos, y los must de seguridad. Paso a paso manual y también con las herramientas de IA vigentes.

## Qué hay acá
- `manual.html` — 15 capítulos: cómo se conectan front y back, arquitecturas (SPA+API, monolito, BFF), el contrato de la API, build manual (backend FastAPI, consumir con fetch, CORS, env vars), seguridad (JWT, HttpOnly vs localStorage, proteger endpoints, estados de error/carga), y dos capítulos sobre construir y revisar con IA (Cursor, Claude Code, Copilot, v0, Lovable, Bolt).
- `ejemplos/backend/` — el mismo demo en dos lenguajes: `main.py` (FastAPI) y `server.js` (Express). Login que devuelve JWT y endpoint `/perfil` protegido.
- `ejemplos/frontend/` — login que consume el backend con `fetch`, guarda el token y pide el perfil.
- `ejemplos/salida/pruebas.txt` — salida real de las pruebas: login OK, `/perfil` sin token = 401, con token = 200, contraseña mala = 401.

## Probar el backend (Python)
```
cd ejemplos/backend
pip install fastapi uvicorn pyjwt
uvicorn main:app --reload
```

El frontend se sirve aparte (por ejemplo con Live Server en el puerto 5500, que es el que el backend permite en CORS).
