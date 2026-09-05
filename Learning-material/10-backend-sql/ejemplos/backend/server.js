// Backend SQL en Node: Express + better-sqlite3. CRUD de tareas.
// Para Postgres se usaria la libreria 'pg' con la misma logica.
const express = require("express");
const Database = require("better-sqlite3");

const db = new Database("tareas.db");
db.exec(`CREATE TABLE IF NOT EXISTS tareas (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  titulo TEXT NOT NULL,
  hecha INTEGER NOT NULL DEFAULT 0
)`);

const app = express();
app.use(express.json());

const aSalida = (f) => ({ id: f.id, titulo: f.titulo, hecha: !!f.hecha });

app.post("/tareas", (req, res) => {
  const { titulo, hecha = false } = req.body;
  // parametrizado con ? : nunca concatenar la entrada del usuario
  const r = db.prepare("INSERT INTO tareas (titulo,hecha) VALUES (?,?)")
              .run(titulo, hecha ? 1 : 0);
  const f = db.prepare("SELECT * FROM tareas WHERE id=?").get(r.lastInsertRowid);
  res.json(aSalida(f));
});

app.get("/tareas", (_req, res) => {
  res.json(db.prepare("SELECT * FROM tareas").all().map(aSalida));
});

app.get("/tareas/:id", (req, res) => {
  const f = db.prepare("SELECT * FROM tareas WHERE id=?").get(req.params.id);
  if (!f) return res.status(404).json({ detail: "no existe" });
  res.json(aSalida(f));
});

app.put("/tareas/:id", (req, res) => {
  const { titulo, hecha = false } = req.body;
  const r = db.prepare("UPDATE tareas SET titulo=?, hecha=? WHERE id=?")
              .run(titulo, hecha ? 1 : 0, req.params.id);
  if (r.changes === 0) return res.status(404).json({ detail: "no existe" });
  const f = db.prepare("SELECT * FROM tareas WHERE id=?").get(req.params.id);
  res.json(aSalida(f));
});

app.delete("/tareas/:id", (req, res) => {
  const r = db.prepare("DELETE FROM tareas WHERE id=?").run(req.params.id);
  if (r.changes === 0) return res.status(404).json({ detail: "no existe" });
  res.json({ borrada: Number(req.params.id) });
});

if (require.main === module) app.listen(8000, () => console.log("en :8000"));
module.exports = app;
