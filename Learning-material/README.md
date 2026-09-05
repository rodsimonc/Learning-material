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
| 09 | [Conectar frontend y backend](09-fullstack-frontend-backend/) | Arquitecturas (SPA+API, monolito, BFF), el contrato, CORS, JWT, config y los must de seguridad. Paso a paso y con IA. Con salida real | Listo |
| 10 | [Backend SQL, de 0 al deploy](10-backend-sql/) | Base relacional, SQL, esquema, ORM, CRUD (Python y Node), migraciones, inyección SQL, índices y deploy de una Postgres gestionada. Con salida real | Listo |
| 11 | [Backend NoSQL, de 0 al deploy](11-backend-nosql/) | MongoDB: documentos, CRUD (Python y Node), modelado, agregación, SQL vs NoSQL, seguridad y deploy en Atlas. Corrido contra un Mongo real | Listo |
| 12 | [Widgets y artilugios](12-widgets-e-integraciones/) | Embeber terceros (iframe/script) y construir los tuyos: acordeón, widget con API, web components. Rendimiento, seguridad y privacidad. Con salida real | Listo |
| 13 | [Tienda de alimentos (sistema completo)](13-tienda-de-alimentos/) | Proyecto integral: pagos (MercadoPago + webhook, QR real, transferencia), reservas con capacidad, y dashboard (ventas, combos con self-join, picos por hora, inventario). Reúne 01, 07, 09 y 10. Con salida real | Listo |
| 14 | [TypeScript](14-typescript/) | JavaScript con tipos: inferencia, interfaces, union types, genéricos, modo estricto. Con los errores reales que atrapa tsc | Listo |
| 15 | [React con TypeScript](15-react/) | Componentes, props, estado, hooks, listas, eventos, custom hooks, TanStack Query. Reconstruye el frontend de la tienda. Probado en navegador | Listo |
| 16 | [Autenticación y usuarios](16-autenticacion/) | bcrypt, JWT, endpoints protegidos, roles (401/403), refresh tokens, OAuth y reset de contraseña. Todo el flujo probado | Listo |
| 17 | [Archivos y storage](17-archivos-y-storage/) | Subir, validar (tipo/tamaño), guardar seguro (UUID), servir sin path traversal, y storage en la nube (S3/Supabase). Con salida real | Listo |
| 18 | [Emails y notificaciones](18-emails-y-notificaciones/) | Transaccionales (HTML+texto), plantillas, proveedores y anti-spam (SPF/DKIM/DMARC), notificaciones. Enviados de verdad por SMTP | Listo |
| 19 | [Observabilidad](19-observabilidad/) | Logs estructurados (JSON), request id, captura de errores, healthcheck, Sentry y métricas. Con logs reales | Listo |
| 20 | [Deploy a la nube](20-deploy-a-la-nube/) | De local a producción con Railway/Render: config por entorno, comando de producción, base, secretos, dominio y HTTPS. App probada en modo producción | Listo |
| 21 | [AWS (teórico)](21-aws-teorico/) | El mapa conceptual: EC2, S3, RDS, Lambda, IAM, VPC, precios y cuándo AWS vs PaaS. Cada servicio atado a la colección | Listo |
| 22 | [IA y LLMs](22-ia-llms/) | Integrar modelos en una app: chat, streaming, RAG y function calling (Claude y OpenAI). Retrieval y dispatch probados | Listo |

Y aparte, un track completo de frontend:

| Track | Tema | Qué cubre | Estado |
|-------|------|-----------|--------|
| [Frontend, de 0 a una landing](frontend-de-0-a-landing/) | 14 libritos | De cómo funciona la web a publicar una landing: HTML, CSS, Flexbox/Grid, responsive, JavaScript, DOM, formularios, accesibilidad, SEO, rendimiento, diseño, el proyecto y el deploy | Listo |

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

Para el desarrollo web de punta a punta, otro camino: el **track de frontend** (de 0 a una landing) → **TypeScript** (14) → **React** (15) → **conectar frontend y backend** (09) → **backend SQL** (10) o **NoSQL** (11) → **autenticación** (16) → **archivos** (17), **emails** (18) → **widgets** (12). Y para llevarlo a producción: **observabilidad** (19) → **deploy a la nube** (20) → **AWS** (21). El proyecto que reúne casi todo es la **tienda** (13), y para sumarle inteligencia, **IA y LLMs** (22).

Con esta ruta construís una aplicación completa y la ponés en internet: la interfaz moderna (React + TS), el backend con datos, usuarios, archivos y emails, la seguridad y el monitoreo, el deploy, y hasta un asistente con IA.
