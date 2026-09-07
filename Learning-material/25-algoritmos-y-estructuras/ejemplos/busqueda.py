import time

def busqueda_lineal(lista, objetivo):
    for i, x in enumerate(lista):
        if x == objetivo:
            return i
    return -1

def busqueda_binaria(lista, objetivo):   # requiere lista ordenada
    lo, hi = 0, len(lista) - 1
    pasos = 0
    while lo <= hi:
        pasos += 1
        medio = (lo + hi) // 2
        if lista[medio] == objetivo:
            return medio, pasos
        elif lista[medio] < objetivo:
            lo = medio + 1
        else:
            hi = medio - 1
    return -1, pasos

datos = list(range(1_000_000))   # ya ordenados 0..999999
objetivo = 999_999               # el peor caso para lineal (el último)

t0 = time.perf_counter()
busqueda_lineal(datos, objetivo)
t_lineal = time.perf_counter() - t0

t0 = time.perf_counter()
_, pasos = busqueda_binaria(datos, objetivo)
t_binaria = time.perf_counter() - t0

print("Buscar el último de 1.000.000 de elementos:")
print(f"  lineal  (O(n)):     {t_lineal*1000:.2f} ms  (recorrió ~1.000.000)")
print(f"  binaria (O(log n)): {t_binaria*1000:.4f} ms  (solo {pasos} pasos)")
print(f"  la binaria fue ~{t_lineal/t_binaria:.0f}x más rápida")
