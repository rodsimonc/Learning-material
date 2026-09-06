# EJEMPLO: entra un pedido de 2 unidades y hay que descontarle 25%
# Cómo lo pensamos, paso a paso:
precio_unitario = 8500     # 1. cuánto sale una unidad
cantidad = 2               # 2. cuántas unidades entran
subtotal = precio_unitario * cantidad          # 3. precio sin descuento
descuento = subtotal * 25 / 100                # 4. cuánto es el 25%
total = subtotal - descuento                   # 5. lo que se paga

print(f"precio unitario: ${precio_unitario}")
print(f"cantidad:        {cantidad}")
print(f"subtotal:        ${subtotal}   (8500 x 2)")
print(f"descuento 25%:   -${descuento:.0f}")
print(f"TOTAL A PAGAR:   ${total:.0f}")
