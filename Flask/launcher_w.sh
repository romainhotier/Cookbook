#!/bin/bash
###  allez dans le venv ###
dir /Users/mac/PycharmProjects/Flask/venv/Scripts/bin
### activer le venv ###
source activate
### installer les packages ###
dir /Users/mac/Desktop/Cookbook/Flask
pip install -r requirements.txt
### generer la doc ###
apidoc -i ../Flask/ -o ../apidoc/
### lancer le server ###
#python run.py