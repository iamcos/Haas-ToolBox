#!/bin/bash

if [ -d "env" ]; then
    ./env/bin/python3.10 start_cli_app.py
else
    echo "Hello! Now I will start installing dependencies on your pc"

    python3.10 -m venv env

    if [ echo $SHELL == "fish" ]; then
        . ./env/bin/activate.fish
    else
        . ./env/bin/activate
    fi

    pip install -r requirements.txt
    ./run.sh
fi

