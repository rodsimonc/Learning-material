precios = [1200, 8500, 3500, 9800, 1800]
# list comprehension: transformar
con_iva = [p * 1.21 for p in precios]
print("con IVA:", [round(x) for x in con_iva])
# filtrar
caros = [p for p in precios if p > 5000]
print("caros:", caros)
# transformar + filtrar juntos
nombres = ["pizza", "flan", "gaseosa"]
en_may = [n.upper() for n in nombres if len(n) > 4]
print("largos en mayus:", en_may)
# dict comprehension
menu = {n: p for n, p in zip(nombres, [8500, 3500, 1800])}
print("menu:", menu)
# zip: recorrer dos listas a la vez
for nombre, precio in zip(nombres, [8500, 3500, 1800]):
    print(f"  {nombre}: ${precio}")
