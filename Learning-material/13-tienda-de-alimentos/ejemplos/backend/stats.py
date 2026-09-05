"""
El cerebro del dashboard interno. Cada función es una consulta SQL sobre
los pedidos reales. Esto es lo que le da valor al negocio: saber qué se
vende, cuándo, con qué, y qué falta reponer.
"""
from db import conectar


def top_productos(limite=5):
    """Los productos más vendidos por unidades."""
    con = conectar()
    filas = con.execute("""
        SELECT p.nombre, SUM(i.cantidad) AS unidades,
               SUM(i.cantidad * i.precio_unit) AS facturado
        FROM pedido_items i
        JOIN productos p ON p.id = i.producto_id
        GROUP BY p.id
        ORDER BY unidades DESC
        LIMIT ?
    """, (limite,)).fetchall()
    con.close()
    return [dict(f) for f in filas]


def combos_frecuentes(limite=5):
    """
    Qué se pide junto con qué. Self-join de los items de un mismo pedido:
    cada par de productos distintos que aparecieron en el mismo pedido,
    contado en cuántos pedidos apareció ese par.
    """
    con = conectar()
    filas = con.execute("""
        SELECT a.nombre AS producto_a, b.nombre AS producto_b,
               COUNT(*) AS veces
        FROM pedido_items ia
        JOIN pedido_items ib
          ON ia.pedido_id = ib.pedido_id AND ia.producto_id < ib.producto_id
        JOIN productos a ON a.id = ia.producto_id
        JOIN productos b ON b.id = ib.producto_id
        GROUP BY ia.producto_id, ib.producto_id
        ORDER BY veces DESC
        LIMIT ?
    """, (limite,)).fetchall()
    con.close()
    return [dict(f) for f in filas]


def pedidos_por_hora():
    """Cuántos pedidos entran en cada hora del día. El mapa de los picos."""
    con = conectar()
    filas = con.execute("""
        SELECT CAST(strftime('%H', creado_en) AS INTEGER) AS hora,
               COUNT(*) AS pedidos
        FROM pedidos
        GROUP BY hora
        ORDER BY hora
    """).fetchall()
    con.close()
    return [dict(f) for f in filas]


def facturacion_por_dia():
    """Facturación diaria del último período."""
    con = conectar()
    filas = con.execute("""
        SELECT DATE(creado_en) AS dia, SUM(total) AS facturado,
               COUNT(*) AS pedidos
        FROM pedidos
        GROUP BY dia
        ORDER BY dia
    """).fetchall()
    con.close()
    return [dict(f) for f in filas]


def stock_bajo():
    """Productos que llegaron o bajaron del mínimo: hay que reponer."""
    con = conectar()
    filas = con.execute("""
        SELECT nombre, stock, stock_min
        FROM productos
        WHERE stock <= stock_min
        ORDER BY stock ASC
    """).fetchall()
    con.close()
    return [dict(f) for f in filas]


def resumen():
    """Los números grandes de arriba del dashboard."""
    con = conectar()
    r = con.execute("""
        SELECT COUNT(*) AS pedidos,
               COALESCE(SUM(total),0) AS facturado,
               COALESCE(AVG(total),0) AS ticket_promedio
        FROM pedidos
    """).fetchone()
    con.close()
    return dict(r)
