// Backend NoSQL en Node: Express + driver oficial de MongoDB. CRUD de tareas.
// Para Atlas se cambia solo la URL de conexion.
const express = require("express");
const { MongoClient, ObjectId } = require("mongodb");

const URL = process.env.MONGO_URL || "mongodb://127.0.0.1:27017";
const cliente = new MongoClient(URL);
let tareas;

const aSalida = (d) => ({ id: d._id.toString(), titulo: d.titulo, hecha: d.hecha });
const oid = (id) => { try { return new ObjectId(id); } catch { return null; } };

const app = express();
app.use(express.json());

app.post("/tareas", async (req, res) => {
  const { titulo, hecha = false } = req.body;
  const r = await tareas.insertOne({ titulo, hecha });
  const d = await tareas.findOne({ _id: r.insertedId });
  res.json(aSalida(d));
});

app.get("/tareas", async (_req, res) => {
  res.json((await tareas.find().toArray()).map(aSalida));
});

app.get("/tareas/:id", async (req, res) => {
  const _id = oid(req.params.id);
  if (!_id) return res.status(400).json({ detail: "id invalido" });
  const d = await tareas.findOne({ _id });
  if (!d) return res.status(404).json({ detail: "no existe" });
  res.json(aSalida(d));
});

app.put("/tareas/:id", async (req, res) => {
  const _id = oid(req.params.id);
  if (!_id) return res.status(400).json({ detail: "id invalido" });
  const { titulo, hecha = false } = req.body;
  const r = await tareas.updateOne({ _id }, { $set: { titulo, hecha } });
  if (r.matchedCount === 0) return res.status(404).json({ detail: "no existe" });
  res.json(aSalida(await tareas.findOne({ _id })));
});

app.delete("/tareas/:id", async (req, res) => {
  const _id = oid(req.params.id);
  if (!_id) return res.status(400).json({ detail: "id invalido" });
  const r = await tareas.deleteOne({ _id });
  if (r.deletedCount === 0) return res.status(404).json({ detail: "no existe" });
  res.json({ borrada: req.params.id });
});

async function iniciar() {
  await cliente.connect();
  tareas = cliente.db("miapp").collection("tareas");
  app.listen(8000, () => console.log("en :8000"));
}
if (require.main === module) iniciar();
module.exports = { app, cliente };
