    # pull official base image
    FROM python:3.8-alpine as builder

    ENV PYTHONDONTWRITEBYTECODE 1
    ENV PYTHONUNBUFFERED 1

    # Set the working directory to /app
    WORKDIR /app

    RUN apk update \
        && apk add apk-tools \
        && apk add postgresql-dev gcc python3-dev musl-dev
    
    # RUN apt-get update \
    # && apt-get install -y postgresql-dev gcc python3-dev musl-dev

    # Install Python dependencies
    COPY requirements.txt ./
    RUN pip install --no-cache-dir -r requirements.txt

    COPY ./static .
    COPY ./media .

    COPY . .
    
    EXPOSE 8000

    CMD ["gunicorn", "--bind", "0.0.0.0:8000", "unicon.wsgi:application"]
