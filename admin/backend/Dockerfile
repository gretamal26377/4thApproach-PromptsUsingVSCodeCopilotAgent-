# Use official Python image
FROM python:3.11-slim

WORKDIR /app

# Copy backend requirements for shared dependencies
COPY ../../backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy admin backend code
COPY . .
# Copy shared backend code
COPY ../../backend/app ../backend/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
