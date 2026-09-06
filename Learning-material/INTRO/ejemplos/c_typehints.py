# Anotaciones de tipo: documentan qué recibe y devuelve cada función.
def total_pedido(precio: float, cantidad: int, descuento: float = 0.0) -> float:
    subtotal = precio * cantidad
    return subtotal * (1 - descuento)

# tipos en variables y estructuras
nombre: str = "Pizza"
precios: list[int] = [1200, 8500]
menu: dict[str, int] = {"pizza": 8500}

print(total_pedido(8500, 2, 0.25))
print("las anotaciones no cambian el resultado, guían y documentan")
