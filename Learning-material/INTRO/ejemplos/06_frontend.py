# Python puede generar la estructura del frontend (HTML).
# Un div y una lista NO son magia: son texto con una estructura.

def div(contenido, clase=""):
    c = f' class="{clase}"' if clase else ""
    return f"<div{c}>{contenido}</div>"

def lista(items):
    lis = "".join(f"  <li>{x}</li>\n" for x in items)
    return f"<ul>\n{lis}</ul>"

productos = ["Pizza", "Empanada", "Flan"]
print("== un div ==")
print(div("Hola", clase="saludo"))
print("\n== una lista (ul > li) ==")
print(lista(productos))
print("\n== un div con una lista adentro (así se anidan) ==")
print(div(lista(productos), clase="menu"))
