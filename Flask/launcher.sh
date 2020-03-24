#!/bin/bash
###  allez dans le venv ###
cd /Users/mac/PycharmProjects/Flask/venv/bin
### activer le venv ###
source activate
### installer les packages ###
cd /Users/mac/Desktop/Cookbook/Flask
pip install -r requirements.txt
### generer la doc ###
apidoc -i ../Flask/ -o ../apidoc/
### lancer le server ###
#python run.py