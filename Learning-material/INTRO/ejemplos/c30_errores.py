# try/except: manejar errores sin que el programa se caiga
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "no se puede dividir por cero"
print(dividir(10, 2))
print(dividir(10, 0))
# validar entrada del usuario
def a_entero(texto):
    try:
        return int(texto)
    except ValueError:
        return None
print("'42' ->", a_entero("42"))
print("'hola' ->", a_entero("hola"))
# atrapar y seguir
for valor in ["10", "abc", "5"]:
    n = a_entero(valor)
    if n is None:
        print(f"  '{valor}' no es un numero, lo salteo")
    else:
        print(f"  '{valor}' x2 = {n*2}")
