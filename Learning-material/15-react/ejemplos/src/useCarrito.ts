import { useState } from "react";
import type { Producto, ItemCarrito } from "./tipos";

// Un custom hook: encapsula la lógica del carrito y la hace reutilizable.
// Esta es la idea central de React: componer con piezas propias.
export function useCarrito() {
  const [items, setItems] = useState<ItemCarrito[]>([]);

  function agregar(producto: Producto) {
    setItems((prev) => {
      const existe = prev.find((i) => i.producto.id === producto.id);
      if (existe) {
        return prev.map((i) =>
          i.producto.id === producto.id
            ? { ...i, cantidad: i.cantidad + 1 }
            : i
        );
      }
      return [...prev, { producto, cantidad: 1 }];
    });
  }

  function quitar(id: number) {
    setItems((prev) => prev.filter((i) => i.producto.id !== id));
  }

  const total = items.reduce(
    (acc, i) => acc + i.producto.precio * i.cantidad,
    0
  );

  return { items, agregar, quitar, total };
}
