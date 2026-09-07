import { render, screen, fireEvent } from "@testing-library/react";
import { describe, it, expect, vi } from "vitest";
import { TarjetaProducto } from "../componentes/TarjetaProducto";

const pizza = { id: 1, nombre: "Pizza muzza", categoria: "Pizzas", precio: 8500 };

describe("TarjetaProducto", () => {
  it("muestra el nombre y el precio", () => {
    render(<TarjetaProducto producto={pizza} onAgregar={() => {}} />);
    expect(screen.getByText("Pizza muzza")).toBeTruthy();
    expect(screen.getByText(/8.500/)).toBeTruthy();
  });

  it("llama a onAgregar al hacer clic en el botón", () => {
    const onAgregar = vi.fn();                      // función espía
    render(<TarjetaProducto producto={pizza} onAgregar={onAgregar} />);
    fireEvent.click(screen.getByText("Agregar"));
    expect(onAgregar).toHaveBeenCalledWith(pizza);  // se llamó con el producto
  });
});
