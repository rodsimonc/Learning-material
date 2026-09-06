# CALCULADORA: junta funciones + condicionales + bucle
def calcular(a, operacion, b):
    if operacion == "+": return a + b
    if operacion == "-": return a - b
    if operacion == "*": return a * b
    if operacion == "/":
        if b == 0:
            return "error: no se puede dividir por cero"
        return a / b
    return "operación no válida"

# probamos con una lista de operaciones (simula lo que tipearía el usuario)
operaciones = [(10, "+", 5), (10, "-", 3), (4, "*", 6), (20, "/", 4), (5, "/", 0)]
for a, op, b in operaciones:
    print(f"{a} {op} {b} = {calcular(a, op, b)}")
