#!/bin/bash
###  go in venv ###
cd /home/ubuntu/Workspace/env-python/env-cookbook/bin
### activate venv ###
source activate
### go in repo ###
cd /home/ubuntu/Workspace/Cookbook/Flask
### install packages ###
pip install -r requirements.txt
### generer la doc ###
apidoc -i ../Flask/ -o ../apidoc/
### lancer le server ###
python run.py