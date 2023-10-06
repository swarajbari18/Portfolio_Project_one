import os 
from pathlib import Path    #Path is used to convert strings into Paths
import logging    # to create logs

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')   # this is to enable us to see the logs in our terminal
# log------->  time: message

project_name = 'portfolio_project_one'

list_of_files = [
    ".github/workflows/.gitkeep",    # .github we need for our CI/CD pipelines
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "Experimentation/trials.ipynb",
    "templates/index.html",
    "test.py"
]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating directory: {filedir} for the file : {filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f'Creating empty file: {filepath}')

    else: 
        logging.info(f'{filename} already exists.')

