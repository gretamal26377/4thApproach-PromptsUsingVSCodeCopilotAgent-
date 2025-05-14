# Use official Python image
FROM python:3.11-slim

WORKDIR /app

# Copy backend requirements for shared dependencies
COPY ../../customer/backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy admin backend code
COPY . .
# Copy shared backend code
COPY ../../customer/backend/app ../customer/backend/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
