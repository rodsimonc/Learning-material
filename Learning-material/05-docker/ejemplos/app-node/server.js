const express = require("express");
const app = express();
app.get("/", (_req, res) => res.json({ mensaje: "hola desde un contenedor" }));
app.listen(3000, () => console.log("en :3000"));
