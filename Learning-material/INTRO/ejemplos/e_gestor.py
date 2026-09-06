# PROYECTO: mini gestor de stock (junta listas, dicts, funciones, if, for)
inventario = [
    {"nombre": "Pizza", "precio": 8500, "stock": 5},
    {"nombre": "Empanada", "precio": 1200, "stock": 40},
    {"nombre": "Flan", "precio": 3500, "stock": 3},
]

def buscar(nombre):
    for prod in inventario:
        if prod["nombre"] == nombre:
            return prod
    return None

def vender(nombre, cantidad):
    prod = buscar(nombre)
    if prod is None:
        return f"no existe {nombre}"
    if prod["stock"] < cantidad:
        return f"sin stock de {nombre} (quedan {prod['stock']})"
    prod["stock"] -= cantidad
    return f"vendidas {cantidad} de {nombre}. Total: ${prod['precio']*cantidad}. Quedan {prod['stock']}"

def reponer():
    return [p["nombre"] for p in inventario if p["stock"] <= 5]

print(vender("Pizza", 2))
print(vender("Pizza", 10))
print(vender("Empanada", 12))
print(vender("Sushi", 1))
print("hay que reponer:", reponer())
print("\ninventario final:")
for p in inventario:
    print(f"  {p['nombre']}: {p['stock']} en stock")
