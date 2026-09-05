import type { Producto } from "./tipos";

// En una app real esto viene de la API (GET /productos, librito 09).
// Acá va estático para que el ejemplo corra solo.
export const CATALOGO: Producto[] = [
  { id: 1, nombre: "Empanada de carne", categoria: "Empanadas", precio: 1200 },
  { id: 4, nombre: "Pizza muzzarella", categoria: "Pizzas", precio: 8500 },
  { id: 5, nombre: "Pizza napolitana", categoria: "Pizzas", precio: 9800 },
  { id: 6, nombre: "Milanesa con papas", categoria: "Platos", precio: 9500 },
  { id: 8, nombre: "Gaseosa 500ml", categoria: "Bebidas", precio: 1800 },
  { id: 11, nombre: "Flan casero", categoria: "Postres", precio: 3500 },
];
