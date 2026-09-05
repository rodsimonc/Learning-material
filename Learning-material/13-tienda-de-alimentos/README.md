# 13 · Tienda de alimentos, sistema completo

El librito integral de la colección. Toma un negocio real (una tienda de alimentos, "Sabores del Barrio") y construye su sistema de punta a punta: pagos con MercadoPago, QR y transferencia; sistema de reservas con control de capacidad; y un dashboard interno que controla stock, mide ventas y descubre qué se pide junto con qué y a qué hora.

Reúne todo lo de la colección: APIs (01), ciberseguridad web (07), conexión front-back (09) y base de datos SQL (10).

## Qué hay acá
- `manual.html` — 19 capítulos: arquitectura, modelo de datos, catálogo y carrito, pedidos con control de stock, los tres métodos de pago paso a paso (MercadoPago + webhook, QR real, transferencia), reservas, y el dashboard completo (top productos, facturación, combos con self-join, picos por hora, inventario), más seguridad del sistema y cómo construirlo con IA. Con QR real embebido y captura del dashboard.
- `ejemplos/backend/` — el sistema completo en Python (FastAPI + SQLite):
  - `db.py` esquema · `seed.py` datos de ejemplo (200 pedidos con horarios realistas) · `stats.py` consultas del dashboard · `pagos.py` MercadoPago/QR/transferencia · `main.py` la API.
- `ejemplos/frontend/dashboard.html` — el panel interno con datos reales y gráficos (autocontenido).
- `ejemplos/salida/` — salida real: `dashboard_pruebas.txt` (stats sobre 200 pedidos), `dashboard.png` (captura del panel), `qr_pedido_201.png` (QR de pago escaneable de verdad).

## Correrlo
```
cd ejemplos/backend
pip install fastapi uvicorn "qrcode[pil]"
python3 seed.py            # carga productos y 200 pedidos de ejemplo
uvicorn main:app --reload  # levanta la API
# el dashboard: abrí ejemplos/frontend/dashboard.html
```

Para cobrar de verdad con MercadoPago, seteá tu token: `export MP_ACCESS_TOKEN=...` (se saca gratis en tu cuenta de MP). Sin token, el flujo de MP muestra el request que se enviaría; el QR y la transferencia funcionan sin credenciales.
