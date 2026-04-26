# FROM python:3.9

# WORKDIR /app

# COPY ../app /app

# RUN pip install -r requirements.txt

# CMD ["python", "app.py"]

FROM python:3.10-slim

WORKDIR /app

COPY app/ /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]