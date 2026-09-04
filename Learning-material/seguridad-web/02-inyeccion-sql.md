---
sidebar_position: 3
title: Inyección SQL
sidebar_label: 1.6.2 Inyección SQL
---

# Inyección SQL

La inyección SQL sigue siendo una de las vulnerabilidades más frecuentes y más dañinas, y es de las más fáciles de encontrar y de corregir. Ocurre cuando un valor que aporta el usuario termina formando parte del texto de una consulta SQL, y ese valor se interpreta como código en lugar de como dato.

:::info Ver también
Este módulo se enfoca en **encontrar** la vulnerabilidad y entender su impacto. La conversión detallada a consultas parametrizadas en PL/SQL, Java y .NET, y la verificación con evidencia, están en [Consultas parametrizadas en migraciones legacy](../modernizacion-legacy/05-consultas-parametrizadas-en-migracion.md).
:::

## Cómo encontrarla

### Revisión de código (SAST y manual)

El patrón se reconoce a simple vista: una consulta construida concatenando o interpolando un valor de entrada.

```csharp
// Patrón vulnerable en .NET: el valor de 'nombre' se pega al texto del query.
var sql = "SELECT * FROM Usuarios WHERE Nombre = '" + nombre + "'";
var usuarios = conexion.Query<Usuario>(sql);
```

SonarQube y otros SAST marcan este patrón automáticamente. En revisión manual, busca la concatenación de strings (`+`, `||`, interpolación `$"..."`, `String.Format`) alrededor de palabras como `SELECT`, `INSERT`, `WHERE`, `EXECUTE IMMEDIATE`.

### Prueba dinámica

En la aplicación en ejecución, la prueba clásica es introducir una comilla simple en un campo que probablemente llega a una consulta:

```
'
```

Si la respuesta cambia a un error de base de datos, un error 500, o un comportamiento anómalo, la comilla rompió la sintaxis del query: señal fuerte de que el input llega sin parametrizar. La confirmación se hace con una entrada que altera la lógica sin causar daño, como una condición siempre verdadera en un campo de búsqueda:

```
' OR '1'='1
```

Si eso devuelve más resultados de los que debería (o todos), la estructura del query cambió por el input. Esa es la prueba de concepto: no hace falta ir más lejos para confirmar el hallazgo.

## Qué peligro implica

La inyección SQL le da al atacante control sobre la consulta, y a través de ella, sobre la base de datos. Según el caso puede permitir:

- **Leer datos ajenos:** saltarse un `WHERE` y extraer toda una tabla, incluidos datos de otros usuarios.
- **Saltear la autenticación:** un `' OR '1'='1` en un login puede hacer que la consulta devuelva un usuario válido sin contraseña correcta.
- **Modificar o borrar datos:** en los casos más graves, ejecutar `UPDATE` o `DELETE` no previstos.
- **Extraer el esquema completo** de la base, e incluso, en configuraciones débiles, ejecutar comandos en el servidor.

Es una vulnerabilidad de severidad alta o crítica casi siempre, porque compromete la confidencialidad y la integridad de todos los datos, no solo los de un usuario.

## Cómo corregirla

La corrección es una sola idea: **el texto del query y los valores viajan por canales separados**. La consulta lleva un marcador de parámetro, y el driver envía los valores aparte. Así el valor nunca se interpreta como SQL.

```csharp
// Seguro (ADO.NET / Dapper): el valor viaja como parámetro, no como texto.
var sql = "SELECT * FROM Usuarios WHERE Nombre = @nombre";
var usuarios = conexion.Query<Usuario>(sql, new { nombre });
```

```csharp
// Seguro (Entity Framework): LINQ parametriza automáticamente.
var usuarios = contexto.Usuarios
    .Where(u => u.Nombre == nombre)
    .ToList();
```

Con la versión segura, el input `' OR '1'='1` se busca como un nombre de usuario literal: no encuentra nada y el ataque deja de existir como vector.

:::tip Casos que parecen no admitir parámetros
Tres situaciones confunden: ordenar por una columna dinámica (`ORDER BY`), listas variables (`IN (...)`) y comodines de `LIKE`. Ninguna justifica volver a concatenar input crudo. El módulo de [consultas parametrizadas](../modernizacion-legacy/05-consultas-parametrizadas-en-migracion.md) muestra el patrón correcto para cada una (lista blanca para nombres de columna, parámetros expandidos para `IN`, escape de comodines para `LIKE`).
:::

### Defensa en profundidad

La parametrización resuelve la raíz. Sobre ella se suman capas:

- **Usar un ORM** (Entity Framework) que parametriza por defecto, reservando el SQL crudo para casos justificados.
- **Mínimo privilegio en la base:** el usuario de la aplicación solo tiene los permisos que necesita, así una inyección hace menos daño.
- **Validación de entrada** por tipo y formato, como filtro adicional (nunca como reemplazo de la parametrización).

## Resumen para agentes

- **Objetivo:** detectar y eliminar la inyección SQL parametrizando toda consulta que reciba input.
- **Entradas comunes:** código de acceso a datos, hallazgos de SAST, endpoints con parámetros que llegan a la base.
- **Controles clave:** consultas parametrizadas, uso de ORM, mínimo privilegio, validación de entrada.
- **Salidas esperadas:** consultas sin concatenación de input, prueba de que `' OR '1'='1` ya no altera resultados.
- **Errores frecuentes:** concatenar en casos "especiales" (`ORDER BY`, `IN`, `LIKE`), confiar en escapar a mano, validar solo en el frontend.

## Glosario

**Inyección SQL** *(SQL injection, SQLi)* — vulnerabilidad donde input del usuario se interpreta como código SQL por haberse concatenado al texto de la consulta.

**Consulta parametrizada** *(Parameterized query)* — sentencia donde el texto y los valores viajan por canales separados mediante marcadores.

**ORM** *(Object-Relational Mapping)* — capa que traduce objetos del lenguaje a SQL y parametriza por defecto (por ejemplo Entity Framework).

**Mínimo privilegio** *(Least privilege)* — dar a cada componente solo los permisos que necesita.

:::info Referencias primarias
- [OWASP Top 10 — A03 Injection](https://owasp.org/Top10/A03_2021-Injection/) — categoría de referencia.
- [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) — guía de remediación.
- [CWE-89](https://cwe.mitre.org/data/definitions/89.html) — Improper Neutralization of Special Elements used in an SQL Command.
:::

---

<div className="agent-block">

### Bloque estructurado para agentes

**Objetivo:** encontrar y corregir inyección SQL en la capa de acceso a datos.

**Entradas:**
- Código que construye consultas SQL.
- Hallazgos de SAST relacionados con inyección.
- Endpoints cuyos parámetros llegan a la base de datos.
- Conocimiento de qué valores provienen del usuario.

**Pasos:**
1. Buscar concatenación o interpolación de input dentro de sentencias SQL.
2. Confirmar en ejecución con una comilla y una condición siempre verdadera, en alcance autorizado.
3. Convertir la consulta a parametrizada o a LINQ/ORM.
4. Aplicar el patrón correcto a `ORDER BY`, `IN` y `LIKE`.
5. Reducir privilegios del usuario de base de datos.
6. Verificar que la prueba de concepto ya no altera resultados.

**Salidas:**
- Consultas sin input concatenado.
- Evidencia de remediación reproducible.

**Errores comunes:**
- Reintroducir concatenación en casos "que no se pueden parametrizar".
- Escapar comillas a mano en lugar de parametrizar.
- Validar solo en el frontend.

**Referencias cruzadas:**
- [1.4.5 Consultas parametrizadas en migraciones](../modernizacion-legacy/05-consultas-parametrizadas-en-migracion.md)
- [1.3.5 SAST y SCA en la fase de validación](../fundamentos-sonarqube/05-sast-y-sca-en-validacion.md)
</div>

---

<AuthorCredit />
