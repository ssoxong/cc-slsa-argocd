FROM python:3.9-slim

WORKDIR /
COPY demo.py .

CMD ["python", "demo.py"]
