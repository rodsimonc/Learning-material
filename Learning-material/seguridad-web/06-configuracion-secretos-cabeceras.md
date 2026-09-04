---
sidebar_position: 7
title: Configuración, secretos y cabeceras
sidebar_label: 1.6.6 Configuración, secretos y cabeceras
---

# Configuración, secretos y cabeceras

Muchas brechas no vienen de un error en el código, sino de cómo está configurado el sistema: un secreto en el repositorio, un mensaje de error que revela de más, o cabeceras de seguridad ausentes. Es la categoría de **configuración de seguridad incorrecta**, y suele ser de las más rápidas de encontrar y corregir.

## Cómo encontrarlo

### Secretos expuestos

- **Busca en el repositorio** claves, tokens y contraseñas escritos en el código o en archivos de configuración versionados. Patrones como `password =`, `apikey`, `secret`, `connectionstring` con credenciales reales. Hay bots que escanean GitHub buscando justo esto en segundos.
- **Revisa el historial de Git**, no solo el estado actual: un secreto borrado en un commit posterior sigue en la historia.
- **Confirma que existe un `.gitignore`** que excluye `.env`, `appsettings.*.json` con secretos y equivalentes.

### Errores que revelan de más

Provoca un error (una entrada inválida, un tipo equivocado) y mira la respuesta. Si devuelve un *stack trace* completo, la versión del framework, rutas internas o la consulta SQL, la aplicación está filtrando información útil para un atacante.

### Cabeceras de seguridad

Con las DevTools o `curl -I`, revisa las cabeceras de respuesta. La ausencia de las cabeceras de seguridad (abajo) es un hallazgo. Revisa también si el sitio fuerza HTTPS o acepta HTTP plano.

### CORS permisivo

Busca en la configuración un CORS que permita cualquier origen (`Access-Control-Allow-Origin: *`) en una API con datos privados. Deja que cualquier sitio consuma tu API desde el navegador de tus usuarios.

## Qué peligro implica

- **Secreto filtrado:** acceso directo a la base, a servicios de terceros o a la infraestructura, según qué credencial sea. Es de los incidentes más comunes y más caros.
- **Errores verbosos:** le dan al atacante el mapa del sistema (versiones con CVE conocidos, estructura de la base, rutas internas) para afinar su ataque.
- **Cabeceras ausentes:** dejan al navegador sin las defensas que podrían frenar XSS, *clickjacking* o degradación a HTTP.
- **CORS abierto:** habilita que un sitio malicioso lea respuestas de tu API con la sesión de la víctima.

## Cómo corregirlo

### Secretos fuera del código

Los secretos viven fuera del repositorio: en variables de entorno, en el gestor de secretos del proveedor, o en los *secrets* del pipeline (ver [CI/CD y SAST/SCA](../fundamentos-sonarqube/04-ciclo-devops.md)).

```csharp
// Vulnerable: secreto hardcodeado.
var connString = "Server=...;Password=SuperSecreta123;";

// Seguro: viene de la configuración/entorno, nunca del código.
var connString = builder.Configuration.GetConnectionString("Default");
```

:::warning Si un secreto se filtró, rótalo
La primera acción no es borrarlo del código: es **rotarlo** (generar uno nuevo e invalidar el viejo). Mientras el viejo siga activo, no importa que lo hayas quitado del repositorio; quien ya lo copió lo tiene.
:::

### Errores discretos

En producción, nunca muestres *stack traces* al cliente. Registra el detalle del error en tus logs internos y devuelve al usuario un mensaje genérico con un identificador de correlación. En ASP.NET Core, usa el *exception handler* de producción, no la página de desarrollo.

### Cabeceras de seguridad

Unas pocas cabeceras suben mucho la defensa. Se pueden agregar con middleware:

| Cabecera | Qué hace |
|---|---|
| `Strict-Transport-Security` | Obliga al navegador a usar siempre HTTPS. |
| `Content-Security-Policy` | Limita de dónde se cargan y ejecutan scripts. Defensa clave contra XSS. |
| `X-Content-Type-Options: nosniff` | Evita que el navegador adivine el tipo de un archivo. |
| `X-Frame-Options` | Impide que tu sitio se embeba en un iframe ajeno (clickjacking). |

### CORS restringido

```csharp
// Seguro: solo el frontend legítimo puede consumir la API desde el navegador.
builder.Services.AddCors(o => o.AddPolicy("frontend", p =>
    p.WithOrigins("https://miapp.com").AllowAnyMethod().AllowAnyHeader()));
```

Nunca uses `AllowAnyOrigin` en una API con datos privados.

### Endurecimiento general

- **HTTPS forzado** con redirección de HTTP y HSTS.
- **Deshabilitar lo que no se usa:** endpoints de diagnóstico, cuentas por defecto, directorios listables.
- **Mantener actualizados** framework y servidor (los CVE conocidos se explotan primero).

## Resumen para agentes

- **Objetivo:** cerrar las brechas de configuración: secretos, errores verbosos, cabeceras y CORS.
- **Entradas comunes:** repositorio y su historial, respuestas de error, cabeceras HTTP, configuración de CORS y de HTTPS.
- **Controles clave:** secretos en entorno, rotación ante filtración, errores genéricos, cabeceras de seguridad, CORS restringido, HTTPS forzado.
- **Salidas esperadas:** repositorio sin secretos, errores discretos, cabeceras presentes, CORS acotado.
- **Errores frecuentes:** hardcodear secretos, mostrar stack traces en producción, `AllowAnyOrigin`, olvidar rotar un secreto filtrado.

## Glosario

**Configuración de seguridad incorrecta** *(Security misconfiguration)* — riesgos que nacen de cómo está configurado el sistema, no del código.

**Secreto** *(Secret)* — credencial sensible: clave, token, contraseña, cadena de conexión.

**Rotar** *(Rotate)* — reemplazar un secreto por uno nuevo e invalidar el anterior.

**Cabecera de seguridad** *(Security header)* — cabecera HTTP que instruye al navegador a aplicar una defensa.

**CORS** *(Cross-Origin Resource Sharing)* — reglas de qué orígenes pueden consumir una API desde el navegador.

**Clickjacking** — engañar al usuario para que interactúe con un sitio embebido de forma oculta.

:::info Referencias primarias
- [OWASP Top 10 — A05 Security Misconfiguration](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)
- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
- [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/)
- [CWE-16](https://cwe.mitre.org/data/definitions/16.html) — Configuration.
:::

---

<div className="agent-block">

### Bloque estructurado para agentes

**Objetivo:** encontrar y corregir errores de configuración de seguridad.

**Entradas:**
- Repositorio y su historial de Git.
- Respuestas de error de la aplicación.
- Cabeceras HTTP de respuesta.
- Configuración de CORS, HTTPS y del servidor.

**Pasos:**
1. Escanear el repositorio y su historial en busca de secretos.
2. Mover los secretos a variables de entorno o gestor de secretos; rotar los filtrados.
3. Configurar errores genéricos en producción con logging interno.
4. Añadir las cabeceras de seguridad por middleware.
5. Restringir CORS a los orígenes legítimos y forzar HTTPS.
6. Verificar con `curl -I` y provocando un error controlado.

**Salidas:**
- Repositorio sin secretos y secretos rotados.
- Cabeceras de seguridad presentes y CORS acotado.

**Errores comunes:**
- Hardcodear secretos o dejarlos en el historial.
- Exponer stack traces en producción.
- `AllowAnyOrigin` en APIs con datos privados.

**Referencias cruzadas:**
- [1.6.3 Cross-Site Scripting (XSS)](./03-xss.md)
- [1.6.7 Dependencias vulnerables](./07-dependencias-vulnerables.md)
- [1.3.4 Integración de SonarQube en el ciclo DevOps](../fundamentos-sonarqube/04-ciclo-devops.md)
</div>

---

<AuthorCredit />
