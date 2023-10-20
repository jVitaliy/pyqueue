#!/bin/bash
source /etc/sysconfig/tauproject/alcyone-pdm/pyqueue_init.sh
source "$(pwd)/venv/bin/activate"

"$(pwd)/venv/bin/python3.9" "$(pwd)/scan.py"
deactivate
exit 0
