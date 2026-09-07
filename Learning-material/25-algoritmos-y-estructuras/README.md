# 25 · Algoritmos y estructuras de datos

Los cimientos de la eficiencia: Big-O, los algoritmos clásicos, y la decisión que más impacta en el rendimiento (elegir la estructura correcta). Para entender y elegir bien, no para reinventar. Lo más pedido en entrevistas técnicas.

## Qué hay acá
- `manual.html` — 9 capítulos: qué es un algoritmo, Big-O, búsqueda (lineal vs binaria), ordenamiento (bubble vs sorted), elegir la estructura (list vs dict/set), stacks y queues, recursión, y cierre.
- `ejemplos/` — scripts que MIDEN la diferencia de verdad: `busqueda.py`, `estructuras.py`, `ordenar.py`, `recursion.py`.
- `ejemplos/salidas.txt` — las salidas reales con los tiempos medidos (búsqueda binaria ~1925x más rápida, set ~6268x más rápido que lista, sorted ~423x más rápido que bubble).

## Probar
```
python3 ejemplos/busqueda.py
python3 ejemplos/estructuras.py
```
Solo Python puro. Los tiempos exactos varían según la máquina, pero las proporciones se mantienen.
