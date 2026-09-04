import hmac, hashlib
from fastapi import FastAPI, Request, HTTPException

SECRET = b"clave_secreta_compartida"
app = FastAPI()

def firma_valida(cuerpo: bytes, firma: str) -> bool:
    esperada = hmac.new(SECRET, cuerpo, hashlib.sha256).hexdigest()
    return hmac.compare_digest(esperada, firma)

@app.post("/webhooks/pagos")
async def recibir(request: Request):
    cuerpo = await request.body()
    firma = request.headers.get("X-Firma", "")
    if not firma_valida(cuerpo, firma):        # regla 1: verificar la firma
        raise HTTPException(400, "firma invalida")
    evento = await request.json()
    print(f"[receiver] evento OK: {evento['tipo']} monto={evento['monto']}")
    return {"recibido": True}                   # regla 2: responder rapido 200
