import { renderHook, act } from "@testing-library/react";
import { describe, it, expect } from "vitest";
import { useCarrito } from "../useCarrito";

const pizza = { id: 1, nombre: "Pizza", categoria: "Pizzas", precio: 8500 };
const gaseosa = { id: 8, nombre: "Gaseosa", categoria: "Bebidas", precio: 1800 };

describe("useCarrito", () => {
  it("empieza vacío con total 0", () => {
    const { result } = renderHook(() => useCarrito());
    expect(result.current.items).toHaveLength(0);
    expect(result.current.total).toBe(0);
  });

  it("suma el total al agregar productos", () => {
    const { result } = renderHook(() => useCarrito());
    act(() => { result.current.agregar(pizza); });
    act(() => { result.current.agregar(pizza); });   // 2 pizzas
    act(() => { result.current.agregar(gaseosa); });
    expect(result.current.total).toBe(8500 * 2 + 1800);  // 18800
  });

  it("quita un producto del carrito", () => {
    const { result } = renderHook(() => useCarrito());
    act(() => { result.current.agregar(pizza); });
    act(() => { result.current.agregar(gaseosa); });
    act(() => { result.current.quitar(pizza.id); });
    expect(result.current.items).toHaveLength(1);
    expect(result.current.total).toBe(1800);
  });
});
