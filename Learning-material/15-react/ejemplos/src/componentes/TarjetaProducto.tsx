import type { Producto } from "../tipos";

// Un componente: recibe props tipadas y devuelve UI. Reutilizable por producto.
interface Props {
  producto: Producto;
  onAgregar: (p: Producto) => void;
}

export function TarjetaProducto({ producto, onAgregar }: Props) {
  return (
    <div className="tarjeta">
      <span className="cat">{producto.categoria}</span>
      <h3>{producto.nombre}</h3>
      <p className="precio">${producto.precio.toLocaleString("es-AR")}</p>
      <button onClick={() => onAgregar(producto)}>Agregar</button>
    </div>
  );
}
