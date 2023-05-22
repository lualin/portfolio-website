#!/usr/bin/env bash
pip install -r requirements.txt
# set -o errexit  # exit on error

python manage.py collectstatic --no-input
python manage.py migrate