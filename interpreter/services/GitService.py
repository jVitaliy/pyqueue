import logging
import os

from interpreter.services.AbstractExternalShellCmd import AbstractExternalShellCmd
from interpreter.services.FSService import FSService
from interpreter.exceptions.GitException import GitException


class GitService(AbstractExternalShellCmd):

    def __init__(self):
        super().__init__()
        self._fsService = FSService()
        self.gitRepoName = None

    def getRepoName(self, repo_path):
        return self._fsService.extractFilenameWithoutExt(repo_path)

    def clone(self, repo_path, host='localhost'):
        self.gitRepoName = self._fsService.extractFilenameWithoutExt(repo_path)
        os.environ["GIT_SSH_COMMAND"] = "ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no"
        temp_dir = self._fsService.createTemp(self.gitRepoName)
        cmd = f"/usr/bin/git clone git@{host}:{repo_path}"
        self.execute(cmd, working_folder=temp_dir)
        logging.info(f"{cmd} => {self.returncode} {self.error}")
        if self.returncode > 0:
            raise GitException(self.error)
        return temp_dir

    def checkout(self, branch_name, repo_dir):
        self.execute(f"/usr/bin/git checkout {branch_name}", working_folder=repo_dir)

    def removeFolder(self, temp_dir):
        self._fsService.deleteTemp(temp_dir)


