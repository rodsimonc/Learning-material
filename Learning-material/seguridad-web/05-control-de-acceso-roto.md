---
sidebar_position: 6
title: Control de acceso roto
sidebar_label: 1.6.5 Control de acceso roto
---

# Control de acceso roto

El control de acceso roto es la categoría número uno del OWASP Top 10, y la más difícil de detectar con herramientas automáticas, porque depende de la lógica de negocio. Ocurre cuando un usuario autenticado accede a datos o acciones que no le corresponden. Autenticarse (saber quién sos) no es lo mismo que autorizar (verificar qué podés hacer), y este es el módulo de la segunda.

## Cómo encontrarlo

Es una revisión sobre todo manual, porque solo una persona sabe qué debería poder hacer cada rol. La técnica central es probar cada acción **como un usuario que no debería poder hacerla**.

### IDOR: el identificador que se cambia a mano

El caso más frecuente. La aplicación muestra un recurso por su identificador en la URL o el cuerpo:

```
GET /api/facturas/42
```

La prueba: cambiar el `42` por el identificador de un recurso de **otro** usuario y ver si la API lo devuelve.

```
GET /api/facturas/43
```

Si devuelve la factura 43 sin verificar que sea tuya, hay un IDOR (*Insecure Direct Object Reference*), también llamado BOLA (*Broken Object Level Authorization*). Se prueba con dos cuentas de prueba: entras con una, y pides recursos de la otra.

### Otras pruebas de acceso

- **Escalada horizontal:** acceder a datos de otro usuario del mismo nivel (el IDOR de arriba).
- **Escalada vertical:** un usuario común accede a funciones de administrador. Prueba a llamar directamente los endpoints de admin con una cuenta común, sin pasar por el menú que los oculta.
- **Métodos y campos:** si puedes leer un recurso, prueba si también puedes modificarlo o borrarlo (`PUT`, `DELETE`) sin ser el dueño. Prueba enviar campos que no deberías poder cambiar (por ejemplo `rol: "admin"` en tu propio perfil).
- **Forzar la navegación:** pedir directamente una URL a la que el frontend no te deja llegar. Esconder el botón no protege el endpoint.

## Qué peligro implica

El impacto es directo sobre la confidencialidad y la integridad de los datos de todos:

- **Fuga masiva de datos:** un IDOR en un endpoint que se recorre por identificador permite extraer los recursos de todos los usuarios, uno por uno.
- **Modificación no autorizada:** editar o borrar datos ajenos.
- **Toma de control:** una escalada vertical convierte a un usuario común en administrador.

Como estas fallas no rompen nada visible y las herramientas automáticas rara vez las detectan, suelen pasar a producción sin que nadie las note, hasta que alguien las aprovecha.

## Cómo corregirlo

La regla es una: **verificar la autorización en el servidor, en cada operación, contra el usuario autenticado y el recurso concreto.** No alcanza con saber que el usuario está logueado; hay que verificar que tiene permiso sobre *ese* recurso.

```csharp
// Vulnerable: devuelve la factura sin verificar de quién es.
[HttpGet("api/facturas/{id}")]
public async Task<IActionResult> GetFactura(int id)
{
    var factura = await _repo.ObtenerFactura(id);
    return Ok(factura);
}

// Seguro: verifica que la factura pertenezca al usuario autenticado.
[HttpGet("api/facturas/{id}")]
[Authorize]
public async Task<IActionResult> GetFactura(int id)
{
    var usuarioId = User.FindFirst(ClaimTypes.NameIdentifier)!.Value;
    var factura = await _repo.ObtenerFactura(id);
    if (factura is null || factura.UsuarioId != usuarioId)
        return Forbid();          // 403: sé quién sos, pero no es tuya
    return Ok(factura);
}
```

### Principios que sostienen la corrección

- **Negar por defecto.** El acceso empieza cerrado y se abre explícitamente. Así, un endpoint nuevo sin regla queda protegido, no expuesto.
- **Verificar en el servidor, siempre.** El frontend puede ocultar opciones por comodidad, pero la decisión de acceso vive en el backend, en cada endpoint.
- **Autorización a nivel de objeto.** No basta con "este rol puede ver facturas"; hay que verificar "esta factura es de este usuario".
- **Centralizar la lógica** de autorización (políticas, filtros, middlewares) para no depender de que cada endpoint la repita bien. En ASP.NET Core, las *authorization policies* ayudan a esto.

## Resumen para agentes

- **Objetivo:** garantizar que cada usuario solo acceda a los datos y acciones que le corresponden.
- **Entradas comunes:** endpoints con identificadores de recurso, definición de roles, dos cuentas de prueba.
- **Controles clave:** verificación de propiedad por recurso, negar por defecto, autorización en el servidor, políticas centralizadas.
- **Salidas esperadas:** endpoints que devuelven 403 ante accesos ajenos, campos sensibles no modificables por el titular.
- **Errores frecuentes:** confiar en que el frontend oculta la opción, verificar solo autenticación y no propiedad, dejar endpoints de admin sin protección directa.

## Glosario

**Control de acceso** *(Access control)* — conjunto de reglas que determinan qué puede hacer cada usuario.

**Autorización** *(Authorization)* — verificar qué permisos tiene un usuario ya autenticado.

**IDOR / BOLA** *(Insecure Direct Object Reference / Broken Object Level Authorization)* — acceder a un recurso ajeno cambiando su identificador.

**Escalada horizontal** *(Horizontal privilege escalation)* — acceder a datos de otro usuario del mismo nivel.

**Escalada vertical** *(Vertical privilege escalation)* — obtener permisos de un rol superior.

**Negar por defecto** *(Deny by default)* — el acceso está cerrado salvo que una regla lo abra.

:::info Referencias primarias
- [OWASP Top 10 — A01 Broken Access Control](https://owasp.org/Top10/A01_2021-Broken_Access_Control/)
- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
- [CWE-639](https://cwe.mitre.org/data/definitions/639.html) — Authorization Bypass Through User-Controlled Key.
- [OWASP API Security Top 10 — API1 BOLA](https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/)
:::

---

<div className="agent-block">

### Bloque estructurado para agentes

**Objetivo:** encontrar y corregir fallas de autorización a nivel de recurso y de rol.

**Entradas:**
- Endpoints que reciben identificadores de recurso.
- Definición de roles y permisos.
- Dos o más cuentas de prueba de distinto nivel.

**Pasos:**
1. Con dos cuentas, pedir recursos de una desde la otra para detectar IDOR.
2. Llamar endpoints de administrador con una cuenta común (escalada vertical).
3. Probar métodos de escritura y campos sensibles sobre recursos ajenos.
4. Añadir verificación de propiedad y rol en el servidor, en cada operación.
5. Aplicar negar por defecto y centralizar la autorización en políticas.
6. Verificar que los accesos ajenos devuelven 403.

**Salidas:**
- Endpoints con verificación de propiedad por recurso.
- Accesos no autorizados rechazados de forma consistente.

**Errores comunes:**
- Verificar autenticación pero no propiedad del recurso.
- Confiar en que el frontend oculta la acción.
- Dejar endpoints administrativos accesibles directamente.

**Referencias cruzadas:**
- [1.1.4 Autenticación y Autorización en APIs RESTful](../capacitacion-servicios-web-api-rest/04-autenticacion-autorizacion-rest.md)
- [1.6.4 Autenticación y sesiones](./04-autenticacion-y-sesiones.md)
</div>

---

<AuthorCredit />
