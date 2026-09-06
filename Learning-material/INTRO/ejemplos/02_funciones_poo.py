# --- Funciones ---
def con_descuento(precio, porcentaje):
    return precio - (precio * porcentaje / 100)

print("1000 con 25% off:", con_descuento(1000, 25))
print("8500 con 10% off:", con_descuento(8500, 10))

def total_pedido(precio, cantidad, descuento=0):
    subtotal = precio * cantidad
    return con_descuento(subtotal, descuento)

print("3 pizzas con 15% off:", total_pedido(8500, 3, 15))

# --- Programación Orientada a Objetos ---
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def hay_stock(self, cantidad):
        return self.stock >= cantidad

    def vender(self, cantidad):
        if not self.hay_stock(cantidad):
            return f"sin stock de {self.nombre} (quedan {self.stock})"
        self.stock -= cantidad
        return f"vendidas {cantidad} de {self.nombre}, quedan {self.stock}"

# crear objetos a partir de la clase
pizza = Producto("Pizza muzza", 8500, 5)
print(pizza.nombre, "cuesta", pizza.precio, "y hay", pizza.stock)
print(pizza.vender(2))
print(pizza.vender(2))
print(pizza.vender(2))   # este se pasa del stock
