# 14 · TypeScript, de 0

JavaScript con tipos: la red de seguridad que atrapa errores mientras escribís, no en producción. De no saber qué es un tipo a usar genéricos.

## Qué hay acá
- `manual.html` — 9 capítulos: por qué existe TypeScript, tipos básicos e inferencia, funciones tipadas, interfaces, union types y narrowing, genéricos, tsconfig y modo estricto (más el porqué de evitar `any`), y construir con IA.
- `ejemplos/ejemplos.ts` — código correcto tipado (tipos, interfaz, union, genérico) que compila y corre.
- `ejemplos/errores.ts` — código con 5 bugs clásicos para ver qué atrapa el compilador.
- `ejemplos/pruebas.txt` — salida real: el código correcto corriendo y los 5 errores que `tsc` marcó.

## Probar
```
npm install -g typescript
tsc ejemplos.ts --strict && node ejemplos.js
tsc errores.ts --strict --noUncheckedIndexedAccess --noEmit   # ver los errores
```
