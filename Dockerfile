# pull official base image
FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        nginx \
        mysql-client \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -r requirements.txt \
    && rm -rf /root/.cache/pip/*

# Configure Nginx
# RUN rm /etc/nginx/sites-enabled/default
# COPY nginx.conf /etc/nginx/sites-enabled/
# RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Expose port 80
# EXPOSE 80

# Start Gunicorn
# CMD gunicorn unicon.wsgi:application --bind 0.0.0.0:8000
