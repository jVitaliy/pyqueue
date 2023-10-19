import logging
import os
import re
import sys

from interpreter.DescProcessor import DescProcessor
from interpreter.TauDeployScriptInterpreter import get_tree_and_parser, start_walking

DEFAULT_QUEUE_FOLDER = "/var/lib/tauproject/alcyone-pdm/queue"
DEFAULT_SCRIPT_FOLDER = "/var/lib/tauproject/alcyone-pdm/scripts"


def process_file(filename):
    filename_processing = f"{filename}.queue"
    os.rename(filename, filename_processing)
    path = None
    branch = None
    script_filename = filename.replace(".git", ".desc")
    with open(filename_processing, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("path:"):
                path = line.split(':')[1]
            elif line.startswith("branch:"):
                branch = line.split(':')[1]
    if path is not None and branch is not None:
        script_file_path = f"{DEFAULT_SCRIPT_FOLDER}/{script_filename}"
        if os.path.isfile(script_file_path):
            tree_and_parser = get_tree_and_parser(f"{DEFAULT_SCRIPT_FOLDER}/{script_filename}")
            processor = DescProcessor(branch, path.replace("/home/git/", ""))
            start_walking(tree_and_parser[1], processor)
        else:
            logging.info(f"there is no script {script_file_path} - no actions")
    os.remove(f"{DEFAULT_QUEUE_FOLDER}/{filename_processing}")


def start(args):
    folder_to_scan = DEFAULT_QUEUE_FOLDER if len(args) < 2 else args[1]
    pattern = re.compile('\*.git')
    for root, dirs, files in os.walk(folder_to_scan):

        for filename in files:
            if re.search(pattern, filename) is not None:
                process_file(filename)


if __name__ == '__main__':
    start(sys.argv)
