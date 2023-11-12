import torch
from pytorch_lightning import Trainer, seed_everything
from lightning.pytorch.loggers.neptune import NeptuneLogger
import os
import sys
import argparse
from dotenv import load_dotenv
from GLUEDataModule import GLUEDataModule
from GLUETransformer import GLUETransformer


load_dotenv()


# Setup Naeptune
my_api_token = os.getenv('NEPTUNE_API_TOKEN')
my_project = os.getenv('NEPTUNE_PROJECT')

# get run configuration
parser = argparse.ArgumentParser(description="Process inputs.")

parser.add_argument('--checkpoint_dir', type=str, required=False, help='directory for model checkpoints')
parser.add_argument('--lr', type=float, default=1e-3, help='learning rate')
parser.add_argument('--adam_epsilon', type=float, default=1e-8, help='epsilon for Adam optimizer')
parser.add_argument('--warmup_steps', type=int, default=248, help='number of warmup steps for learning rate schedule')
parser.add_argument('--weight_decay', type=float, default=0.00934170221511866, help='weight decay for optimization')
parser.add_argument('--train_batch_size', type=int, default=1024, help='batch size for training')
parser.add_argument('--eval_batch_size', type=int, default=32, help='batch size for evaluation')


args = parser.parse_args()

print(f"Checkpoint directory: {args.checkpoint_dir}")
print(f"Learning rate: {args.lr}")
print(f"Adam Epsilon: {args.adam_epsilon}")
print(f"Warmup Steps: {args.warmup_steps}")
print(f"Weight Decay: {args.weight_decay}")
print(f"Train Batch Size: {args.train_batch_size}")
print(f"Eval Batch Size: {args.eval_batch_size}")

seed_everything(42)

dm = GLUEDataModule(
    model_name_or_path="distilbert-base-uncased",
    task_name="mrpc",
)
dm.setup("fit")
model = GLUETransformer(
    model_name_or_path="distilbert-base-uncased",
    num_labels=dm.num_labels,
    eval_splits=dm.eval_splits,
    task_name=dm.task_name,
)

# Create NeptuneLogger instance
neptune_logger = NeptuneLogger(
    project=my_project,
    api_token=my_api_token,
)

# add neptune to the logger
trainer = Trainer(
    max_epochs=3,
    accelerator="auto",
    devices=1 if torch.cuda.is_available() else None,
    logger=neptune_logger
)

trainer.fit(model, datamodule=dm)

# save model
if(args.checkpoint_dir != None):
    model_save_path = args.checkpoint_dir + 'model.pt'
    torch.save(model, model_save_path)