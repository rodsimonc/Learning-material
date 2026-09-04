const express = require("express");
const crypto = require("crypto");
const app = express();
const SECRET = "clave_secreta_compartida";

// necesitamos el body crudo para verificar la firma
app.use(express.raw({ type: "application/json" }));

function firmaValida(cuerpo, firma) {
  const esperada = crypto.createHmac("sha256", SECRET).update(cuerpo).digest("hex");
  return firma.length === esperada.length &&
         crypto.timingSafeEqual(Buffer.from(esperada), Buffer.from(firma));
}

app.post("/webhooks/pagos", (req, res) => {
  const firma = req.header("X-Firma") || "";
  if (!firmaValida(req.body, firma)) return res.status(400).json({ detail: "firma invalida" });
  const evento = JSON.parse(req.body);
  console.log(`[receiver] evento OK: ${evento.tipo} monto=${evento.monto}`);
  res.json({ recibido: true });
});
app.listen(8006, () => console.log("receiver en :8006"));
