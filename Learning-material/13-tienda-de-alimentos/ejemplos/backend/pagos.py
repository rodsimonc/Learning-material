"""
Los tres métodos de pago de la tienda.

1. MercadoPago (Checkout Pro): se crea una "preferencia" con los items y MP
   devuelve un link de pago. El cobro lo maneja MP en su entorno seguro; vos
   nunca tocás datos de tarjeta. MP te avisa el resultado por un webhook.
   Requiere tu ACCESS_TOKEN de MercadoPago (se saca en la cuenta de MP).

2. QR de transferencia: generás un QR real que abre la transferencia con tu
   alias y el monto. No necesita credenciales de nadie: es un QR estándar.

3. Transferencia manual: mostrás CBU/alias, el cliente transfiere, y en el
   dashboard confirmás el pago. Simple y sin comisiones.
"""
import os
import io
import json
import urllib.request
from datetime import datetime
import qrcode

ALIAS_TIENDA = "sabores.del.barrio.mp"
MP_ACCESS_TOKEN = os.getenv("MP_ACCESS_TOKEN", "")  # tu token de MercadoPago


# ---------- 1. MercadoPago ----------
def crear_preferencia_mp(items, pedido_id):
    """
    Crea una preferencia de pago en MercadoPago y devuelve el link de pago.
    items: [{"title": "...", "quantity": n, "unit_price": precio}, ...]
    Necesita MP_ACCESS_TOKEN. Sin token, devuelve la estructura que se enviaría
    (para poder mostrar el flujo sin credenciales).
    """
    cuerpo = {
        "items": items,
        "external_reference": str(pedido_id),
        "back_urls": {
            "success": "https://tutienda.com/pago/ok",
            "failure": "https://tutienda.com/pago/error",
        },
        "notification_url": "https://tutienda.com/api/webhook/mp",
    }
    if not MP_ACCESS_TOKEN:
        return {"_sin_credencial": True, "request_body": cuerpo}

    req = urllib.request.Request(
        "https://api.mercadopago.com/checkout/preferences",
        data=json.dumps(cuerpo).encode(),
        headers={"Authorization": f"Bearer {MP_ACCESS_TOKEN}",
                 "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req) as r:
        data = json.load(r)
    # init_point es el link al que se manda al cliente a pagar
    return {"pref_id": data["id"], "init_point": data["init_point"]}


def procesar_webhook_mp(cuerpo):
    """
    MP llama a tu notification_url cuando cambia un pago. Acá consultás el
    pago por su id y actualizás el pedido. Devuelve (pedido_id, estado).
    """
    pago_id = cuerpo.get("data", {}).get("id")
    if not MP_ACCESS_TOKEN or not pago_id:
        return None, "sin_datos"
    req = urllib.request.Request(
        f"https://api.mercadopago.com/v1/payments/{pago_id}",
        headers={"Authorization": f"Bearer {MP_ACCESS_TOKEN}"})
    with urllib.request.urlopen(req) as r:
        pago = json.load(r)
    return pago.get("external_reference"), pago.get("status")  # 'approved', etc.


# ---------- 2. QR de transferencia ----------
def generar_qr_pago(monto, pedido_id, ruta_png):
    """
    Genera un QR real que codifica los datos de pago (alias + monto + pedido).
    Al escanearlo, la app del banco o MP abre la transferencia precargada.
    Devuelve el texto que quedó dentro del QR.
    """
    contenido = (f"PAGO|alias={ALIAS_TIENDA}|monto={monto:.2f}"
                 f"|ref=PEDIDO-{pedido_id}")
    img = qrcode.make(contenido)
    img.save(ruta_png)
    return contenido


# ---------- 3. Transferencia manual ----------
def datos_transferencia(monto, pedido_id):
    """Lo que se le muestra al cliente para que transfiera."""
    return {
        "alias": ALIAS_TIENDA,
        "monto": monto,
        "referencia": f"PEDIDO-{pedido_id}",
        "instruccion": "Transferí e informá el comprobante. "
                       "Confirmamos el pago desde el panel.",
    }


def registrar_pago(con, pedido_id, metodo, estado, referencia=None):
    """Guarda un pago y, si quedó aprobado, marca el pedido como pagado."""
    con.execute("INSERT INTO pagos (pedido_id,metodo,estado,referencia,creado_en)"
                " VALUES (?,?,?,?,?)",
                (pedido_id, metodo, estado, referencia, datetime.now().isoformat()))
    if estado == "aprobado":
        con.execute("UPDATE pedidos SET estado='pagado' WHERE id=?", (pedido_id,))
    con.commit()
