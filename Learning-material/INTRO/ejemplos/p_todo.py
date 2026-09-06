import json
tareas = []
def agregar(texto):
    tareas.append({"texto": texto, "hecha": False})
def completar(indice):
    tareas[indice]["hecha"] = True
def mostrar():
    for i, t in enumerate(tareas):
        marca = "[x]" if t["hecha"] else "[ ]"
        print(f"  {i}. {marca} {t['texto']}")

agregar("comprar harina")
agregar("preparar la masa")
agregar("hornear")
completar(0)
completar(1)
print("== lista de tareas ==")
mostrar()
# guardar y volver a cargar (persistencia con JSON)
with open("tareas.json", "w") as f:
    json.dump(tareas, f, ensure_ascii=False)
with open("tareas.json") as f:
    cargadas = json.load(f)
print("pendientes:", sum(1 for t in cargadas if not t["hecha"]))
