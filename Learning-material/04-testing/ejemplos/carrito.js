function subtotal(items) {
  return items.reduce((acc, [precio, cant]) => acc + precio * cant, 0);
}
function aplicarDescuento(monto, porcentaje) {
  if (porcentaje < 0 || porcentaje > 100) throw new Error("porcentaje invalido");
  return monto * (1 - porcentaje / 100);
}
module.exports = { subtotal, aplicarDescuento };
