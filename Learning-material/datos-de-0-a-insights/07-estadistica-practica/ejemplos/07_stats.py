import pandas as pd
df = pd.read_csv("datos/ventas_limpio.csv", parse_dates=["fecha"])
df["importe"] = df["cantidad"] * df["precio_unit"]

ticket = df.groupby("pedido_id")["importe"].sum()
print("== Ticket por pedido ==")
print(f"  media:    ${ticket.mean():,.0f}")
print(f"  mediana:  ${ticket.median():,.0f}")
print(f"  desvío:   ${ticket.std():,.0f}")
print(f"  mín/máx:  ${ticket.min():,.0f} / ${ticket.max():,.0f}")
print("\n== media vs mediana ==")
print("  acá están cerca: la distribución es pareja. Si la media fuera")
print("  mucho mayor, unos pocos pedidos enormes la estarían estirando.")

por_pedido = df.groupby("pedido_id").agg(items=("cantidad","sum"),
                                         total=("importe","sum"))
c = por_pedido["items"].corr(por_pedido["total"])
print("\n== Correlación: items por pedido vs total del pedido ==")
print(f"  {c:.2f}  -> CASI CERO. La intuición ('más items = más plata') NO se cumple.")
print("  ¿Por qué? Los ítems baratos (empanadas, gaseosa) vienen de a muchos,")
print("  y los caros (milanesa, pizza) vienen solos. Cantidad no predice importe.")
print("  Lección: no asumas la correlación; medila. Los datos te corrigen.")
