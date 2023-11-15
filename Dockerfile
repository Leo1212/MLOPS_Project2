FROM python:3.10.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY train.py .
COPY GLUEDataModule.py .
COPY GLUETransformer.py .
COPY .env .

CMD ["python", "train.py"],
# CMD ["python", "train.py", "--train_batch_size", "1", "--eval_batch_size", "1", "--warmup_steps", "0"],
