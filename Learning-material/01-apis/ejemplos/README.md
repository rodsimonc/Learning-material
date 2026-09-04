# Ejemplos de API — código testeado

Código de acompañamiento del libro "APIs de 0 a producción".
Cada carpeta tiene un servidor y un cliente mínimos, en Python y en Node.
Todo esto se ejecutó de verdad; en `out/` está la salida real capturada.

## Requisitos
- Python 3.11+  ->  `pip install fastapi "uvicorn[standard]" httpx requests "strawberry-graphql[fastapi]" grpcio grpcio-tools websockets flask zeep lxml`
- Node 18+      ->  `npm install` (dentro de esta carpeta)

## Cómo correr cada uno

### REST
- Python: `uvicorn --app-dir rest main:app --port 8001`  y en otra terminal: `curl http://127.0.0.1:8001/usuarios/42`
- Node:   `node rest/server.js`  (puerto 8002)

### GraphQL
- Python: `uvicorn --app-dir graphql app:app --port 8003`  -> POST a /graphql
- Node:   `node graphql/server.js`  (puerto 8004)

### gRPC
- Generar stubs Python: `cd grpc && python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. usuarios.proto`
- Python: `python grpc/server.py` (9001) + `python grpc/client.py`
- Node:   `node grpc/server.js` (9002) + `node grpc/client.js`

### WebSockets
- Python: `python websockets/server.py` (9101) + `python websockets/client.py`
- Node:   `node websockets/server.js` (9102) + `node websockets/client.js`

### Webhooks
- Python: `uvicorn --app-dir webhooks receiver:app --port 8005` + `python webhooks/sender.py`
- Node:   `node webhooks/receiver.js` (8006) + `node webhooks/sender.js`

### SOAP
- Node server + Python client (cross-language): `node soap/server.js` (8007) + `python soap/client.py`
- Cliente Node: `node soap/client.js`

### Consumir una API pública real
- `python real/consume.py`  y  `node real/consume.js`  (usan jsonplaceholder.typicode.com)

Los puertos están elegidos para no chocar entre sí.
