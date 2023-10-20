#!/bin/bash
source /etc/sysconfig/tauproject/alcyone-pdm/pyqueue_init.sh
VENV="/usr/local/tauproject/alcyone-pdm/pyqueue/venv"
source "$VENV/bin/activate"

"$VENV/bin/python3" /usr/local/tauproject/alcyone-pdm/pyqueue/scan.py
deactivate
exit 0
