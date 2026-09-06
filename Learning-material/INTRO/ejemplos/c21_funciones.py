# parametros, default, argumentos nombrados
def precio_final(precio, iva=0.21, descuento=0):
    return precio * (1 + iva) * (1 - descuento)
print("solo precio:", precio_final(1000))
print("con descuento:", precio_final(1000, descuento=0.25))
print("nombrados:", precio_final(precio=1000, iva=0.105))
# *args: cantidad variable de argumentos
def sumar(*numeros):
    return sum(numeros)
print("sumar varios:", sumar(1, 2, 3, 4, 5))
# retornar varios valores (tupla)
def analizar(precios):
    return min(precios), max(precios), sum(precios)/len(precios)
minimo, maximo, promedio = analizar([1200, 8500, 3500])
print(f"min={minimo} max={maximo} prom={promedio:.0f}")
# ambito: una variable dentro de una funcion no existe afuera
def f():
    x = 10
    return x
print("retorno:", f())
