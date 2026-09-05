"""
API de la tienda de alimentos "Sabores del Barrio".
Une todo: catálogo, pedidos (con descuento de stock), pagos, reservas y
el dashboard interno. Se corre con: uvicorn main:app --reload
"""
from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from db import conectar, crear_esquema
import pagos
import stats

app = FastAPI(title="Sabores del Barrio · API")

# el frontend vive en otro origen: hay que habilitarlo (ver librito 09)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500"],
    allow_methods=["*"], allow_headers=["*"],
)

crear_esquema()

CAPACIDAD_POR_HORA = 20  # personas máximas por franja de reserva


# ---------- Modelos ----------
class ItemPedido(BaseModel):
    producto_id: int
    cantidad: int


class PedidoIn(BaseModel):
    cliente: str
    items: list[ItemPedido]
    metodo_pago: str = "qr"      # mercadopago | qr | transferencia


class ReservaIn(BaseModel):
    cliente: str
    fecha: str
    hora: str
    personas: int


# ---------- Catálogo ----------
@app.get("/productos")
def listar_productos():
    con = conectar()
    r = [dict(x) for x in con.execute("SELECT * FROM productos ORDER BY categoria, nombre")]
    con.close()
    return r


# ---------- Pedidos ----------
@app.post("/pedidos")
def crear_pedido(p: PedidoIn):
    con = conectar()
    cur = con.cursor()
    # validar stock ANTES de cobrar
    total = 0
    detalle = []
    for it in p.items:
        prod = cur.execute("SELECT * FROM productos WHERE id=?", (it.producto_id,)).fetchone()
        if not prod:
            raise HTTPException(404, f"producto {it.producto_id} no existe")
        if prod["stock"] < it.cantidad:
            raise HTTPException(409, f"sin stock de {prod['nombre']} "
                                     f"(quedan {prod['stock']})")
        total += prod["precio"] * it.cantidad
        detalle.append((prod, it.cantidad))

    cur.execute("INSERT INTO pedidos (cliente,creado_en,estado,total)"
                " VALUES (?,?,?,?)",
                (p.cliente, datetime.now().isoformat(), "pendiente", total))
    pid = cur.lastrowid
    for prod, cant in detalle:
        cur.execute("INSERT INTO pedido_items (pedido_id,producto_id,cantidad,precio_unit)"
                    " VALUES (?,?,?,?)", (pid, prod["id"], cant, prod["precio"]))
        # descontar stock (control de consumo real)
        cur.execute("UPDATE productos SET stock = stock - ? WHERE id=?",
                    (cant, prod["id"]))
    con.commit()

    # armar el pago según el método
    info_pago = iniciar_pago(con, pid, p.metodo_pago, total, detalle)
    con.close()
    return {"pedido_id": pid, "total": total, "pago": info_pago}


def iniciar_pago(con, pid, metodo, total, detalle):
    if metodo == "mercadopago":
        items = [{"title": prod["nombre"], "quantity": cant,
                  "unit_price": prod["precio"]} for prod, cant in detalle]
        pref = pagos.crear_preferencia_mp(items, pid)
        pagos.registrar_pago(con, pid, "mercadopago", "iniciado")
        return {"metodo": "mercadopago", **pref}
    if metodo == "transferencia":
        pagos.registrar_pago(con, pid, "transferencia", "iniciado")
        return {"metodo": "transferencia", **pagos.datos_transferencia(total, pid)}
    # default: QR
    ruta = f"qr_pedido_{pid}.png"
    contenido = pagos.generar_qr_pago(total, pid, ruta)
    pagos.registrar_pago(con, pid, "qr", "iniciado")
    return {"metodo": "qr", "qr_png": ruta, "qr_contenido": contenido}


@app.post("/pedidos/{pid}/confirmar-pago")
def confirmar_pago(pid: int, referencia: str = "manual"):
    """El panel confirma un pago (transferencia recibida, o QR verificado)."""
    con = conectar()
    if not con.execute("SELECT 1 FROM pedidos WHERE id=?", (pid,)).fetchone():
        con.close(); raise HTTPException(404, "pedido no existe")
    pagos.registrar_pago(con, pid, "manual", "aprobado", referencia)
    con.close()
    return {"pedido": pid, "estado": "pagado"}


@app.post("/webhook/mp")
def webhook_mp(cuerpo: dict):
    """MercadoPago avisa acá el resultado del pago."""
    ref, estado = pagos.procesar_webhook_mp(cuerpo)
    if ref and estado == "approved":
        con = conectar()
        pagos.registrar_pago(con, int(ref), "mercadopago", "aprobado",
                             str(cuerpo.get("data", {}).get("id")))
        con.close()
    return {"ok": True}


# ---------- Reservas ----------
@app.post("/reservas")
def crear_reserva(r: ReservaIn):
    con = conectar()
    ocupadas = con.execute(
        "SELECT COALESCE(SUM(personas),0) c FROM reservas"
        " WHERE fecha=? AND hora=? AND estado='confirmada'",
        (r.fecha, r.hora)).fetchone()["c"]
    if ocupadas + r.personas > CAPACIDAD_POR_HORA:
        con.close()
        raise HTTPException(409, f"sin lugar a las {r.hora} "
                                 f"(ocupadas {ocupadas}/{CAPACIDAD_POR_HORA})")
    cur = con.cursor()
    cur.execute("INSERT INTO reservas (cliente,fecha,hora,personas)"
                " VALUES (?,?,?,?)", (r.cliente, r.fecha, r.hora, r.personas))
    con.commit()
    rid = cur.lastrowid
    con.close()
    return {"reserva_id": rid, "estado": "confirmada"}


@app.get("/reservas")
def listar_reservas():
    con = conectar()
    r = [dict(x) for x in con.execute(
        "SELECT * FROM reservas WHERE estado='confirmada' ORDER BY fecha,hora")]
    con.close()
    return r


# ---------- Dashboard interno ----------
@app.get("/dashboard/resumen")
def d_resumen(): return stats.resumen()

@app.get("/dashboard/top-productos")
def d_top(): return stats.top_productos()

@app.get("/dashboard/combos")
def d_combos(): return stats.combos_frecuentes()

@app.get("/dashboard/por-hora")
def d_hora(): return stats.pedidos_por_hora()

@app.get("/dashboard/por-dia")
def d_dia(): return stats.facturacion_por_dia()

@app.get("/dashboard/stock-bajo")
def d_stock(): return stats.stock_bajo()
