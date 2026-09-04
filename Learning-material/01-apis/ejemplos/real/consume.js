const API = "https://jsonplaceholder.typicode.com";
(async () => {
  const r = await fetch(`${API}/todos/1`);
  if (!r.ok) throw new Error(`HTTP ${r.status}`);   // manejar errores
  console.log("status:", r.status);
  console.log("json:", await r.json());
})();
