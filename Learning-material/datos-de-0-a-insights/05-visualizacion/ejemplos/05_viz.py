import pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
df = pd.read_csv("datos/ventas_limpio.csv", parse_dates=["fecha"])
df["importe"] = df["cantidad"]*df["precio_unit"]
TEAL="#0d6b6b"; RED="#c0392b"

fig, ax = plt.subplots(1,3, figsize=(15,4))
# 1. barras: top productos
top = df.groupby("producto")["cantidad"].sum().sort_values().tail(6)
ax[0].barh(top.index, top.values, color=TEAL)
ax[0].set_title("Top productos (unidades)")

# 2. línea: facturación por día
pordia = df.groupby(df["fecha"].dt.date)["importe"].sum()
ax[1].plot(pordia.index, pordia.values, color=RED)
ax[1].set_title("Facturación por día"); ax[1].tick_params(axis="x", rotation=45)

# 3. torta: método de pago
met = df.groupby("metodo_pago")["importe"].sum()
ax[2].pie(met.values, labels=met.index, autopct="%1.0f%%", colors=[TEAL,"#ef9b50",RED])
ax[2].set_title("Ventas por método de pago")

plt.tight_layout(); plt.savefig("out/graficos.png", dpi=90)
print("gráficos guardados en out/graficos.png")
print("puntos en la serie diaria:", len(pordia))
