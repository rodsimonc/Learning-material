# 15 · React con TypeScript

El paso que junta todo el frontend: construir interfaces con componentes reutilizables que se actualizan solos. Reconstruye el frontend de la tienda (catálogo + carrito) en React 19 con TypeScript.

## Qué hay acá
- `manual.html` — 14 capítulos: qué es React (declarativo vs imperativo), componentes y JSX, props, estado con useState, listas y keys, eventos, custom hooks, useEffect y consumir una API, TanStack Query, estructura y build con Vite, la tienda armada, buenas prácticas y errores comunes, y construir con IA.
- `ejemplos/` — el proyecto React + TS completo (Vite):
  - `src/tipos.ts` interfaces · `src/datos.ts` catálogo · `src/useCarrito.ts` custom hook · `src/componentes/` TarjetaProducto y Carrito · `src/App.tsx`.
- `ejemplos/pruebas.txt` — salida real: el build (tsc + vite) y la interacción probada en navegador (agregar/quitar, total correcto).
- `ejemplos/captura.png` — la tienda funcionando.

## Probar
```
cd ejemplos
npm install
npm run dev      # desarrollo con recarga en vivo
npm run build    # compila TS + build de producción
```
