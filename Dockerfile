FROM python:3.8-slim

WORKDIR /app

COPY . .

# COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["python", "app.py"]