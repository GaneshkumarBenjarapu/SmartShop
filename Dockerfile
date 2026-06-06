FROM python:3.14-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

COPY . .

EXPOSE 5000

CMD ["sh", "-c", "python backend/inject_lookbooks.py && gunicorn --bind 0.0.0.0:${PORT:-5000} backend.app:app"]
