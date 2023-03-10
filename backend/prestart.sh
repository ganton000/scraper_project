#! /usr/bin/env bash

#/usr/local/bin/pip install -r requirements.txt

/app/venv/bin/pip install -r requirements.txt

# Run custom Python script before starting
python /app/my_custom_prestart_script.py
