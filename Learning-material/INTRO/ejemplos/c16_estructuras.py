# tuplas: como listas pero no se modifican
punto = (10, 20)
print("tupla:", punto, "x =", punto[0])
# sets: sin duplicados
tags = {"oferta", "nuevo", "oferta"}
print("set sin duplicados:", tags)
print("esta 'nuevo'?:", "nuevo" in tags)
# lista de diccionarios: LA estructura de los datos de una app
menu = [
    {"nombre": "Pizza", "precio": 8500},
    {"nombre": "Flan", "precio": 3500},
    {"nombre": "Gaseosa", "precio": 1800},
]
for item in menu:
    print(f"  {item['nombre']}: ${item['precio']}")
total = sum(item["precio"] for item in menu)
print("total del menu:", total)
# el mas caro
mas_caro = max(menu, key=lambda x: x["precio"])
print("mas caro:", mas_caro["nombre"])
