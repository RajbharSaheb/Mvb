# 1. Build React
FROM node:18 AS build
WORKDIR /app
COPY frontend ./frontend
RUN cd frontend && npm install && npm run build

# 2. Backend image
FROM node:18
WORKDIR /app
COPY backend ./backend
COPY --from=build /app/frontend/build ./backend/frontend/build
WORKDIR /app/backend
RUN npm install

CMD ["node", "index.js"]
