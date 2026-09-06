# Descuento por cantidad: 0% hasta 2, 10% de 3-5, 20% de 6+
def descuento_por_cantidad(cantidad):
    if cantidad >= 6: return 0.20
    if cantidad >= 3: return 0.10
    return 0.0
def total(precio, cantidad):
    subtotal = precio * cantidad
    desc = descuento_por_cantidad(cantidad)
    return subtotal * (1 - desc), desc
for c in [1, 4, 8]:
    t, d = total(1200, c)
    print(f"{c} empanadas: ${t:.0f}  (descuento {int(d*100)}%)")
