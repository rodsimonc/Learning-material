---
sidebar_position: 5
title: Autenticación y sesiones
sidebar_label: 1.6.4 Autenticación y sesiones
---

# Autenticación y sesiones

La autenticación decide quién entra. Cuando falla, un atacante entra como otro sin ser ese otro. Este módulo enseña a encontrar las debilidades más comunes en el login y el manejo de sesiones, y a corregirlas.

:::info Ver también
Los mecanismos de autenticación y autorización en APIs (Basic, tokens, JWT, entrega por cookie `HttpOnly`) están desarrollados en [Autenticación y Autorización en APIs RESTful](../capacitacion-servicios-web-api-rest/04-autenticacion-autorizacion-rest.md). Aquí nos enfocamos en **encontrar** dónde ese esquema se implementó de forma débil.
:::

## Cómo encontrar debilidades

La revisión de autenticación es sobre todo de código y configuración. Las preguntas que la guían:

- **¿Cómo se guardan las contraseñas?** Busca en el registro de usuarios cómo se persiste la contraseña. Si ves la contraseña en texto plano, o un hash rápido como `MD5` o `SHA1` sin sal, hay un hallazgo.
- **¿Hay límite de intentos?** Prueba varios logins fallidos seguidos contra tu entorno de prueba. Si no aparece bloqueo ni demora, el login es vulnerable a fuerza bruta.
- **¿Dónde vive el token en el navegador?** En las DevTools, mira si el token de sesión está en `localStorage` (accesible a JavaScript, y por tanto robable con XSS) o en una cookie `HttpOnly`.
- **¿El token expira y se puede invalidar?** Revisa si el JWT tiene expiración (`exp`) y si existe forma de cerrar sesión de verdad.
- **¿Se filtra información en los errores?** Un mensaje "usuario no existe" distinto de "contraseña incorrecta" le dice al atacante qué usuarios son válidos.

## Qué peligro implica

Una autenticación débil compromete cuentas completas:

- **Contraseñas en texto plano o con hash débil:** si la base se filtra (ocurre seguido), las contraseñas quedan expuestas de inmediato, y como la gente reutiliza contraseñas, el daño se extiende a otros servicios.
- **Sin límite de intentos:** un atacante prueba millones de combinaciones hasta entrar (fuerza bruta o *credential stuffing* con contraseñas filtradas de otros sitios).
- **Token accesible a JavaScript:** un XSS (módulo anterior) roba la sesión y suplanta al usuario.
- **Enumeración de usuarios:** mensajes de error distintos revelan qué cuentas existen, el primer paso de un ataque dirigido.

## Cómo corregirlo

### Guardar contraseñas correctamente

Nunca se guarda la contraseña: se guarda un **hash con sal** generado por un algoritmo lento, diseñado para resistir fuerza bruta. En .NET, ASP.NET Core Identity usa PBKDF2 por defecto; también son adecuados **bcrypt**, **argon2** y **scrypt**.

```csharp
// Con ASP.NET Core Identity el hashing seguro es el comportamiento por defecto.
var resultado = await _userManager.CreateAsync(usuario, password);
```

La **sal** es un valor aleatorio único por usuario que se agrega antes de hashear: hace que dos personas con la misma contraseña tengan hashes distintos y arruina las tablas precalculadas (*rainbow tables*). Los algoritmos mencionados la incorporan solos.

:::warning Nunca uses MD5 o SHA1 para contraseñas
Son rápidos, y esa velocidad es justo lo que un atacante necesita para probar miles de millones de combinaciones. Para contraseñas se usan algoritmos lentos a propósito. Y jamás inventes tu propio esquema de hashing.
:::

### Endurecer el login y la sesión

- **Límite de intentos** (*rate limiting*) y bloqueo temporal tras varios fallos. ASP.NET Core Identity trae *lockout* configurable.
- **Segundo factor (2FA)** para cuentas sensibles.
- **Token en cookie `HttpOnly; Secure; SameSite`**, fuera del alcance de JavaScript, como recomienda el módulo de APIs REST.
- **Expiración corta del token** y un mecanismo de renovación e invalidación (cierre de sesión real).
- **Mensajes de error genéricos:** "usuario o contraseña incorrectos", igual exista o no el usuario, para no filtrar cuáles son válidos.
- **Exigir contraseñas razonables** y contrastarlas contra listas de las más filtradas.

## Resumen para agentes

- **Objetivo:** que solo el titular legítimo pueda autenticarse y mantener su sesión.
- **Entradas comunes:** código de registro y login, configuración de identidad, ubicación del token en el cliente.
- **Controles clave:** hashing lento con sal, rate limiting y lockout, 2FA, token en cookie HttpOnly, expiración e invalidación, errores genéricos.
- **Salidas esperadas:** contraseñas con hash seguro, login protegido contra fuerza bruta, token no accesible a JavaScript.
- **Errores frecuentes:** MD5/SHA1 o texto plano, sin límite de intentos, token en `localStorage`, errores que revelan usuarios válidos.

## Glosario

**Hash** *(Hash)* — transformación de un solo sentido que se guarda en lugar de la contraseña.

**Sal** *(Salt)* — valor aleatorio único por usuario que se agrega antes de hashear.

**Fuerza bruta** *(Brute force)* — probar muchas combinaciones hasta acertar la contraseña.

**Credential stuffing** — probar contraseñas filtradas de otros servicios, aprovechando la reutilización.

**Rate limiting** — límite de intentos por unidad de tiempo.

**2FA** *(Two-Factor Authentication)* — segundo factor además de la contraseña.

**Enumeración de usuarios** *(User enumeration)* — deducir qué cuentas existen a partir de diferencias en las respuestas.

:::info Referencias primarias
- [OWASP Top 10 — A07 Identification and Authentication Failures](https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/)
- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [CWE-287](https://cwe.mitre.org/data/definitions/287.html) — Improper Authentication.
:::

---

<div className="agent-block">

### Bloque estructurado para agentes

**Objetivo:** encontrar y corregir debilidades de autenticación y manejo de sesión.

**Entradas:**
- Código de registro, login y cierre de sesión.
- Configuración de identidad y de tokens.
- Ubicación del token en el navegador.

**Pasos:**
1. Revisar cómo se almacenan las contraseñas y sustituir hash débil por PBKDF2/bcrypt/argon2.
2. Probar fuerza bruta en entorno autorizado y añadir rate limiting y lockout.
3. Mover el token a una cookie HttpOnly; Secure; SameSite.
4. Configurar expiración e invalidación de sesión.
5. Unificar los mensajes de error de login para no enumerar usuarios.
6. Ofrecer 2FA en cuentas sensibles.

**Salidas:**
- Contraseñas con hash lento y sal.
- Login resistente a fuerza bruta y token protegido.

**Errores comunes:**
- Hash rápido (MD5/SHA1) o texto plano.
- Token en `localStorage`.
- Errores de login que revelan si el usuario existe.

**Referencias cruzadas:**
- [1.1.4 Autenticación y Autorización en APIs RESTful](../capacitacion-servicios-web-api-rest/04-autenticacion-autorizacion-rest.md)
- [1.6.3 Cross-Site Scripting (XSS)](./03-xss.md)
- [1.6.5 Control de acceso roto](./05-control-de-acceso-roto.md)
</div>

---

<AuthorCredit />
