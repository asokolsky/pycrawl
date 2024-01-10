FROM python:3-slim

WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app

ENTRYPOINT ["python", "main.py"]
