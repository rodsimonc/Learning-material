interface Producto { id: number; nombre: string; precio: number; }
function precioConIva(precio: number): number { return precio * 1.21; }
type Estado = "pendiente" | "pagado" | "entregado";

// ERROR 1: pasar un string donde va un number
precioConIva("1000");

// ERROR 2: falta una propiedad obligatoria
const p: Producto = { id: 1, nombre: "Pizza" };

// ERROR 3: un valor que no está en el union
const e: Estado = "cancelado";

// ERROR 4: typo en una propiedad
console.log(p.nombr);

// ERROR 5: usar algo que puede ser undefined sin chequear
const lista: number[] = [];
const x: number = lista[0];
console.log(x.toFixed(2));
