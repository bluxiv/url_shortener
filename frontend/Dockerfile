# Use an official Node runtime as a parent image
FROM node:22-alpine

# Set working directory
WORKDIR /app/frontend

# Copy package.json and lock file (if exists)
# Use `--link` for better pnpm/yarn workspace support if needed
COPY package*.json ./
# If using yarn, copy yarn.lock
# COPY yarn.lock ./
# If using pnpm, copy pnpm-lock.yaml
# COPY pnpm-lock.yaml ./

# Install dependencies based on your package manager
RUN yarn install --frozen-lockfile

# Copy the rest of the application code
COPY . .

# Build Nuxt for production (optional, depends on workflow)
# If you want to build during image creation:
# RUN npm run build

# Expose port 3000
EXPOSE 3000

# Command to run the Nuxt development server
# For production, you might run `node .output/server/index.mjs`
# or serve static files depending on your Nuxt config (ssr: false)
CMD ["yarn", "dev"]