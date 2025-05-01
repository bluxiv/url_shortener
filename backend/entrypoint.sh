#!/bin/sh

# Wait for Database
echo "Waiting for database at db:$DATABASE_PORT..."
while ! nc -z db $DATABASE_PORT; do
  sleep 0.5 # wait for 0.5 seconds before check again
done
echo "Database started"

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

echo "Starting server..."
exec "$@"