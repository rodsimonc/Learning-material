import requests
API = "https://jsonplaceholder.typicode.com"

r = requests.get(f"{API}/todos/1", timeout=10)
print("status:", r.status_code)          # siempre chequear el status
print("json:", r.json())

# crear un recurso (POST) con body JSON
nuevo = {"title": "estudiar APIs", "completed": False, "userId": 1}
r = requests.post(f"{API}/posts", json=nuevo, timeout=10)
print("POST status:", r.status_code)
print("creado:", r.json())
