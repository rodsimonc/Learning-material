# EJEMPLO: entran dos pedidos. El segundo no tiene stock suficiente.
stock = 3                       # solo quedan 3 unidades
precio_unitario = 8500

pedidos = [2, 2]                # pedido 1 pide 2, pedido 2 pide 2

for numero, cantidad in enumerate(pedidos, start=1):
    print(f"\n--- Pedido {numero}: {cantidad} unidades (stock actual: {stock}) ---")
    if cantidad <= stock:                       # ¿alcanza el stock?
        subtotal = precio_unitario * cantidad
        total = subtotal - subtotal * 25 / 100  # con 25% off
        stock = stock - cantidad                # descontamos del stock
        print(f"  OK. Total con 25% off: ${total:.0f}")
        print(f"  stock restante: {stock}")
    else:
        faltan = cantidad - stock
        print(f"  RECHAZADO: sin stock suficiente.")
        print(f"  pedían {cantidad}, quedan {stock}, faltan {faltan}")
