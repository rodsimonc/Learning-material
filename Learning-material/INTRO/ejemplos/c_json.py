import json
pedido = {"cliente": "Carlos", "items": [{"producto": "Pizza", "cant": 2}], "total": 17000}
# de objeto Python a texto JSON
texto = json.dumps(pedido, ensure_ascii=False, indent=2)
print("== JSON (texto) ==")
print(texto)
# de texto JSON de vuelta a objeto Python
recuperado = json.loads(texto)
print("\ncliente:", recuperado["cliente"])
print("primer item:", recuperado["items"][0]["producto"])
