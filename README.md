# Portfolio_Project_one
* This is a end to end implementation of a machine learning model, tracked and deployed using MLFlow.

* To make make the Experimentation collaborative a remote server called DagsHUB is used in integration with
  Git and MLFlow.

* This project is deployed locally using Flask

* To make this project able to run on any machine( which support dockers ) the entire project is containerized and the relavent 
  Dockerfiles and .dockerignore files are also give for you to be able to build a docker image on your system and deploy the model in 
  a Docker Container

## Problem Statement

You are given a Wine Quality dataset and you need to create a ML model to perdict the quality of 
wine based on the features given


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

# Step by Step projecct Walkthrough
#### This is how I made this project

## Step 1 -- Setiing up a Github Repository
 
1. Go to github, login to your account.
2. Create a new repository and give it a name of your choice.
3. Select a Licence--- I selected GNU version 3, you may choose accordingly
4. Create a .gitignore file, just by checking the tickbox, and selecting Python  ( you don't need to manually make one)

## Step 2 --Making virtual environment and cloning the github repo
1. To make a virtual enviromnet I used the following command

            python -m venv
        virtual environments can be created via conda as well and there are few more ways, but I preffer venv

2. Clone your github repository
         
        git clone https://github.com/swarajbari18/Portfolio_Project_one.git

##### While working to push my code to the github repo the commands required are:

```cmd
git add .
git commit -m "Message of your choice"
git push origin main
```
## Step 3 -- Create folder structure, so that we can easily go about the project

I created a folders first hand because I wanted to have a sort of blueprint of what I wanted to do

## Step 4 -- CODE

Now I had a blueprint to work with , I wrote all the code I needed .

## Step 5 -- Setting up a DagsHUB server

So DagsHUB offers remote servers where we can make the project Experimentation collaborative and 
track our model experiments via MLFlow Experiment tracker

The link to my remote server is: https://dagshub.com/swarajbari18/Portfolio_Project_one

If you wish to see the MLFlow Experiment Dashboard : https://dagshub.com/swarajbari18/Portfolio_Project_one.mlflow


## Step 6 -- Integrating MLFlow with the project

###### mlflow commands   --- > 
mlflow ui (will show a local server link for ui)
to see the collaborative experiments go tho the dagsHUB tracking uri


MLFLOW_TRACKING_URI=https://dagshub.com/swarajbari18/Portfolio_Project_one.mlflow \
MLFLOW_TRACKING_USERNAME=swarajbari18 \
MLFLOW_TRACKING_PASSWORD=624708f51d3a09f6c16c93c4ba5a1491c9137622 \
python script.py


We need to export them as our environment variables for us to be able to use dagsHUB for MLFlow Experiment tracking
If you don't do these then the MLFlow dashboard will still open in your local host machine port, but not on the remote server
CAUTION
These commands will not work in windows terminal or Powershell
They run in Git Bash
Or if one is using Linux , then also they will work because export is a command that exists in unix based OS

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/swarajbari18/Portfolio_Project_one.mlflow 

export MLFLOW_TRACKING_USERNAME=swarajbari18

export MLFLOW_TRACKING_PASSWORD=624708f51d3a09f6c16c93c4ba5a1491c9137622

```

## Step 7 -- Containerize our model

Before containerizing , I did run the app.py , which is our 
Flask application I used for deploying. After it ran succesfully locally, then only I went ahead with containerization

To containerize create a Dockerfile

Also create a .dockerignore file for us to be able to ignore copying our virtual environment (venv) to the image,
as it would just be of no use there and our image size will be uselessly bigger
I also ignored our Dockerfile in .dockerignore as to not expose our layer scheme in the image

## Step 8 -- Build dockr image
```cmd
docker build -t swarajbaris-app:version1
```

## Step 9 -- Run the container
```cmd
docker run -d -p 5000:8000 --name runwineapp winequality-app:version1
```

## Step 10 -- Open the WebApp in the browser

While building the docker image I exposed the port 8000 of the docker machine
and while running the container I mapped my port 5000 to the port 8000 of the docker machine
so to open our web app in the machin we just have to follow the three steps
        1) Open a web browser of your liking
        2) type 
                http://127.0.0.1:5000/
                in your address bar
        3) Use the app.

