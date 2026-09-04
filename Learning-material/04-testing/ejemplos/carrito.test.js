const { subtotal, aplicarDescuento } = require("./carrito");

test("subtotal suma bien", () => {
  expect(subtotal([[100, 2], [50, 1]])).toBe(250);
});

test("carrito vacio da 0", () => {
  expect(subtotal([])).toBe(0);
});

test.each([
  [100, 0, 100],
  [100, 10, 90],
  [100, 100, 0],
])("descuento(%i, %i) = %i", (monto, pct, esperado) => {
  expect(aplicarDescuento(monto, pct)).toBe(esperado);
});

test("descuento invalido lanza error", () => {
  expect(() => aplicarDescuento(100, 150)).toThrow();
});
