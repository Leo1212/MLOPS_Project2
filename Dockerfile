FROM python:3.10.12-slim

WORKDIR /app

COPY requirements.txt .

COPY .env .

RUN pip install --no-cache-dir -r requirements.txt

COPY train.py .
COPY GLUEDataModule.py .
COPY GLUETransformer.py .

CMD ["python", "train.py"]
