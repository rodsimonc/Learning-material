import pandas as pd
df = pd.read_csv("datos/ventas.csv")
print("== ANTES ==")
print("filas:", len(df))
print("nulos en precio_unit:", df["precio_unit"].isna().sum())
print("duplicados exactos:", df.duplicated().sum())
print("categorías distintas:", sorted(df["categoria"].unique()))
print("métodos distintos:", sorted(df["metodo_pago"].unique()))

# 1. sacar espacios y unificar mayúsculas
df["producto"] = df["producto"].str.strip()
df["categoria"] = df["categoria"].str.strip().str.title()
# 2. normalizar método de pago
df["metodo_pago"] = df["metodo_pago"].str.lower().str.replace(" ", "")
# 3. precio nulo: lo completamos con el precio del mismo producto
df["precio_unit"] = df.groupby("producto")["precio_unit"].transform(lambda s: s.fillna(s.median()))
# 4. sacar duplicados
df = df.drop_duplicates()
# 5. fecha a tipo fecha de verdad
df["fecha"] = pd.to_datetime(df["fecha"])

print("\n== DESPUÉS ==")
print("filas:", len(df))
print("nulos en precio_unit:", df["precio_unit"].isna().sum())
print("duplicados exactos:", df.duplicated().sum())
print("categorías distintas:", sorted(df["categoria"].unique()))
print("métodos distintos:", sorted(df["metodo_pago"].unique()))
print("tipo de 'fecha':", df["fecha"].dtype)
df.to_csv("datos/ventas_limpio.csv", index=False)
print("\nguardado datos/ventas_limpio.csv")
