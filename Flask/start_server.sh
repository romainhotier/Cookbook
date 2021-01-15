#!/bin/bash
###  go in venv ###
cd /home/ubuntu/Workspace/env-python/env-cookbook/bin
### activate venv ###
source activate
### go in repo ###
cd /home/ubuntu/Workspace/Cookbook/Flask
### install packages ###
pip install -r requirements.txt
### generate doc ###
apidoc -i ../Flask/ -o ../apidoc/
### launch le server ###
python run.py