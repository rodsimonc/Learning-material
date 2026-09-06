stock = 5; pedido = 3; pagado = True
print("hay stock:", pedido <= stock)
print("and:", pedido <= stock and pagado)      # las dos verdaderas
print("or:", pedido > stock or pagado)         # al menos una
print("not:", not pagado)                       # invierte
# comparaciones encadenadas
edad = 25
print("entre 18 y 65:", 18 <= edad <= 65)
# valores "falsy": 0, "", [], None son falsos
print("lista vacia es falsa:", bool([]))
print("cero es falso:", bool(0))
print("texto con algo es verdadero:", bool("hola"))
