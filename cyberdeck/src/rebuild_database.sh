#!/bin/bash
########################################################
# go.sh
# Run the app in the virtual environment
########################################################

cd /home/duncan/dev/src/python//acute-experiments/cyberdeck/src
source venv_app/bin/activate
python ./z_setup_database.py
