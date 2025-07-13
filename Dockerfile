# base image
FROM node:18

# Create app dir
WORKDIR /app

# Copy and install backend
COPY backend ./backend
WORKDIR /app/backend
RUN npm install

# Copy frontend and install
WORKDIR /app
COPY frontend ./frontend
WORKDIR /app/frontend
RUN npm install && npm run build

# Serve frontend + backend using serve
RUN npm install -g serve
WORKDIR /app
CMD concurrently "node backend/index.js" "serve -s frontend/build -l 3000"
