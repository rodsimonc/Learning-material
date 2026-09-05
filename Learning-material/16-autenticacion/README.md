# 16 · Autenticación y usuarios

Sistema de auth completo: registro seguro, login con tokens, roles y sesiones renovables. Amplía el login con JWT del librito 09.

## Qué hay acá
- `manual.html` — 10 capítulos: autenticar vs autorizar, contraseñas con bcrypt, registro y login, tokens JWT, proteger endpoints, roles y permisos (401 vs 403), refresh tokens, OAuth (login social) y reset de contraseña, y checklist de seguridad.
- `ejemplos/auth.py` — FastAPI: registro (bcrypt), login (access + refresh), `/perfil` protegido, `/admin` por rol, `/refresh`.
- `ejemplos/pruebas.txt` — salida real: registro, login, tokens, control de rol (403/200), refresh y verificación bcrypt.

## Probar
```
pip install fastapi uvicorn pyjwt bcrypt
uvicorn auth:app --reload
```
