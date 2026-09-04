import sqlite3, sys
con = sqlite3.connect(":memory:")
con.execute("PRAGMA foreign_keys=ON")
cur = con.cursor()

def show(sql, titulo=None):
    print(f"$ {titulo or sql.strip()}")
    cur.execute(sql)
    if cur.description:
        cols = [d[0] for d in cur.description]
        rows = cur.fetchall()
        w = [max(len(str(c)), *(len(str(r[i])) for r in rows)) if rows else len(str(c)) for i,c in enumerate(cols)]
        line = " | ".join(c.ljust(w[i]) for i,c in enumerate(cols))
        print(line); print("-"*len(line))
        for r in rows:
            print(" | ".join(str(v).ljust(w[i]) for i,v in enumerate(r)))
    print()

# --- CREATE ---
cur.executescript("""
CREATE TABLE usuarios (
  id      INTEGER PRIMARY KEY,
  nombre  TEXT NOT NULL,
  ciudad  TEXT
);
CREATE TABLE pedidos (
  id        INTEGER PRIMARY KEY,
  usuario_id INTEGER NOT NULL REFERENCES usuarios(id),
  producto  TEXT NOT NULL,
  monto     REAL NOT NULL,
  fecha     TEXT
);
""")
cur.executemany("INSERT INTO usuarios (id,nombre,ciudad) VALUES (?,?,?)",
    [(1,"Carlos","Mar del Plata"),(2,"Ana","Rosario"),(3,"Luis","Rosario"),(4,"Sofia","Córdoba")])
cur.executemany("INSERT INTO pedidos (id,usuario_id,producto,monto,fecha) VALUES (?,?,?,?,?)",
    [(1,1,"Teclado",25000,"2026-08-01"),(2,1,"Mouse",12000,"2026-08-03"),
     (3,2,"Monitor",90000,"2026-08-05"),(4,3,"Teclado",25000,"2026-08-09"),
     (5,1,"Monitor",90000,"2026-08-11"),(6,2,"Cable",3000,"2026-08-12")])
con.commit()
print("(tablas creadas y datos insertados)\n")

step = sys.argv[1] if len(sys.argv)>1 else "all"

if step in ("select","all"):
    show("SELECT nombre, ciudad FROM usuarios;")
    show("SELECT * FROM usuarios WHERE ciudad = 'Rosario';")
    show("SELECT producto, monto FROM pedidos ORDER BY monto DESC LIMIT 3;", "SELECT ... ORDER BY monto DESC LIMIT 3")
if step in ("where","all"):
    show("SELECT producto, monto FROM pedidos WHERE monto BETWEEN 10000 AND 50000;")
    show("SELECT nombre FROM usuarios WHERE ciudad IN ('Rosario','Córdoba');")
    show("SELECT producto FROM pedidos WHERE producto LIKE 'M%';")
if step in ("join","all"):
    show("""SELECT u.nombre, p.producto, p.monto
FROM pedidos p
JOIN usuarios u ON u.id = p.usuario_id
ORDER BY u.nombre;""", "INNER JOIN: pedidos con su usuario")
    show("""SELECT u.nombre, COUNT(p.id) AS pedidos
FROM usuarios u
LEFT JOIN pedidos p ON p.usuario_id = u.id
GROUP BY u.id
ORDER BY pedidos DESC;""", "LEFT JOIN: todos los usuarios, incluso sin pedidos")
if step in ("agg","all"):
    show("""SELECT u.nombre, SUM(p.monto) AS total, COUNT(*) AS cantidad
FROM pedidos p JOIN usuarios u ON u.id = p.usuario_id
GROUP BY u.id
HAVING total > 30000
ORDER BY total DESC;""", "GROUP BY + HAVING: quién gastó más de 30000")
    show("SELECT producto, COUNT(*) AS veces, AVG(monto) AS promedio FROM pedidos GROUP BY producto ORDER BY veces DESC;")
if step in ("mod","all"):
    show("UPDATE usuarios SET ciudad='Buenos Aires' WHERE id=4;", "UPDATE (una fila)")
    show("SELECT id,nombre,ciudad FROM usuarios WHERE id=4;")
if step in ("index","all"):
    show("EXPLAIN QUERY PLAN SELECT * FROM pedidos WHERE usuario_id = 1;", "EXPLAIN QUERY PLAN (sin índice)")
    cur.execute("CREATE INDEX idx_pedidos_usuario ON pedidos(usuario_id);")
    show("EXPLAIN QUERY PLAN SELECT * FROM pedidos WHERE usuario_id = 1;", "EXPLAIN QUERY PLAN (con índice)")
