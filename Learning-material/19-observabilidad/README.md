# 19 · Observabilidad

Saber qué pasa cuando la app se rompe, sin estar mirando: logs estructurados, request id, captura de errores, healthcheck y las herramientas para cuando el proyecto crece.

## Qué hay acá
- `manual.html` — 8 capítulos: qué es la observabilidad (logs/métricas/trazas), logs estructurados en JSON, request id, captura central de errores (sin exponer detalles), healthcheck (con chequeo de base), Sentry y métricas, y checklist.
- `ejemplos/app.py` — FastAPI con logs JSON, middleware de request id + tiempo, captura de errores, `/health` y un endpoint que falla a propósito.
- `ejemplos/pruebas.txt` — salida real: los logs generados, incluida la captura de un error (division by zero) con su request_id.

## Probar
```
pip install fastapi uvicorn
uvicorn app:app
# probá GET /health, /productos, /romper y mirá los logs en la consola
```
