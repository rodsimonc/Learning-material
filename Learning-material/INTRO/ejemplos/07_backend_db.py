# El backend en Python: la estructura de una petición a una base de datos.
# Usamos SQLite (viene con Python, no hay que instalar nada).
import sqlite3

con = sqlite3.connect(":memory:")   # base en memoria, para el ejemplo
cur = con.cursor()

# 1. CREAR una tabla (la estructura de los datos)
cur.execute("""
CREATE TABLE productos (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    precio INTEGER,
    stock INTEGER
)""")

# 2. INSERTAR datos (siempre con ? para los valores: seguro)
cur.execute("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
            ("Pizza muzza", 8500, 5))
cur.execute("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
            ("Empanada", 1200, 40))
con.commit()

# 3. LEER (consultar) los datos
print("== todos los productos ==")
for fila in cur.execute("SELECT nombre, precio, stock FROM productos"):
    print(" ", fila)

# 4. LEER con condición
print("\n== productos de más de 5000 ==")
for fila in cur.execute("SELECT nombre, precio FROM productos WHERE precio > ?", (5000,)):
    print(" ", fila)

# 5. ACTUALIZAR (descontar stock tras una venta)
cur.execute("UPDATE productos SET stock = stock - ? WHERE nombre = ?", (2, "Pizza muzza"))
con.commit()
r = cur.execute("SELECT nombre, stock FROM productos WHERE nombre = ?", ("Pizza muzza",)).fetchone()
print("\n== stock de la pizza tras vender 2 ==")
print(" ", r)
con.close()
