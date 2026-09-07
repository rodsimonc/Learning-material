# 26 · Testing del stack moderno

Testear el frontend de verdad: componentes de React (Vitest + React Testing Library) y la app entera end-to-end (Playwright). Amplía el librito 04 (testing base) al stack moderno, sobre la tienda React del librito 15.

## Qué hay acá
- `manual.html` — 7 capítulos: la pirámide de testing, tests unitarios (Vitest), tests de componente (React Testing Library), tests end-to-end (Playwright), qué testear y qué no, y cierre.
- `ejemplos/useCarrito.test.ts` — tests unitarios del hook del carrito.
- `ejemplos/TarjetaProducto.test.tsx` — tests de componente (render, clic, spy).
- `ejemplos/e2e.test.mjs` — test end-to-end del flujo de compra con Playwright.
- `ejemplos/salidas.txt` — las corridas reales: 5 tests de Vitest y 5 E2E, todos en verde.

## Probar (dentro del proyecto React del librito 15)
```
npm install -D vitest @testing-library/react @testing-library/jest-dom jsdom @vitejs/plugin-react
npx vitest run          # unitarios + componente
node e2e.test.mjs       # end-to-end (necesita la app buildeada y Playwright)
```
