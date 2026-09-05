const express = require("express");
const cors = require("cors");
const jwt = require("jsonwebtoken");
const crypto = require("crypto");

const SECRET = "clave_de_ejemplo_no_usar_en_produccion";
const app = express();
app.use(express.json());
app.use(cors({ origin: "http://localhost:5500", credentials: true }));

const hashPw = (p) => crypto.createHash("sha256").update(p).digest("hex");
const USUARIOS = { "carlos@ejemplo.com": { pw: hashPw("secreto123"), nombre: "Carlos", rol: "user" } };

app.post("/login", (req, res) => {
  const { email, password } = req.body;
  const u = USUARIOS[email];
  if (!u || u.pw !== hashPw(password)) return res.status(401).json({ detail: "credenciales invalidas" });
  const token = jwt.sign({ sub: email, rol: u.rol }, SECRET, { expiresIn: "1h" });
  res.json({ token });
});

// middleware que protege endpoints
function auth(req, res, next) {
  const header = req.header("Authorization") || "";
  const token = header.replace("Bearer ", "");
  try { req.user = jwt.verify(token, SECRET); next(); }
  catch { res.status(401).json({ detail: "token invalido o expirado" }); }
}

app.get("/perfil", auth, (req, res) => {
  const email = req.user.sub;
  res.json({ email, nombre: USUARIOS[email].nombre, rol: req.user.rol });
});

app.listen(8010, () => console.log("API en :8010"));
