#!/bin/bash
VENV="/usr/local/tauproject/alcyone-pdm/pyqueue/venv"
source "$VENV/bin/activate"

"$VENV/bin/python3" /usr/local/tauproject/alcyone-pdm/pyqueue/scan.py $1
deactivate
exit 0
