---
sidebar_position: 8
title: Dependencias vulnerables
sidebar_label: 1.6.7 Dependencias vulnerables
---

# Dependencias vulnerables

Tu aplicación no es solo el código que escribiste. Es también las decenas o cientos de librerías de terceros que usa, más las que esas librerías arrastran. Cada una es código que corre con los permisos de tu app, y una vulnerabilidad en cualquiera de ellas es una vulnerabilidad tuya. Esta es la categoría que ataca la cadena de suministro del software.

:::info Ver también
El análisis de dependencias (SCA) y su integración al pipeline se desarrollan en [SAST y SCA en la fase de validación](../fundamentos-sonarqube/05-sast-y-sca-en-validacion.md). Aquí lo aplicamos como práctica de búsqueda y remediación.
:::

## Cómo encontrarlo

La detección es automatizable, y por eso conviene tenerla siempre corriendo. Las herramientas del propio ecosistema comparan tus dependencias contra bases públicas de vulnerabilidades conocidas (CVE).

```bash
# .NET: lista paquetes con vulnerabilidades conocidas, incluidas las transitivas.
dotnet list package --vulnerable --include-transitive

# Node: audita el árbol de dependencias.
npm audit
```

En una forja como GitHub, **Dependabot** hace este análisis solo y abre pull requests con las actualizaciones. Un escáner de **SCA** (Software Composition Analysis) en el pipeline es la forma madura de no depender de que alguien se acuerde de correrlo.

### Dependencias transitivas

El detalle que más se escapa: una **dependencia transitiva** es una librería que tu proyecto no instaló directamente, sino que llega como requisito de otra. El riesgo puede existir aunque nadie la haya agregado a mano, por eso no basta revisar tu `csproj` o `package.json`: hay que mirar el árbol completo. Por eso los comandos de arriba incluyen la opción de transitivas.

## Qué peligro implica

- **Explotación de un CVE conocido:** una vulnerabilidad pública en una librería viene con su técnica de explotación documentada. Los atacantes escanean internet buscando aplicaciones que usen versiones vulnerables, y las explotan en masa. No hace falta que te elijan a ti: basta con que uses la versión.
- **Riesgo heredado sin saberlo:** una dependencia transitiva vulnerable te expone aunque tu código sea impecable.
- **Cadena de suministro:** un paquete comprometido (por un mantenedor malicioso o una cuenta secuestrada) ejecuta código en tu build o en producción.

Incidentes de enorme impacto han venido de una sola librería vulnerable ampliamente usada. Es una superficie que crece con cada dependencia que sumas.

## Cómo corregirlo

### Ante una alerta

El flujo, alineado con el de SonarQube, es:

1. **Confirmar el impacto real.** ¿Usas la parte vulnerable de la librería? ¿Es alcanzable desde una entrada del usuario? No toda alerta es igual de urgente.
2. **Actualizar** a una versión segura compatible, que suele ser la solución más rápida.
3. **Sustituir** la librería si ya no se mantiene o no hay versión segura.
4. **Documentar una excepción temporal** con contexto, dueño y fecha de revisión si no hay alternativa inmediata. La excepción no debe convertirse en olvido.

### Buenas prácticas permanentes

- **SCA en el pipeline**, que bloquee o alerte en cada cambio, con un *quality gate* que impida introducir dependencias con vulnerabilidades críticas.
- **Fijar versiones** con el *lockfile* (`packages.lock.json`, `package-lock.json`) para builds reproducibles.
- **Actualizar seguido y de a poco**, en vez de saltos enormes cada dos años que se vuelven imposibles de probar.
- **Evaluar antes de sumar** una dependencia: ¿está mantenida?, ¿cuánto arrastra?, ¿vale el riesgo? Cada dependencia es superficie de ataque.
- **Desconfiar de nombres parecidos** a paquetes populares: el *typosquatting* (un paquete malicioso con un nombre casi igual) es una técnica de ataque real.

## Resumen para agentes

- **Objetivo:** detectar y remediar dependencias con vulnerabilidades conocidas, incluidas las transitivas.
- **Entradas comunes:** manifiestos de dependencias, lockfiles, salida de SCA/Dependabot, árbol de dependencias.
- **Controles clave:** SCA en el pipeline, actualización, sustitución, excepción documentada, lockfile, evaluación previa.
- **Salidas esperadas:** sin dependencias vulnerables críticas, excepciones trazables, pipeline que verifica en cada cambio.
- **Errores frecuentes:** revisar solo dependencias directas, aceptar alertas sin evaluar impacto, convertir una excepción temporal en permanente.

## Glosario

**Dependencia** *(Dependency)* — librería de terceros que tu aplicación utiliza.

**Dependencia transitiva** *(Transitive dependency)* — dependencia que llega indirectamente, requerida por otra.

**SCA** *(Software Composition Analysis)* — análisis de dependencias contra vulnerabilidades conocidas y licencias.

**CVE** *(Common Vulnerabilities and Exposures)* — identificador público de una vulnerabilidad conocida.

**Lockfile** — archivo que fija las versiones exactas de todas las dependencias para builds reproducibles.

**Typosquatting** — publicar un paquete malicioso con un nombre casi idéntico a uno popular.

**Cadena de suministro** *(Supply chain)* — el conjunto de componentes de terceros de los que depende tu software.

:::info Referencias primarias
- [OWASP Top 10 — A06 Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/)
- [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/) — herramienta de SCA open source.
- [CVE Program](https://www.cve.org/) — catálogo público de vulnerabilidades.
- [GitHub Dependabot](https://docs.github.com/en/code-security/dependabot) — análisis y actualización automática.
:::

---

<div className="agent-block">

### Bloque estructurado para agentes

**Objetivo:** encontrar y remediar dependencias vulnerables en toda la cadena.

**Entradas:**
- Manifiestos de dependencias y lockfiles.
- Salida de `dotnet list package --vulnerable`, `npm audit` o SCA.
- Árbol completo de dependencias, incluidas transitivas.

**Pasos:**
1. Ejecutar SCA incluyendo dependencias transitivas.
2. Confirmar el impacto real de cada alerta.
3. Actualizar a una versión segura, o sustituir la librería.
4. Documentar excepciones con dueño y fecha si no hay alternativa.
5. Integrar SCA al pipeline con un quality gate.
6. Fijar versiones con lockfile y planificar actualizaciones frecuentes.

**Salidas:**
- Sin dependencias con vulnerabilidades críticas.
- Excepciones trazables y pipeline que verifica cada cambio.

**Errores comunes:**
- Revisar solo dependencias directas.
- Aceptar alertas sin evaluar impacto.
- Dejar excepciones temporales sin seguimiento.

**Referencias cruzadas:**
- [1.3.5 SAST y SCA en la fase de validación](../fundamentos-sonarqube/05-sast-y-sca-en-validacion.md)
- [1.6.8 Del hallazgo a la corrección](./08-del-hallazgo-a-la-correccion.md)
</div>

---

<AuthorCredit />
