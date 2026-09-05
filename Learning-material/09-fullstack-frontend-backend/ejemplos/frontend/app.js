const API = "http://localhost:8010";   // en producción: variable de entorno
const form = document.querySelector("#form");
const aviso = document.querySelector("#aviso");
const perfil = document.querySelector("#perfil");
const datos = document.querySelector("#datos");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const email = document.querySelector("#email").value.trim();
  const password = document.querySelector("#password").value;

  try {
    // 1) login: pedir el token
    const r = await fetch(`${API}/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });
    if (!r.ok) { mostrar("Credenciales inválidas", "error"); return; }
    const { token } = await r.json();

    // 2) guardar el token (demo: en memoria; ver el libro para HttpOnly cookie)
    sessionStorage.setItem("token", token);

    // 3) usar el token para pedir un recurso protegido
    await cargarPerfil(token);
    mostrar("Sesión iniciada", "ok");
  } catch (err) {
    mostrar("No se pudo conectar con el servidor", "error");
  }
});

async function cargarPerfil(token) {
  const r = await fetch(`${API}/perfil`, {
    headers: { "Authorization": `Bearer ${token}` },   // el token viaja acá
  });
  if (!r.ok) { mostrar("Sesión expirada", "error"); return; }
  const perfilData = await r.json();
  datos.textContent = JSON.stringify(perfilData, null, 2);
  form.hidden = true;
  perfil.hidden = false;
}

document.querySelector("#salir").addEventListener("click", () => {
  sessionStorage.removeItem("token");
  location.reload();
});

function mostrar(msg, tipo) {
  aviso.textContent = msg;
  aviso.style.color = tipo === "ok" ? "#2f8f56" : "#c0392b";
}
