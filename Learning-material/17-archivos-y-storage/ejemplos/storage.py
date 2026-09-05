"""
Subida y manejo de archivos con FastAPI.
- Validar tipo (solo imágenes) y tamaño (máx 2 MB)
- Guardar con un nombre único (nunca el que manda el usuario)
- Servir el archivo por su URL
Incluye, comentado, cómo sería con storage en la nube (S3 / Supabase).
"""
import uuid
from pathlib import Path
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse

app = FastAPI(title="Storage demo")

CARPETA = Path(__file__).parent / "uploads"
CARPETA.mkdir(exist_ok=True)

TIPOS_OK = {"image/jpeg": ".jpg", "image/png": ".png", "image/webp": ".webp"}
MAX_BYTES = 2 * 1024 * 1024   # 2 MB


@app.post("/subir")
async def subir(archivo: UploadFile = File(...)):
    # 1. validar el tipo declarado
    if archivo.content_type not in TIPOS_OK:
        raise HTTPException(415, f"tipo no permitido: {archivo.content_type}")

    # 2. leer y validar el tamaño
    datos = await archivo.read()
    if len(datos) > MAX_BYTES:
        raise HTTPException(413, f"archivo muy grande ({len(datos)} bytes, máx {MAX_BYTES})")

    # 3. nombre único propio (NUNCA usar el nombre que manda el usuario)
    ext = TIPOS_OK[archivo.content_type]
    nombre = f"{uuid.uuid4().hex}{ext}"
    (CARPETA / nombre).write_bytes(datos)

    return {"archivo": nombre, "bytes": len(datos),
            "url": f"/archivos/{nombre}"}


@app.get("/archivos/{nombre}")
def servir(nombre: str):
    # sanitizar: nunca dejar salir de la carpeta (evita ../../etc/passwd)
    ruta = (CARPETA / nombre).resolve()
    if not str(ruta).startswith(str(CARPETA.resolve())) or not ruta.is_file():
        raise HTTPException(404, "no existe")
    return FileResponse(ruta)


# ---------- En la nube (S3 / Supabase) ----------
# En producción no guardás en el disco del servidor (se pierde en cada deploy,
# no escala). Subís a un storage en la nube. La lógica de validar es la misma;
# solo cambia el "guardar". Ejemplo con S3 (requiere credenciales):
#
#   import boto3
#   s3 = boto3.client("s3")
#   s3.put_object(Bucket="mi-bucket", Key=nombre, Body=datos,
#                 ContentType=archivo.content_type)
#   url = f"https://mi-bucket.s3.amazonaws.com/{nombre}"
#
# Con Supabase Storage:
#   supabase.storage.from_("imagenes").upload(nombre, datos)
