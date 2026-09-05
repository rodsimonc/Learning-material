import type { ItemCarrito } from "../tipos";

interface Props {
  items: ItemCarrito[];
  total: number;
  onQuitar: (id: number) => void;
}

export function Carrito({ items, total, onQuitar }: Props) {
  if (items.length === 0) {
    return <aside className="carrito"><h2>Carrito</h2><p>Vacío</p></aside>;
  }
  return (
    <aside className="carrito">
      <h2>Carrito</h2>
      <ul>
        {items.map((i) => (
          <li key={i.producto.id}>
            <span>{i.cantidad}× {i.producto.nombre}</span>
            <button className="x" onClick={() => onQuitar(i.producto.id)}>quitar</button>
          </li>
        ))}
      </ul>
      <p className="total" data-testid="total">
        Total: ${total.toLocaleString("es-AR")}
      </p>
    </aside>
  );
}
