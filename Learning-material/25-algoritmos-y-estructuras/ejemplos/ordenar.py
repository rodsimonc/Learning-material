import time, random

def bubble_sort(lista):        # O(n^2): lento, solo didáctico
    a = lista[:]
    n = len(a)
    for i in range(n):
        for j in range(n - 1 - i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

datos = [random.randint(0, 1000) for _ in range(2000)]

t0 = time.perf_counter(); bubble_sort(datos); t_bubble = time.perf_counter() - t0
t0 = time.perf_counter(); sorted(datos);     t_python = time.perf_counter() - t0

print("Ordenar 2000 números:")
print(f"  bubble sort O(n^2), a mano: {t_bubble*1000:.1f} ms")
print(f"  sorted() de Python O(n log n): {t_python*1000:.3f} ms")
print(f"  sorted() fue ~{t_bubble/t_python:.0f}x más rápido")
print("Lección: casi nunca escribas tu propio ordenamiento; usá sorted().")
