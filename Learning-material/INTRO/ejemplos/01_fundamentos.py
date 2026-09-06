# --- Variables y operaciones ---
precio = 1200
cantidad = 3
total = precio * cantidad
print("total:", total)
print("con IVA (21%):", total * 1.21)
print("mitad:", total / 2)
print("resto de 10/3:", 10 % 3)

# --- Condicionales ---
stock = 5
pedido = 8
if pedido <= stock:
    print("hay stock")
elif pedido - stock <= 3:
    print("falta poco, reponer")
else:
    print("sin stock suficiente")

# --- Bucle while ---
print("cuenta regresiva:")
n = 3
while n > 0:
    print(" ", n)
    n = n - 1

# --- Bucle for ---
print("tabla del 5:")
for i in range(1, 4):
    print(f"  5 x {i} = {5*i}")

# --- Listas ---
productos = ["empanada", "pizza", "flan"]
productos.append("gaseosa")
print("productos:", productos)
print("primero:", productos[0], "| total:", len(productos))
for p in productos:
    print("  -", p)

# --- Diccionarios ---
pedido = {"producto": "pizza", "cantidad": 2, "precio": 8500}
print("el pedido es de", pedido["cantidad"], pedido["producto"])
pedido["pagado"] = True
print(pedido)
