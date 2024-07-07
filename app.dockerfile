FROM python:3.11.9-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

COPY app /app
COPY scripts /scripts 
WORKDIR /app

RUN apt-get update && apt-get -y dist-upgrade && \
    apt-get install -y libpq5 && \
    apt-get install -y netcat && \
    python -m venv /venv && \
    /venv/bin/pip install setuptools wheel --upgrade pip && \
    /venv/bin/pip install -r requirements.txt && \
    adduser --disabled-password --no-create-home python_user && \
    mkdir -p /web/static && \
    mkdir -p /web/media && \
    chown -R python_user:python_user /app && \
    chown -R python_user:python_user /venv && \
    chown -R python_user:python_user /web/static && \
    chown -R python_user:python_user /web/media && \
    chmod -R 777 /app && \
    chmod -R 777 /web/static && \
    chmod -R 777 /web/media && \
    chmod -R +x /scripts    


ENV PATH="/app:/scripts:/venv/bin:$PATH"

USER python_user

CMD ["commands.sh"]