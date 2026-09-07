import time

# list vs set/dict para "¿está esto acá?"
N = 100_000
lista = list(range(N))
conjunto = set(range(N))
buscar = N - 1     # el peor caso para la lista

t0 = time.perf_counter()
for _ in range(1000):
    _ = buscar in lista       # O(n): recorre toda la lista
t_lista = time.perf_counter() - t0

t0 = time.perf_counter()
for _ in range(1000):
    _ = buscar in conjunto    # O(1): acceso directo
t_set = time.perf_counter() - t0

print("'¿está x?' 1000 veces sobre 100.000 elementos:")
print(f"  en lista (O(n)): {t_lista*1000:.1f} ms")
print(f"  en set   (O(1)): {t_set*1000:.3f} ms")
print(f"  el set fue ~{t_lista/t_set:.0f}x más rápido")

# stack y queue con list y deque
from collections import deque
pila = []                      # stack (LIFO): el último en entrar, primero en salir
pila.append("a"); pila.append("b"); pila.append("c")
print("\nstack:", pila)
ultimo = pila.pop()
print("  pop() saca el ULTIMO:", ultimo, "-> queda", pila)

cola = deque()                 # queue (FIFO): el primero en entrar, primero en salir
cola.append("a"); cola.append("b"); cola.append("c")
print("queue:", list(cola))
primero = cola.popleft()
print("  popleft() saca el PRIMERO:", primero, "-> queda", list(cola))
