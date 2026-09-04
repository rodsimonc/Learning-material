import hmac, hashlib, json, requests

SECRET = b"clave_secreta_compartida"
evento = {"tipo": "pago.exitoso", "monto": 2500, "moneda": "usd"}
cuerpo = json.dumps(evento).encode()
firma = hmac.new(SECRET, cuerpo, hashlib.sha256).hexdigest()

# 1) evento legitimo (firma correcta)
r = requests.post("http://127.0.0.1:8005/webhooks/pagos",
                  data=cuerpo,
                  headers={"Content-Type": "application/json", "X-Firma": firma})
print("legitimo  ->", r.status_code, r.json())

# 2) evento falso (firma incorrecta): el receiver lo rechaza
r = requests.post("http://127.0.0.1:8005/webhooks/pagos",
                  data=cuerpo,
                  headers={"Content-Type": "application/json", "X-Firma": "0000"})
print("falsificado ->", r.status_code, r.json())
