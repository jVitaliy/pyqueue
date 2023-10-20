from interpreter.DescListener import DescListener
from interpreter.DescLog import DescLog
from interpreter.services.DeployService import DeployService
from interpreter.services.GitService import GitService


class AbstractProcessor(DescListener):

    def __init__(self, branch, repo_path=None):
        self._current_branch = None
        self._target_branch = branch
        self._repo_host = None
        self.scope_stack = list()
        self._initial_repo_path = repo_path
        self._descLog = DescLog()
        self._repo_data = None
        self._exclude_pattern = None
        self._deploy_pattern = None
        self._deploy_data = None
        self._git_service = GitService()
        self._deploy_service = DeployService()

    def getBranch(self):
        return self._current_branch

    def getRepoHost(self):
        return self._repo_host
