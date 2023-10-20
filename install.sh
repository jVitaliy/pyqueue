#!/bin/bash
/usr/bin/python3.9 -m venv venv
source "$(pwd)/venv/bin/activate"
"$(pwd)/venv/bin/pip3.9" install -r requirements.txt
deactivate
exit 0
