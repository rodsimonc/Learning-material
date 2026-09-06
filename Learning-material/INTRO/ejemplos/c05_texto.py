nombre = "Pizza Muzzarella"
print("largo:", len(nombre))
print("mayusculas:", nombre.upper())
print("minusculas:", nombre.lower())
print("reemplazar:", nombre.replace("Muzzarella", "Napolitana"))
print("primera letra:", nombre[0])         # indexado
print("ultimas 4:", nombre[-4:])           # slicing desde el final
print("primeras 5:", nombre[0:5])          # slicing 0 a 5
partes = "carne,pollo,jamon".split(",")   # dividir en lista
print("split:", partes)
print("unir:", " + ".join(partes))         # unir una lista en texto
sucio = "   hola   "
print("strip:", repr(sucio.strip()))       # sacar espacios de los bordes
# f-strings
precio = 8500; cant = 2
print(f"{cant} pizzas = ${precio*cant}")
print(f"con formato: ${precio*cant:,.2f}")  # separador de miles y 2 decimales
