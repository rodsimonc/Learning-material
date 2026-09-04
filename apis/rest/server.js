const express = require("express");
const app = express();
app.use(express.json());

const usuarios = { 42: { id: 42, nombre: "Carlos", email: "carlos@ejemplo.com" } };

app.get("/usuarios/:id", (req, res) => {
  const u = usuarios[req.params.id];
  if (!u) return res.status(404).json({ detail: "no existe" });
  res.json(u);
});

app.post("/usuarios", (req, res) => {
  const nuevoId = Math.max(...Object.keys(usuarios).map(Number)) + 1;
  usuarios[nuevoId] = { id: nuevoId, ...req.body };
  res.status(201).json(usuarios[nuevoId]);
});

app.listen(8002, () => console.log("REST en :8002"));
