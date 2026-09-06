# escribir un archivo
with open("pedidos.txt", "w") as f:
    f.write("Pizza,2\n")
    f.write("Gaseosa,3\n")
# leerlo
print("== contenido ==")
with open("pedidos.txt") as f:
    for linea in f:
        producto, cantidad = linea.strip().split(",")
        print(f"  {cantidad} x {producto}")
# modulos de la libreria estandar
import datetime, random, math
print("hoy:", datetime.date.today())
print("random 1-6:", random.randint(1, 6))
print("raiz de 144:", math.sqrt(144))
