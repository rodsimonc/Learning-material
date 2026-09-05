// TypeScript = JavaScript + tipos. Este archivo demuestra qué atrapa tsc.

// 1. Tipos básicos e inferencia
let nombre: string = "Carlos";
let edad = 30;              // inferido como number
const activo: boolean = true;

// 2. Funciones tipadas
function precioConIva(precio: number, iva: number = 0.21): number {
  return precio * (1 + iva);
}

// 3. Interfaces: la forma de un objeto
interface Producto {
  id: number;
  nombre: string;
  precio: number;
  stock?: number;          // opcional
}

const pizza: Producto = { id: 1, nombre: "Muzzarella", precio: 8500 };

// 4. Union types y narrowing
type Estado = "pendiente" | "pagado" | "entregado";
function describir(e: Estado): string {
  return e === "pagado" ? "Ya cobrado" : "En curso";
}

// 5. Genéricos: una función que sirve para cualquier tipo, sin perder el tipo
function primero<T>(lista: T[]): T | undefined {
  return lista[0];
}

const p = primero<Producto>([pizza]);   // p es Producto | undefined
const n = primero([1, 2, 3]);           // n es number | undefined

// Uso correcto
console.log("precio con IVA:", precioConIva(1000));
console.log("estado:", describir("pagado"));
console.log("primer producto:", primero([pizza])?.nombre);
console.log("con opcional stock:", pizza.stock ?? "sin definir");
