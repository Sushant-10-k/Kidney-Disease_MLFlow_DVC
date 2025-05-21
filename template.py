import os
from pathlib import Path
from datetime import datetime
import logging

#logging string
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

project_name = 'cnnkidneydiseaseClassifier'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
"config/config.yaml",
"dvc.yaml",
"params.yaml",
"requirements.txt",
"setup.py",
"research/trials.ipynb",
"templates/index.html",



]

for file in list_of_files:
    file_path = os.path.join(os.getcwd(), file)
    file_dir = os.path.dirname(file_path)

    # check if the directory exists
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
        logging.info(f"Creating directory: {file_dir}")

    # check if the file exists
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            pass
        logging.info(f"Creating file: {file_path}")
    else:
        logging.info(f"File already exists: {file_path}")
    

