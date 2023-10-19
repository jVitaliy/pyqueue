#!/usr/bin/env bash
source venv/bin/activate
/usr/bin/python3 processor/processing_request_files.py $1
deactivate
exit 0
