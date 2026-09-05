"""
Base de datos de la tienda de alimentos "Sabores del Barrio".
SQLite: un archivo, cero configuración. En producción, la misma estructura
va a Postgres cambiando solo la conexión (ver librito 10).
"""
import sqlite3
from pathlib import Path

RUTA = Path(__file__).parent / "tienda.db"


def conectar():
    con = sqlite3.connect(RUTA)
    con.row_factory = sqlite3.Row          # filas como diccionarios
    con.execute("PRAGMA foreign_keys = ON")  # respeta las relaciones
    return con


ESQUEMA = """
CREATE TABLE IF NOT EXISTS productos (
  id        INTEGER PRIMARY KEY,
  nombre    TEXT NOT NULL,
  categoria TEXT NOT NULL,
  precio    REAL NOT NULL,
  stock     INTEGER NOT NULL DEFAULT 0,
  stock_min INTEGER NOT NULL DEFAULT 5
);

CREATE TABLE IF NOT EXISTS pedidos (
  id        INTEGER PRIMARY KEY,
  cliente   TEXT NOT NULL,
  creado_en TEXT NOT NULL,          -- ISO: 2026-09-05T13:40:00
  estado    TEXT NOT NULL DEFAULT 'pendiente',  -- pendiente|pagado|entregado
  total     REAL NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS pedido_items (
  id          INTEGER PRIMARY KEY,
  pedido_id   INTEGER NOT NULL REFERENCES pedidos(id),
  producto_id INTEGER NOT NULL REFERENCES productos(id),
  cantidad    INTEGER NOT NULL,
  precio_unit REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS pagos (
  id         INTEGER PRIMARY KEY,
  pedido_id  INTEGER NOT NULL REFERENCES pedidos(id),
  metodo     TEXT NOT NULL,         -- mercadopago|qr|transferencia
  estado     TEXT NOT NULL,         -- iniciado|aprobado|rechazado
  referencia TEXT,                  -- id externo (ej. payment_id de MP)
  creado_en  TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS reservas (
  id         INTEGER PRIMARY KEY,
  cliente    TEXT NOT NULL,
  fecha      TEXT NOT NULL,         -- 2026-09-10
  hora       TEXT NOT NULL,         -- 20:00
  personas   INTEGER NOT NULL,
  estado     TEXT NOT NULL DEFAULT 'confirmada'  -- confirmada|cancelada
);

-- índices para las consultas del dashboard (ver librito 10)
CREATE INDEX IF NOT EXISTS idx_pedidos_creado ON pedidos(creado_en);
CREATE INDEX IF NOT EXISTS idx_items_pedido ON pedido_items(pedido_id);
CREATE INDEX IF NOT EXISTS idx_reservas_fecha ON reservas(fecha, hora);
"""


def crear_esquema():
    con = conectar()
    con.executescript(ESQUEMA)
    con.commit()
    con.close()


if __name__ == "__main__":
    crear_esquema()
    print("esquema creado en", RUTA)
