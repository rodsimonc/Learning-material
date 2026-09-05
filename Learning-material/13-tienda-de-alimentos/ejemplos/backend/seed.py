"""
Carga datos realistas: catálogo de productos y ~200 pedidos repartidos
en el último mes, con horarios que imitan el consumo real (picos al mediodía
y a la noche). Sirve para que el dashboard tenga algo de qué hablar.
"""
import random
from datetime import datetime, timedelta
from db import conectar, crear_esquema

random.seed(42)  # reproducible: los mismos datos siempre

PRODUCTOS = [
    # nombre, categoria, precio, stock, stock_min
    ("Empanada de carne", "Empanadas", 1200, 300, 40),
    ("Empanada de pollo", "Empanadas", 1200, 250, 40),
    ("Empanada de jamón y queso", "Empanadas", 1200, 200, 40),
    ("Pizza muzzarella", "Pizzas", 8500, 60, 10),
    ("Pizza napolitana", "Pizzas", 9800, 45, 10),
    ("Milanesa con papas", "Platos", 9500, 40, 8),
    ("Ensalada César", "Platos", 7200, 30, 8),
    ("Gaseosa 500ml", "Bebidas", 1800, 120, 20),
    ("Agua mineral", "Bebidas", 1400, 100, 20),
    ("Cerveza artesanal", "Bebidas", 3200, 50, 10),
    ("Flan casero", "Postres", 3500, 40, 8),
    ("Helado 1/4", "Postres", 4200, 25, 6),
]

CLIENTES = ["Carlos", "Ana", "Luis", "Sofía", "Diego", "Marta", "Juan",
            "Lucía", "Pablo", "Vale", "Nico", "Cami"]

# combinaciones que la gente pide junta (para que aparezcan combos reales)
COMBOS_TIPICOS = [
    [1, 1, 1, 8],       # empanadas de carne + gaseosa
    [4, 8],             # pizza muzza + gaseosa
    [4, 10],            # pizza muzza + cerveza
    [6, 8],             # milanesa + gaseosa
    [5, 10, 11],        # napolitana + cerveza + flan
    [1, 2, 3, 8],       # docena mixta + gaseosa
    [7, 9],             # ensalada + agua
    [6, 11],            # milanesa + flan
]


def hora_realista(dia):
    """Elige una hora imitando picos de almuerzo (12-14) y cena (20-22)."""
    franja = random.choices(["almuerzo", "cena", "otro"], weights=[38, 45, 17])[0]
    if franja == "almuerzo":
        h = random.choices([12, 13, 14], weights=[3, 4, 2])[0]
    elif franja == "cena":
        h = random.choices([20, 21, 22], weights=[3, 4, 2])[0]
    else:
        h = random.choice([11, 15, 16, 17, 18, 19, 23])
    return dia.replace(hour=h, minute=random.randint(0, 59), second=0, microsecond=0)


def cargar():
    crear_esquema()
    con = conectar()
    cur = con.cursor()
    # limpiar para poder correr varias veces
    for t in ("pagos", "pedido_items", "pedidos", "reservas", "productos"):
        cur.execute(f"DELETE FROM {t}")

    for p in PRODUCTOS:
        cur.execute("INSERT INTO productos (nombre,categoria,precio,stock,stock_min)"
                    " VALUES (?,?,?,?,?)", p)

    precios = {r["id"]: r["precio"] for r in cur.execute("SELECT id,precio FROM productos")}

    hoy = datetime(2026, 9, 5, 12, 0, 0)
    for _ in range(200):
        dia = hoy - timedelta(days=random.randint(0, 29))
        cuando = hora_realista(dia)
        combo = random.choice(COMBOS_TIPICOS)[:]
        # a veces suman un postre suelto
        if random.random() < 0.25:
            combo.append(random.choice([11, 12]))

        cur.execute("INSERT INTO pedidos (cliente,creado_en,estado,total)"
                    " VALUES (?,?,?,0)",
                    (random.choice(CLIENTES), cuando.isoformat(), "pagado"))
        pid = cur.lastrowid
        total = 0
        # agrupar cantidades por producto
        conteo = {}
        for prod in combo:
            conteo[prod] = conteo.get(prod, 0) + 1
        for prod, cant in conteo.items():
            pu = precios[prod]
            cur.execute("INSERT INTO pedido_items (pedido_id,producto_id,cantidad,precio_unit)"
                        " VALUES (?,?,?,?)", (pid, prod, cant, pu))
            total += pu * cant
        cur.execute("UPDATE pedidos SET total=? WHERE id=?", (total, pid))

    # unas reservas
    for _ in range(15):
        d = (hoy + timedelta(days=random.randint(1, 14))).date()
        cur.execute("INSERT INTO reservas (cliente,fecha,hora,personas)"
                    " VALUES (?,?,?,?)",
                    (random.choice(CLIENTES), d.isoformat(),
                     random.choice(["20:00", "20:30", "21:00", "21:30"]),
                     random.randint(2, 6)))

    con.commit()
    n = cur.execute("SELECT COUNT(*) c FROM pedidos").fetchone()["c"]
    con.close()
    print(f"cargados: {len(PRODUCTOS)} productos, {n} pedidos, 15 reservas")


if __name__ == "__main__":
    cargar()
