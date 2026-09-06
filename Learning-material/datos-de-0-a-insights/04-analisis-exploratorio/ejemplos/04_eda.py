import pandas as pd
df = pd.read_csv("datos/ventas_limpio.csv", parse_dates=["fecha"])
df["importe"] = df["cantidad"] * df["precio_unit"]

print("== Top productos por unidades ==")
top = df.groupby("producto")["cantidad"].sum().sort_values(ascending=False).head(5)
print(top.to_string())

print("\n== Facturación por categoría ==")
cat = df.groupby("categoria")["importe"].sum().sort_values(ascending=False)
print(cat.map(lambda x: f"${x:,.0f}").to_string())

print("\n== Ventas por método de pago (participación) ==")
met = df.groupby("metodo_pago")["importe"].sum()
print((met/met.sum()*100).round(1).map(lambda x: f"{x}%").to_string())

print("\n== Pedidos por hora (pico) ==")
df["hora"] = df["fecha"].dt.hour
porhora = df.drop_duplicates("pedido_id").groupby("hora").size()
print(porhora.sort_values(ascending=False).head(4).to_string())

print("\n== Tabla dinámica: importe por categoría y método ==")
piv = pd.pivot_table(df, values="importe", index="categoria", columns="metodo_pago", aggfunc="sum", fill_value=0)
print(piv.map(lambda x: f"{x/1000:.0f}k").to_string())
