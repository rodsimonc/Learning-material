# 12 · Widgets y artilugios en tu página

Cómo generar e integrar widgets dentro de una página web: embeber los de terceros (mapas, videos, chats, pagos) y construir los tuyos (acordeón, widget con API, web components). Con rendimiento, seguridad y privacidad.

## Qué hay acá
- `manual.html` — 13 capítulos: qué es un widget (propio vs terceros), los tres mecanismos para embeber (iframe, script, embed), widgets comunes, integrar un mapa (Google Maps/Leaflet) y un chat por script paso a paso, construir un widget propio, un widget que consume una API, web components reutilizables, rendimiento (async/defer, lazy load), seguridad y privacidad (sandbox, CSP, consentimiento), y construir con IA.
- `ejemplos/widgets/index.html` — página con tres widgets reales: un acordeón (JS vanilla), un widget de clima que consume open-meteo (API sin key), y un web component `<mi-insignia>`.
- `ejemplos/pruebas.txt` — salida real: el acordeón y el web component probados en un navegador headless (Playwright), y la respuesta real de la API de clima.
- `ejemplos/widgets_demo.png` — captura de la página con los tres widgets funcionando.

## Probar
Abrí `ejemplos/widgets/index.html` en el navegador. El acordeón y las insignias funcionan siempre; el clima necesita conexión a internet.
