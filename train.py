import torch
from pytorch_lightning import Trainer, seed_everything
from lightning.pytorch.loggers.neptune import NeptuneLogger
import os
from dotenv import load_dotenv
from GLUEDataModule import GLUEDataModule
from GLUETransformer import GLUETransformer


load_dotenv()


# Setup Naeptune
my_api_token = os.getenv('NEPTUNE_API_TOKEN')
my_project = os.getenv('NEPTUNE_PROJECT')

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