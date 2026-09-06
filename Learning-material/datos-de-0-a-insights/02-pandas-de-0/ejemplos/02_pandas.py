import pandas as pd
df = pd.read_csv("datos/ventas.csv")
print("== forma (filas, columnas) =="); print(df.shape)
print("\n== primeras filas =="); print(df.head(3).to_string(index=False))
print("\n== columnas y tipos =="); print(df.dtypes.to_string())
print("\n== seleccionar columnas =="); print(df[["producto","cantidad"]].head(3).to_string(index=False))
print("\n== filtrar: solo Pizzas =="); print(df[df["categoria"]=="Pizzas"].head(3)[["producto","precio_unit"]].to_string(index=False))
