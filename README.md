# MLOPS_Project2

## Getting started
1. Add your Neptune Credentials (https://neptune.ai):
Create a `.env` file in the root folder.  
Add your credentials to the `.env` file:
```
NEPTUNE_API_TOKEN=""
NEPTUNE_PROJECT=""
```
2. Create the conda environment: `conda create -n mlopsp2 python=3.10.12`
3. activate conda env: `conda activate  mlopsp2`
4. install requirements: `pip install -r requirements.txt`
5. run the script locally: `python train.py --checkpoint_dir ./`

## Create docker container
1. run `docker build -t mlops-p2 .`
2. run `docker run --name MLOPS-Project2 mlops-p2`