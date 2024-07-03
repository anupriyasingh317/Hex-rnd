FROM python:3.12.4-slim

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "app.py"]