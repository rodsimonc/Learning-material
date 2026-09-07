# Recursión: una función que se llama a sí misma, con un caso base que corta.
def factorial(n):
    if n <= 1:            # caso base: corta la recursión
        return 1
    return n * factorial(n - 1)   # caso recursivo: se llama con algo más chico

print("factorial(5) =", factorial(5), "  (5*4*3*2*1)")

# el clásico ejemplo con visualización
def cuenta_regresiva(n):
    if n == 0:
        print("  despegue!")
        return
    print(f"  {n}...")
    cuenta_regresiva(n - 1)
print("cuenta regresiva desde 3:")
cuenta_regresiva(3)

# recorrer una estructura anidada (donde la recursión brilla)
def sumar_todo(cosa):
    total = 0
    for x in cosa:
        if isinstance(x, list):
            total += sumar_todo(x)   # si es lista, entrar recursivamente
        else:
            total += x
    return total
anidado = [1, [2, 3, [4, 5]], 6]
print("suma de", anidado, "=", sumar_todo(anidado))
