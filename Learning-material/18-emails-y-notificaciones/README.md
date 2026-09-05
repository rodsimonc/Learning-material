# 18 · Emails y notificaciones

Emails transaccionales bien hechos (que no caen en spam) y las alternativas: notificaciones in-app, push, SMS.

## Qué hay acá
- `manual.html` — 8 capítulos: transaccional vs marketing, componer (HTML + texto), enviar por SMTP, plantillas con variables, proveedores y no caer en spam (SPF/DKIM/DMARC), notificaciones más allá del email, y checklist.
- `ejemplos/emails.py` — componer y enviar por SMTP, con plantillas de confirmación de pedido y reset de contraseña. Incluye ejemplo con Resend.
- `ejemplos/pruebas.txt` — salida real: los 2 emails enviados y capturados por un servidor SMTP local.

## Probar
```
pip install aiosmtpd
# levantá un SMTP local de prueba:
python3 -m aiosmtpd -n -l localhost:8025
# en otra terminal, enviá con emails.py (SMTP_HOST=localhost SMTP_PORT=8025)
```
