# Learning material

Una colección de libritos cortos sobre temas de programación. Cada uno arranca de cero y termina en algo que podés usar, con código que se ejecutó de verdad, no pseudocódigo.

La idea es simple: un tema, un librito, autocontenido. Se van sumando con el tiempo.

## Libritos

| # | Tema | Qué cubre | Estado |
|---|------|-----------|--------|
| 01 | [APIs, de 0 a producción](01-apis/) | Qué es una API, HTTP, formatos, auth, y los 6 estilos (REST, GraphQL, gRPC, WebSockets, Webhooks, SOAP) construidos y testeados en Python y Node | Listo |
| 02 | [Git y control de versiones](02-git/) | Los tres estados, commits, ramas, merge, conflictos, deshacer, remotos y Pull Requests. Con salidas reales de la terminal | Listo |
| 03 | [Bases de datos y SQL](03-sql/) | Tablas, SELECT, WHERE, JOIN, GROUP BY, índices y transacciones. SQL corrido contra una base real | Listo |
| 04 | [Testing](04-testing/) | pytest y jest de 0: casos, errores, mocks, integración y cobertura. Con corridas reales | Listo |
| 05 | [Docker y deploy](05-docker/) | Contenedores, imágenes, Dockerfiles para Python y Node, multi-stage, Compose y deploy | Listo |
| 06 | [CI/CD con GitHub Actions](06-cicd/) | Pipelines, workflows, matrices, secrets, caché y deploy automático | Listo |
| 07 | [Ciberseguridad web](07-ciberseguridad/) | Inyección SQL, XSS, CSRF, auth, control de acceso, secretos y headers. Con ataques reales y su defensa | Listo |
| 08 | [Arquitectura de software](08-arquitectura/) | Acoplamiento y cohesión, capas, monolito vs microservicios, escalado y cómo decidir | Listo |

## Cómo se leen

Cada librito es una carpeta con un `manual.html`: un libro navegable con índice lateral, capítulos, progreso y tema claro/oscuro. Se abre en cualquier navegador.

- Cloná el repo y abrí el `manual.html` del tema que quieras, o
- descargalo desde GitHub (botón de descarga en la vista del archivo) y abrilo local.

El código de ejemplo vive en la subcarpeta `ejemplos/` de cada librito. Donde dice "salida real", en `ejemplos/salidas/` está la salida capturada de correrlo.

## Formato de cada librito

```
NN-tema/
  manual.html        el libro navegable
  ejemplos/          código que corre, con sus salidas
  README.md          de qué va este librito
```

## Recorrido sugerido

Los libritos se apoyan unos en otros. Un orden que funciona:

**APIs → Git → SQL → Testing → Docker → CI/CD → Ciberseguridad → Arquitectura.**

Con esos ocho tenés el ciclo completo: construir software, versionarlo, guardarlo, probarlo, empaquetarlo, desplegarlo, asegurarlo y diseñarlo para que crezca.
