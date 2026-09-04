const WebSocket = require("ws");
const ws = new WebSocket("ws://127.0.0.1:9102");
const mensajes = ["hola", "como va"];
let i = 0;
ws.on("message", (raw) => {
  console.log("<- server:", raw.toString());
  if (i < mensajes.length) {
    const t = mensajes[i++];
    console.log("-> yo:    ", t);
    ws.send(JSON.stringify({ tipo: "mensaje", texto: t }));
  } else { ws.close(); }
});
