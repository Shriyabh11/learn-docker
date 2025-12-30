FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY app.py test_app.py ./

# Run tests DURING build
RUN pytest

# If tests pass, image builds successfully
CMD ["python"]
