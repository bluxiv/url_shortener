# Use an official Python runtime as a parent image
FROM python:3.13-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app/backend

# Install dependencies
# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy ONLY the project source code and entrypoint
COPY manage.py .
COPY project ./project
COPY shortener ./shortener
COPY entrypoint.sh .

# --- START OF DEBUGGING ---
# List the contents of the working directory to verify the entrypoint exists
# and check its permissions. This will show up in the Coolify build logs.
RUN ls -la /app/backend
# --- END OF DEBUGGING ---

# Add execute permissions to the entrypoint script.
# This is a mandatory step for any script that will be executed.
RUN chmod +x /app/backend/entrypoint.sh

# Expose port 8000 for Django dev server
EXPOSE 8000


# Specify the entrypoint script
ENTRYPOINT ["/app/backend/entrypoint.sh"]

# Default command to run the Django development server
# For production, you would change this to use gunicorn
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]