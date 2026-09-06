# Ej 1: promedio de tres notas
notas = [7, 9, 8]
print("promedio:", sum(notas) / len(notas))
# Ej 2: ¿es par?
n = 14
print(f"{n} es par:", n % 2 == 0)
# Ej 3: el más caro de una lista
precios = [1200, 8500, 3500]
print("más caro:", max(precios))
# Ej 4: contar vocales en un texto
texto = "programar en python"
vocales = 0
for letra in texto:
    if letra in "aeiou":
        vocales += 1
print("vocales:", vocales)
# Ej 5: total de un carrito simple
carrito = [("Pizza", 8500, 2), ("Gaseosa", 1800, 3)]
total = 0
for nombre, precio, cant in carrito:
    total += precio * cant
print("total carrito:", total)
