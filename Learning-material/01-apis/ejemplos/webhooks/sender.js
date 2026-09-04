const crypto = require("crypto");
const SECRET = "clave_secreta_compartida";
const cuerpo = JSON.stringify({ tipo: "pago.exitoso", monto: 2500, moneda: "usd" });
const firma = crypto.createHmac("sha256", SECRET).update(cuerpo).digest("hex");

async function post(firmaUsada, etiqueta) {
  const r = await fetch("http://127.0.0.1:8006/webhooks/pagos", {
    method: "POST",
    headers: { "Content-Type": "application/json", "X-Firma": firmaUsada },
    body: cuerpo,
  });
  console.log(etiqueta, "->", r.status, await r.json());
}
(async () => {
  await post(firma, "legitimo  ");
  await post("0000", "falsificado");
})();
