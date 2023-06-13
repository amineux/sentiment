# Dockerfile

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY sentiment_analysis_service.py .

EXPOSE 5000

CMD ["python", "sentiment_analysis_service.py"]
