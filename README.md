# Portfolio_Project_one
This is a end to end implementation of a machine learning model, tracked and deployed using MLFlow.
To make make the Experimentation collaborative a remote server called DagsHUB is used in integration with
Git and MLFlow.

## Problem Statement



## Approach



## Workflows

1. Update config.yaml
2. Updte schema.yaml
3. Update params.yaml
4. Update entity
5. Update configuration manager in src/config
6. Update components
7. Update pipeline
8. Update main.py
9. Update app.py

## Setting up github repo

## Step 0 making virtual environment and cloning the github repo

## Step 1


## Step 2

## Step 3

## Step 4

## Step 5


## Integrating MLFlow and setting up a DagsHUB remote server for collaboration.

#### STEPS:
###### mlflow command   --- > 
mlflow ui (will show a local server link for ui)
to see the collaborative experiments go tho the dagsHUB tracking uri


MLFLOW_TRACKING_URI=https://dagshub.com/swarajbari18/Portfolio_Project_one.mlflow \
MLFLOW_TRACKING_USERNAME=swarajbari18 \
MLFLOW_TRACKING_PASSWORD=624708f51d3a09f6c16c93c4ba5a1491c9137622 \
python script.py


Now we need to export them as our environment variables: 

```bash 

export MLFLOW_TRACKING_URI=https://dagshub.com/swarajbari18/Portfolio_Project_one.mlflow 

export MLFLOW_TRACKING_USERNAME=swarajbari18

export MLFLOW_TRACKING_PASSWORD=624708f51d3a09f6c16c93c4ba5a1491c9137622

