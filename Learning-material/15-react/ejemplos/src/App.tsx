import { CATALOGO } from "./datos";
import { useCarrito } from "./useCarrito";
import { TarjetaProducto } from "./componentes/TarjetaProducto";
import { Carrito } from "./componentes/Carrito";
import "./App.css";

export default function App() {
  const { items, agregar, quitar, total } = useCarrito();

  return (
    <div className="app">
      <header><h1>Sabores del Barrio</h1></header>
      <main>
        <section className="catalogo">
          {CATALOGO.map((p) => (
            <TarjetaProducto key={p.id} producto={p} onAgregar={agregar} />
          ))}
        </section>
        <Carrito items={items} total={total} onQuitar={quitar} />
      </main>
    </div>
  );
}
