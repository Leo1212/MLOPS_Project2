# MLOPS_Project2

## Getting Started

Follow these steps to set up your project:

1. **Add Neptune Credentials:**
   - Create a `.env` file in the root folder.
   - Add your [Neptune credentials](https://app.neptune.ai/register/) to the `.env` file:
     ```
     NEPTUNE_API_TOKEN=""
     NEPTUNE_PROJECT=""
     ```
     How to get my [api token](https://docs.neptune.ai/setup/setting_api_token/)?

2. **Create the Conda Environment:**
   - Run the command: `conda create -n mlopsp2 python=3.10.12`

3. **Activate Conda Environment:**
   - Activate the environment: `conda activate mlopsp2`

4. **Install Requirements:**
   - Install necessary packages: `pip install -r requirements.txt`

5. **Run the Script Locally:**
   - Execute the script: `python train.py --checkpoint_dir ./`

## Building & Running Docker Container

To build and run the Docker container, follow these steps:

1. Build the container:
   - `docker build -t mlops-p2 .`

2. Run the container:
   - `docker run --name MLOPS-Project2 mlops-p2`

## Pushing the Docker Container

To push the Docker container to a registry, follow these instructions:

1. **Modify `.env` for Security:**
   - In the `.env` file, replace  
    `COPY .env .`   
    with   
    `#COPY .env .`   
    to prevent copying credentials.

2. **Build the Container:**
   - Build with your username: `docker build -t {yourUsername}/mlops-p2 .`
   - Replace `{yourUsername}` with your Docker Hub username.

3. **Verify the Container:**
   - Run and verify the container: 
     ```
     docker run --name MLOPS-Project2 -e NEPTUNE_API_TOKEN="YOUR_API_KEY" -e NEPTUNE_PROJECT='YOUR_PROJECT' {yourUsername}/mlops-p2
     ```
   - Replace `{yourUsername}`, `YOUR_API_KEY`, and `YOUR_PROJECT` appropriately.

4. **Push the Container:**
   - Push to Docker Hub: `docker push {yourUsername}/mlops-p2`
   - Again, replace `{yourUsername}` with your username.

## Pulling Your Container

To pull your previously pushed container, use the command:

- `docker pull {yourUsername}/mlops-p2`
- Remember to replace `{yourUsername}` with your Docker Hub username.