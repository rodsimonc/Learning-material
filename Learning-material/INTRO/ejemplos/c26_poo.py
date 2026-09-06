class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    def vender(self, cantidad):
        if cantidad > self.stock:
            raise ValueError(f"sin stock de {self.nombre} (quedan {self.stock})")
        self.stock -= cantidad
        return self.precio * cantidad

class Carrito:
    def __init__(self):
        self.items = []       # lista de (producto, cantidad)
        self.total = 0
    def agregar(self, producto, cantidad):
        importe = producto.vender(cantidad)   # un objeto usa a otro
        self.items.append((producto.nombre, cantidad, importe))
        self.total += importe
    def resumen(self):
        for nombre, cant, imp in self.items:
            print(f"  {cant}x {nombre} = ${imp}")
        print(f"  TOTAL: ${self.total}")

pizza = Producto("Pizza", 8500, 5)
gaseosa = Producto("Gaseosa", 1800, 10)
carrito = Carrito()
carrito.agregar(pizza, 2)
carrito.agregar(gaseosa, 3)
carrito.resumen()
print("stock pizza tras la venta:", pizza.stock)

# Herencia: un ProductoConDescuento ES un Producto, con algo extra
class ProductoConDescuento(Producto):
    def __init__(self, nombre, precio, stock, descuento):
        super().__init__(nombre, precio, stock)   # reusa el init del padre
        self.descuento = descuento
    def vender(self, cantidad):                     # cambia el comportamiento
        base = super().vender(cantidad)
        return base * (1 - self.descuento)

flan = ProductoConDescuento("Flan", 3500, 8, 0.20)
print("flan con 20% off, 2 unidades:", flan.vender(2))
