precio = 1200            # int
descuento = 0.25         # float
nombre = "Pizza"         # str
disponible = True        # bool
print(type(precio), type(descuento), type(nombre), type(disponible))

# reasignar
precio = 1500
print("nuevo precio:", precio)

# conversiones de tipo
cantidad_texto = "3"                 # esto es texto, no numero
cantidad = int(cantidad_texto)       # convertir a entero
print("doble:", cantidad * 2)        # ahora se puede multiplicar
print("como texto:", str(precio) + " pesos")   # numero a texto para concatenar
print("a decimal:", float("2.5") + 1)
