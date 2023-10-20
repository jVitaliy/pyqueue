#!/bin/bash
/usr/bin/python3.9 -m venv venv
VENV=`$(pwd)`
source "$VENV/venv/bin/activate"
"$VENV/venv/bin/pip3" install -r requirements.txt
deactivate
exit 0
