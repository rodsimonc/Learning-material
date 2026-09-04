---
sidebar_position: 4
title: Cross-Site Scripting (XSS)
sidebar_label: 1.6.3 Cross-Site Scripting (XSS)
---

# Cross-Site Scripting (XSS)

Si la inyección SQL mete código en la base de datos, el XSS mete código en el navegador de otros usuarios. Ocurre cuando la aplicación muestra un dato aportado por el usuario sin limpiarlo, y ese dato contiene JavaScript que se ejecuta en la sesión de quien lo ve. Es especialmente relevante en las **SPAs** que consumen la API del bootcamp.

## Cómo encontrarlo

### Prueba dinámica

La prueba consiste en introducir una marca inofensiva en cada campo que después se muestra en pantalla, y ver si se ejecuta o se muestra como texto. Una marca segura y visible:

```html
<b>prueba123</b>
```

Si el texto aparece en **negrita**, la aplicación interpretó el HTML: la salida no está escapada y es vulnerable. Si aparece literal (`<b>prueba123</b>`), está escapando bien. La confirmación clásica sin causar daño usa una etiqueta que produce un efecto visible controlado por ti, en tu propia sesión de prueba.

Los lugares a revisar son todos los que reflejan input: campos de perfil, comentarios, resultados de búsqueda que repiten el término, mensajes de error que incluyen lo que escribiste, y parámetros de la URL que la página muestra.

### Revisión de código

En el frontend, busca dónde se inserta contenido dinámico como HTML crudo en lugar de texto:

```javascript
// Vulnerable: interpreta el contenido como HTML y ejecuta cualquier script.
elemento.innerHTML = comentario;
```

En React y frameworks similares, la marca de alarma es el uso explícito de inserción de HTML sin sanitizar (`dangerouslySetInnerHTML`). El nombre lo dice.

## Qué peligro implica

El script inyectado se ejecuta con los permisos de la víctima, dentro de su sesión. Eso permite:

- **Robar la sesión:** leer cookies o tokens accesibles a JavaScript y enviarlos a un servidor del atacante, para luego suplantar a la víctima.
- **Ejecutar acciones en nombre de la víctima:** hacer requests a la API como si fuera ella (cambiar su correo, hacer una transferencia).
- **Modificar la página** que ve la víctima: inyectar un formulario de login falso, redirigir a un sitio malicioso.
- **Propagarse:** en un XSS almacenado (por ejemplo en un comentario), cada persona que abre la página queda afectada.

El XSS almacenado, que queda guardado en la base y se sirve a todos, es el más grave; el reflejado, que viaja en un enlace, requiere que la víctima haga clic.

## Cómo corregirlo

La defensa central es **escapar la salida según su contexto**: convertir los caracteres especiales del HTML en texto inofensivo, de modo que el navegador los muestre en lugar de ejecutarlos.

```javascript
// Seguro: inserta como texto; el navegador nunca lo ejecuta.
elemento.textContent = comentario;
```

La buena noticia es que los frameworks modernos escapan por defecto. En React, `{comentario}` dentro del JSX se escapa automáticamente; solo te expones si fuerzas la inserción de HTML crudo. Mientras uses el renderizado normal del framework, estás cubierto.

Cuando de verdad necesitas mostrar HTML enviado por el usuario (un editor de texto enriquecido, por ejemplo), no lo insertes directo: **sanitízalo** con una librería probada como [DOMPurify](https://github.com/cure53/DOMPurify), que quita las etiquetas y atributos peligrosos y deja el resto.

### Defensa en profundidad

- **Content-Security-Policy (CSP):** una cabecera que limita desde dónde puede cargar y ejecutar scripts la página. Aunque se cuele un XSS, la CSP puede impedir que el script haga algo útil. Se cubre en [Configuración, secretos y cabeceras](./06-configuracion-secretos-cabeceras.md).
- **Cookies `HttpOnly`:** una cookie de sesión marcada `HttpOnly` no es accesible a JavaScript, así que un XSS no puede robarla. Es justo el patrón que recomienda el módulo de [autenticación en APIs REST](../capacitacion-servicios-web-api-rest/04-autenticacion-autorizacion-rest.md) para entregar el token.
- **Escapar en el contexto correcto:** el escape para HTML, para un atributo, para una URL y para JavaScript son distintos. Apóyate en el framework en lugar de escapar a mano.

## Resumen para agentes

- **Objetivo:** evitar que input del usuario se ejecute como script en el navegador de otros.
- **Entradas comunes:** campos que se reflejan en la interfaz, código de renderizado del frontend, parámetros de URL mostrados.
- **Controles clave:** escape de salida por contexto, renderizado seguro del framework, sanitización con DOMPurify, CSP, cookies HttpOnly.
- **Salidas esperadas:** input mostrado como texto literal, no interpretado como HTML.
- **Errores frecuentes:** usar `innerHTML`/`dangerouslySetInnerHTML` con input, sanitizar en el contexto equivocado, guardar el token en `localStorage` (accesible a XSS).

## Glosario

**XSS** *(Cross-Site Scripting)* — inyección de JavaScript malicioso que se ejecuta en el navegador de otros usuarios por no escapar la salida.

**XSS almacenado** *(Stored XSS)* — el script queda guardado (por ejemplo en un comentario) y afecta a todos los que lo ven.

**XSS reflejado** *(Reflected XSS)* — el script viaja en un enlace y se ejecuta cuando la víctima lo abre.

**Escapar** *(Escaping / output encoding)* — convertir caracteres especiales en texto inofensivo para que no se interpreten como código.

**Sanitizar** *(Sanitizing)* — limpiar HTML del usuario quitando etiquetas y atributos peligrosos.

**CSP** *(Content-Security-Policy)* — cabecera que limita qué scripts puede cargar y ejecutar una página.

:::info Referencias primarias
- [OWASP Top 10 — A03 Injection](https://owasp.org/Top10/A03_2021-Injection/) — el XSS entra en esta categoría.
- [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html) — guía de remediación por contexto.
- [CWE-79](https://cwe.mitre.org/data/definitions/79.html) — Improper Neutralization of Input During Web Page Generation.
- [DOMPurify](https://github.com/cure53/DOMPurify) — sanitización de HTML en el navegador.
:::

---

<div className="agent-block">

### Bloque estructurado para agentes

**Objetivo:** encontrar y corregir XSS en la interfaz que consume la API.

**Entradas:**
- Campos de entrada que se reflejan en la interfaz.
- Código de renderizado del frontend.
- Parámetros de URL que la página muestra.

**Pasos:**
1. Introducir una marca HTML inofensiva en cada campo reflejado y ver si se ejecuta.
2. Revisar el código en busca de inserción de HTML crudo con input.
3. Sustituir por renderizado de texto seguro del framework.
4. Sanitizar con DOMPurify solo cuando haya que mostrar HTML del usuario.
5. Añadir CSP y servir el token en cookie HttpOnly.
6. Verificar que la marca de prueba aparece como texto, no ejecutada.

**Salidas:**
- Salida escapada o sanitizada en todos los puntos que reflejan input.
- CSP configurada y token fuera del alcance de JavaScript.

**Errores comunes:**
- Insertar input con `innerHTML` o `dangerouslySetInnerHTML`.
- Guardar el token de sesión en `localStorage`.
- Escapar en el contexto equivocado.

**Referencias cruzadas:**
- [1.6.6 Configuración, secretos y cabeceras](./06-configuracion-secretos-cabeceras.md)
- [1.1.4 Autenticación y Autorización en APIs RESTful](../capacitacion-servicios-web-api-rest/04-autenticacion-autorizacion-rest.md)
</div>

---

<AuthorCredit />
