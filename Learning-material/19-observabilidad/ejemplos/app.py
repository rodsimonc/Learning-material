"""
Observabilidad en una API: saber qué pasa cuando algo se rompe.
- Logs estructurados (JSON): fáciles de buscar y filtrar
- Request id: seguir un pedido a través de todos sus logs
- Manejo central de errores: nada se pierde en silencio
- Healthcheck: para que el hosting sepa si la app está viva
"""
import json
import logging
import time
import uuid
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse


# ---------- Logs estructurados (JSON) ----------
class JsonFormatter(logging.Formatter):
    def format(self, record):
        log = {
            "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "nivel": record.levelname,
            "mensaje": record.getMessage(),
        }
        if hasattr(record, "extra"):
            log.update(record.extra)
        return json.dumps(log, ensure_ascii=False)


log = logging.getLogger("app")
log.setLevel(logging.INFO)
_h = logging.StreamHandler()
_h.setFormatter(JsonFormatter())
log.addHandler(_h)


def logear(nivel, mensaje, **campos):
    log.log(nivel, mensaje, extra={"extra": campos})


app = FastAPI(title="Observabilidad demo")


# ---------- Middleware: request id + tiempo de respuesta ----------
@app.middleware("http")
async def observar(request: Request, call_next):
    rid = str(uuid.uuid4())[:8]
    inicio = time.time()
    try:
        respuesta = await call_next(request)
    except Exception as e:
        ms = round((time.time() - inicio) * 1000)
        logear(logging.ERROR, "excepción no manejada",
               request_id=rid, ruta=request.url.path, error=str(e), ms=ms)
        return JSONResponse(status_code=500,
                            content={"detail": "error interno", "request_id": rid})
    ms = round((time.time() - inicio) * 1000)
    logear(logging.INFO, "request",
           request_id=rid, metodo=request.method, ruta=request.url.path,
           status=respuesta.status_code, ms=ms)
    respuesta.headers["X-Request-ID"] = rid
    return respuesta


# ---------- Healthcheck ----------
@app.get("/health")
def health():
    # el hosting llama a esto para saber si la app está viva (librito 20)
    return {"estado": "ok"}


# ---------- Endpoints de ejemplo ----------
@app.get("/productos")
def productos():
    logear(logging.INFO, "consulta de catálogo", cantidad=3)
    return [{"id": 1, "nombre": "Pizza"}]


@app.get("/romper")
def romper():
    # simula un bug para ver cómo se captura
    return 1 / 0
