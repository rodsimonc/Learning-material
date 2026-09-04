import asyncio, json, websockets

async def main():
    async with websockets.connect("ws://127.0.0.1:9101") as ws:
        print("<- server:", await ws.recv())          # llega solo, sin pedir
        for texto in ["hola", "como va"]:
            await ws.send(json.dumps({"tipo": "mensaje", "texto": texto}))
            print("-> yo:    ", texto)
            print("<- server:", await ws.recv())

asyncio.run(main())
