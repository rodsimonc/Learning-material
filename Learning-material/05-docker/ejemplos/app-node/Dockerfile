FROM node:20-slim
WORKDIR /app

# copiar package.json primero para cachear npm install
COPY package*.json ./
RUN npm install --omit=dev

COPY . .
USER node
EXPOSE 3000
CMD ["node", "server.js"]
