# 20 · Deploy a la nube

De local a producción con Railway o Render: preparar la app, desplegar, conectar base de datos, manejar secretos, y dominio con HTTPS.

## Qué hay acá
- `manual.html` — 7 capítulos: qué es desplegar un backend (estático vs dinámico), preparar la app (config por entorno, comando de producción, healthcheck), desplegar paso a paso, la base de datos y los secretos, dominio propio y HTTPS, y checklist.
- `ejemplos/` — una app FastAPI lista para producción y sus archivos de deploy: `main.py`, `requirements.txt`, `Procfile`, `Dockerfile`, `render.yaml`.
- `ejemplos/pruebas.txt` — salida real: la app corriendo con el comando de producción (gunicorn), leyendo PORT y ENTORNO del entorno.

## Probar en local (modo producción)
```
pip install -r requirements.txt
PORT=9099 ENTORNO=production gunicorn main:app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT
```
