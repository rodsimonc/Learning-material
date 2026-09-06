import random
random.seed(3)                       # fijo para que la prueba sea reproducible
secreto = random.randint(1, 100)     # con esta semilla, sale 31
# simulamos una busqueda inteligente (el jugador va acotando)
intentos_simulados = [50, 25, 37, 31]
print(f"(numero secreto: {secreto}, oculto para el jugador)")
intentos = 0
for intento in intentos_simulados:
    intentos += 1
    if intento == secreto:
        print(f"intento {intentos}: {intento} -> ACERTASTE en {intentos} intentos!")
        break
    elif intento < secreto:
        print(f"intento {intentos}: {intento} -> muy bajo, probá mas alto")
    else:
        print(f"intento {intentos}: {intento} -> muy alto, probá mas bajo")
