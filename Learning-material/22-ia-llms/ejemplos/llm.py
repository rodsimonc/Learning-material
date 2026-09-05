"""
Integrar un LLM en una app. Agnóstico: mismos conceptos con Claude o OpenAI.
- chat: una pregunta, una respuesta
- streaming: la respuesta llega de a pedazos (como ves escribir a ChatGPT)
- function calling: el modelo pide ejecutar una función tuya
Las llamadas al LLM necesitan tu API key (variable de entorno). El RAG y el
dispatch de function calling se pueden probar sin credenciales.
"""
import os

# ---------- Chat (credential-gated) ----------
def chat_claude(mensaje: str) -> str:
    from anthropic import Anthropic
    cliente = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    r = cliente.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=500,
        messages=[{"role": "user", "content": mensaje}],
    )
    return r.content[0].text


def chat_openai(mensaje: str) -> str:
    from openai import OpenAI
    cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    r = cliente.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": mensaje}],
    )
    return r.choices[0].message.content


# ---------- Streaming (credential-gated) ----------
def chat_stream_claude(mensaje: str):
    from anthropic import Anthropic
    cliente = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    with cliente.messages.stream(
        model="claude-sonnet-4-5", max_tokens=500,
        messages=[{"role": "user", "content": mensaje}],
    ) as stream:
        for texto in stream.text_stream:
            yield texto   # cada pedazo, apenas llega


# ---------- Function calling: el dispatch (probable sin credenciales) ----------
# Definís tus herramientas; el modelo decide cuál llamar y con qué argumentos.
# Vos ejecutás la función y le devolvés el resultado. Acá probamos el dispatch.
def buscar_pedido(pedido_id: int) -> dict:
    # en real, consulta la base (librito 10)
    return {"pedido_id": pedido_id, "estado": "pagado", "total": 22600}

def stock_producto(nombre: str) -> dict:
    return {"producto": nombre, "stock": 12}

HERRAMIENTAS = {"buscar_pedido": buscar_pedido, "stock_producto": stock_producto}

def ejecutar_tool_call(nombre: str, argumentos: dict):
    """El modelo devuelve (nombre, argumentos); vos ejecutás la función real."""
    if nombre not in HERRAMIENTAS:
        return {"error": f"herramienta desconocida: {nombre}"}
    return HERRAMIENTAS[nombre](**argumentos)
