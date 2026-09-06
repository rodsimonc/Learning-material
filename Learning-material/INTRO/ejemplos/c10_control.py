# for con range en sus 3 formas
for i in range(3): print("range(3):", i)
for i in range(2, 5): print("range(2,5):", i)
for i in range(0, 10, 2): print("range(0,10,2):", i)
# enumerate
for pos, prod in enumerate(["pizza","flan"], start=1):
    print(f"{pos}. {prod}")
# acumulador
total = 0
for precio in [1200, 8500, 3500]:
    total += precio
print("total acumulado:", total)
# contar con condicion
caros = 0
for p in [1200, 8500, 3500, 9800]:
    if p > 5000: caros += 1
print("productos caros:", caros)
# break y continue
for n in range(1, 10):
    if n == 5: break          # corta el bucle
    if n % 2 == 0: continue   # saltea los pares
    print("impar antes del 5:", n)
