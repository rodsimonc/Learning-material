const { WebSocketServer } = require("ws");
const wss = new WebSocketServer({ port: 9102 });

wss.on("connection", (ws) => {
  ws.send(JSON.stringify({ tipo: "bienvenida", texto: "conectado" })); // empuje inicial
  ws.on("message", (raw) => {
    const data = JSON.parse(raw);
    ws.send(JSON.stringify({ tipo: "eco", recibido: data.texto }));
  });
});
console.log("WS en :9102");
