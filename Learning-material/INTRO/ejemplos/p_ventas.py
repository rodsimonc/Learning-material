# Simula leer ventas de un archivo y sacar conclusiones
ventas_texto = """Pizza,8500,2
Empanada,1200,12
Pizza,8500,1
Gaseosa,1800,5
Flan,3500,3
Empanada,1200,6"""

ventas = []
for linea in ventas_texto.strip().split("\n"):
    nombre, precio, cant = linea.split(",")
    ventas.append({"producto": nombre, "precio": int(precio), "cantidad": int(cant)})

# total facturado
total = sum(v["precio"] * v["cantidad"] for v in ventas)
print(f"total facturado: ${total:,}")

# unidades por producto (acumular en un diccionario)
por_producto = {}
for v in ventas:
    por_producto[v["producto"]] = por_producto.get(v["producto"], 0) + v["cantidad"]
print("unidades por producto:", por_producto)

# el mas vendido
mas_vendido = max(por_producto, key=por_producto.get)
print("mas vendido:", mas_vendido, "con", por_producto[mas_vendido], "unidades")
