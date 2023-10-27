#!/bin/bash --login

cd `dirname $0`

screen -S onten2023junior -X quit
git pull
screen -dmS onten2023junior source .venv/bin/activate && python3 manage.py runserver