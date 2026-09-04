import sqlite3
con = sqlite3.connect(":memory:")
con.executescript("""
CREATE TABLE usuarios (id INTEGER, usuario TEXT, password TEXT);
INSERT INTO usuarios VALUES (1,'carlos','secreto123'),(2,'ana','pass456'),(3,'admin','root!');
""")
cur = con.cursor()

def login_VULNERABLE(usuario):
    # MAL: pega el texto del usuario directo en el SQL
    q = "SELECT id, usuario FROM usuarios WHERE usuario = '" + usuario + "'"
    print("  SQL armado:", q)
    return cur.execute(q).fetchall()

def login_SEGURO(usuario):
    # BIEN: parámetro, el motor lo trata como dato, no como código
    return cur.execute("SELECT id, usuario FROM usuarios WHERE usuario = ?", (usuario,)).fetchall()

ataque = "' OR '1'='1"
print("### Entrada del atacante:", repr(ataque))
print()
print("VULNERABLE (concatenando):")
print("  resultado:", login_VULNERABLE(ataque))
print("  -> devolvió TODA la tabla. El atacante entró sin usuario válido.")
print()
print("SEGURO (parametrizado):")
print("  resultado:", login_SEGURO(ataque))
print("  -> vacío. El ataque se trató como un nombre de usuario literal.")
