---
id: index
sidebar_position: 6
title: Seguridad Web
slug: /desarrollo-web-y-movil/seguridad-web
---

# Seguridad Web: Encontrar, Entender y Corregir Vulnerabilidades

Un sistema puede compilar, pasar sus pruebas funcionales y aun así ser inseguro. La mayoría de las brechas reales no explotan fallas exóticas: repiten un puñado de errores conocidos que aparecen una y otra vez en aplicaciones web. Este curso enseña a reconocer esos errores en tu propia aplicación, a entender qué daño causan y, sobre todo, a corregirlos.

El enfoque de cada módulo es el mismo triple: **cómo encontrar** la vulnerabilidad, **qué peligro implica** si queda sin corregir, y **cómo corregirla** con ejemplos concretos en el stack del bootcamp (.NET Core, API REST, SPAs que consumen esa API).

:::info Ver también
Este curso conecta con material que ya viste: la autenticación y autorización de [APIs RESTful](../capacitacion-servicios-web-api-rest/04-autenticacion-autorizacion-rest.md), las [consultas parametrizadas](../modernizacion-legacy/05-consultas-parametrizadas-en-migracion.md) y los [fundamentos de SonarQube (SAST y SCA)](../fundamentos-sonarqube/index.md). Aquí lo integramos desde la perspectiva de quien busca y remedia vulnerabilidades.
:::

## Un principio antes de empezar

Toda la práctica de este curso aplica a **sistemas propios o donde tengas autorización explícita por escrito**. Buscar vulnerabilidades en sistemas ajenos sin permiso es ilegal en la mayoría de las jurisdicciones, sin importar la intención. Un profesional de seguridad trabaja siempre dentro de un alcance acordado.

## Módulos del curso

<DocCardList />

<div className="github-only-toc">

**Contenido:**

- [1.6.1 Metodología para encontrar vulnerabilidades](./01-metodologia-para-encontrar-vulnerabilidades.md)
- [1.6.2 Inyección SQL](./02-inyeccion-sql.md)
- [1.6.3 Cross-Site Scripting (XSS)](./03-xss.md)
- [1.6.4 Autenticación y sesiones](./04-autenticacion-y-sesiones.md)
- [1.6.5 Control de acceso roto](./05-control-de-acceso-roto.md)
- [1.6.6 Configuración, secretos y cabeceras](./06-configuracion-secretos-cabeceras.md)
- [1.6.7 Dependencias vulnerables](./07-dependencias-vulnerables.md)
- [1.6.8 Del hallazgo a la corrección](./08-del-hallazgo-a-la-correccion.md)

</div>

## Cómo estudiar este curso

Empieza por la metodología (1.6.1): te da el mapa mental y las herramientas para el resto. Los módulos 1.6.2 a 1.6.7 recorren las categorías de vulnerabilidad más frecuentes, cada una con el mismo triple encontrar-peligro-corregir. El módulo 1.6.8 cierra el ciclo: qué hacer con un hallazgo una vez que lo tienes, cómo priorizarlo y cómo llevar la corrección hasta el pipeline.

Las categorías siguen el marco del [OWASP Top 10](https://owasp.org/Top10/), la referencia de industria sobre los riesgos más críticos en aplicaciones web.

<AuthorCredit />
