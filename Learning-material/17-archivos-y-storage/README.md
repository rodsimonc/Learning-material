# 17 · Archivos y storage

Subida de archivos completa y segura: validar tipo y tamaño, guardar con nombre propio, servir sin fugas, y llevar todo a un storage en la nube.

## Qué hay acá
- `manual.html` — 7 capítulos: cómo viaja un archivo (multipart), recibir y validar (tipo/tamaño), guardar con nombre UUID, servir sin path traversal, storage en la nube (S3/Supabase, subida directa, URLs firmadas), y checklist.
- `ejemplos/storage.py` — FastAPI: `/subir` (valida y guarda), `/archivos/{n}` (sirve con protección de path traversal). Incluye el código S3/Supabase comentado.
- `ejemplos/pruebas.txt` — salida real: subir OK, rechazo de tipo, rechazo de tamaño, y path traversal bloqueado.

## Probar
```
pip install fastapi uvicorn python-multipart pillow
uvicorn storage:app --reload
```
