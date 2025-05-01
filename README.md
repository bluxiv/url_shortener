# A Url Shortener Made With Django & Nuxt using Docker

## API Endpoints
- `POST /api/links/`: Create a new link (Takes 'url' as input).
- `GET  /api/links/`: List links (ordered by most visits by default).
- `GET  /api/links/{short_code}/`: Retrieve a specific link.
- `GET  /api/links/{short_code}/visits/`: List visits for the link (ordered by most recent first).

## Environment variables

Rename `.env.example` to `.env` or redefine the following variables:
* COMPOSE_PROJECT_NAME
* POSTGRES_DB
* POSTGRES_USER
* POSTGRES_PASSWORD
* DATABASE_PORT
* DJANGO_SECRET_KEY
* DJANGO_DEBUG
* DJANGO_ALLOWED_HOSTS
* BACKEND_PORT
* FRONTEND_PORT
* NUXT_PUBLIC_API_BASE
* NUXT_PUBLIC_DOMAIN_ROOT

## Development
```
docker compose up --build -d
```
Frontend `http://localhost:3000`

Backend  `http://localhost:8000`
