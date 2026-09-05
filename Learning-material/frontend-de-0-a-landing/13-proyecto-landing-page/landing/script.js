// ===== Menú móvil: abrir y cerrar =====
const menuBtn = document.querySelector("#menuBtn");
const menu = document.querySelector("#menu");

menuBtn.addEventListener("click", () => {
  menu.classList.toggle("abierto");
});

// cerrar el menú al hacer clic en un enlace (en móvil)
menu.querySelectorAll("a").forEach((enlace) => {
  enlace.addEventListener("click", () => menu.classList.remove("abierto"));
});

// ===== Formulario: validación y feedback =====
const form = document.querySelector("#form");
const email = document.querySelector("#email");
const aviso = document.querySelector("#aviso");

form.addEventListener("submit", (event) => {
  event.preventDefault();                 // no recargar la página
  const valor = email.value.trim();

  // validar
  if (valor === "") {
    mostrar("Escribí tu email para empezar.", "error");
    email.classList.add("invalido");
    return;
  }
  if (!valor.includes("@") || !valor.includes(".")) {
    mostrar("Ese email no parece válido.", "error");
    email.classList.add("invalido");
    return;
  }

  // éxito
  email.classList.remove("invalido");
  mostrar("¡Listo! Te mandamos el acceso a " + valor, "ok");
  form.reset();
});

function mostrar(mensaje, tipo) {
  aviso.textContent = mensaje;
  aviso.style.color = tipo === "ok" ? "#2f8f56" : "#c0392b";
}
