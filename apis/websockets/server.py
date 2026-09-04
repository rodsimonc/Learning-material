import asyncio, json, websockets

async def handler(ws):
    # apenas se conecta, el server EMPUJA un saludo (nadie lo pidio)
    await ws.send(json.dumps({"tipo": "bienvenida", "texto": "conectado"}))
    async for msg in ws:                      # escucha mensajes entrantes
        data = json.loads(msg)
        eco = {"tipo": "eco", "recibido": data.get("texto")}
        await ws.send(json.dumps(eco))        # responde por el mismo canal

async def main():
    async with websockets.serve(handler, "127.0.0.1", 9101):
        await asyncio.Future()

asyncio.run(main())
