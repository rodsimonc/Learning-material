# imagen base: Python liviano
FROM python:3.11-slim

# carpeta de trabajo dentro del contenedor
WORKDIR /app

# 1) copiar SOLO las dependencias primero (aprovecha la caché de capas)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2) copiar el resto del código
COPY . .

# no correr como root
RUN useradd -m appuser
USER appuser

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
