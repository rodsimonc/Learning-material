# 07 · Ciberseguridad web

Las fallas más comunes y cómo taparlas, con código vulnerable al lado del seguro.

## Qué hay acá
- `manual.html` — 12 capítulos: fundamentos, las clásicas (SQLi, XSS, CSRF, auth, control de acceso), endurecer (secretos, headers, dependencias), y un checklist.
- `ejemplos/sqli.py` — demuestra una inyección SQL funcionando (devuelve toda la tabla) vs la versión parametrizada que la frena.
- `ejemplos/hash.py` — hashing de contraseñas con bcrypt y sal.
- `ejemplos/salidas/` — la salida real de ambos.

Todo es para asegurar tus propias apps. Correr estas técnicas contra sistemas ajenos sin permiso es ilegal.
