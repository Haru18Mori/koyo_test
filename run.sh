#!/bin/bash --login

cd `dirname $0`

screen -S onten2023junior -X quit
git pull
screen -dmS onten2023junior bash -c "source .venv/bin/activate && pip3 install -r requirements.txt && python3 manage.py runserver"