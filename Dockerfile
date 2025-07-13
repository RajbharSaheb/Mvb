# Base image
FROM node:18

# Set working directory
WORKDIR /app

# Copy backend code
COPY backend ./backend
WORKDIR /app/backend

# Install dependencies
RUN npm install

# Expose port if needed
EXPOSE 5000

# Start backend
CMD ["npm", "start"]
