import logging
import os
import re

from interpreter.DescLog import DescLog
from interpreter.TauDeployScriptInterpreter import TauDeployScriptInterpreter


class RequestFilesProcessor:
    def __init__(self):
        self._queue_folder = "/var/lib/tauproject/alcyone-pdm/queue" \
            if os.environ.get("PYQUEUE_QUEUE_FOLDER") is None \
            else os.environ.get("PYQUEUE_QUEUE_FOLDER")
        self._script_folder = "/var/lib/tauproject/alcyone-pdm/scripts" \
            if os.environ.get("PYQUEUE_SCRIPT_FOLDER") is None \
            else os.environ.get("PYQUEUE_SCRIPT_FOLDER")
        self._git_home = "/home/git" if os.environ.get("PYQUEUE_GIT_HOME") is None \
            else os.environ.get("PYQUEUE_GIT_HOME")
        self._desc_interpreter = TauDeployScriptInterpreter()

    def get_scriptname(self, tast_filename):
        filename_parts = tast_filename.split('.')
        script_name_arr = filename_parts[1:-1]
        script_name_arr.append("desc")
        return ".".join(script_name_arr)

    def processFile(self, root, filename):
        filename_processing = f"{filename}.queue"
        filename_processing_full_path = f"{root}/{filename_processing}"
        os.rename(f"{root}/{filename}", filename_processing_full_path)
        path = None
        branch = None

        with open(filename_processing_full_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("path:"):
                    path = line.split(':')[1]
                elif line.startswith("branch:"):
                    branch = line.split(':')[1]

        script_filename = self.get_scriptname(filename)
        if path is not None and branch is not None:
            script_file_path = f"{self._script_folder}/{script_filename}"

            if os.path.isfile(script_file_path):
                print(f"script_file_path={script_file_path}")
                path_to_script = f"{self._script_folder}/{script_filename}"
                self._desc_interpreter.start_walking(path_to_script, branch, path.replace(f"{self._git_home}/", ""))
            else:
                logging.info(f"there is no script {script_file_path} - no actions")
        os.remove(f"{root}/{filename_processing}")

    def start(self):
        DescLog()
        logging.info(f"start scanning {self._queue_folder}")

        pattern = re.compile("\*\.git")
        for root, dirs, files in os.walk(self._queue_folder):
            for filename in files:
                print(f"{filename} {re.findall(pattern, filename)}")
                if re.findall(pattern, filename) is not None:
                    self.processFile(root, filename)