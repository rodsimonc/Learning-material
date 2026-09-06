import pandas as pd, sqlite3
df = pd.read_csv("datos/ventas_limpio.csv")
con = sqlite3.connect(":memory:")
df.to_sql("ventas", con, index=False)

print("== Ranking de productos por facturación (window function) ==")
q = """
SELECT producto,
       SUM(cantidad*precio_unit) AS facturado,
       RANK() OVER (ORDER BY SUM(cantidad*precio_unit) DESC) AS puesto
FROM ventas GROUP BY producto LIMIT 5
"""
for r in con.execute(q):
    print(f"  #{r[2]}  ${r[1]:>10,.0f}  {r[0]}")

print("\n== Participación de cada categoría con CTE ==")
q2 = """
WITH tot AS (SELECT SUM(cantidad*precio_unit) t FROM ventas)
SELECT categoria,
       ROUND(SUM(cantidad*precio_unit)*100.0/(SELECT t FROM tot),1) AS pct
FROM ventas GROUP BY categoria ORDER BY pct DESC
"""
for r in con.execute(q2): print(f"  {r[1]:>5}%  {r[0]}")
