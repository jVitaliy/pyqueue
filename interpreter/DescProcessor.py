import logging

from interpreter.DescListener import DescListener
from interpreter.DescLog import DescLog
from interpreter.DescParser import DescParser
from interpreter.exceptions.GitBranchException import GitBranchException
from interpreter.services.DeployService import DeployService
from interpreter.services.GitService import GitService
from interpreter.exceptions.OpenGitRepoException import OpenGitRepoException


class DescProcessor(DescListener):

    def __init__(self, branch, repo_path=None, git_service=None, deploy_service=None):
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

        if git_service is None:
            self._git_service = GitService()
        else:
            self._git_service = git_service

        if deploy_service is None:
            self._deploy_service = DeployService()
        else:
            self._deploy_service = deploy_service

    def getBranch(self):
        return self._current_branch

    def getRepoHost(self):
        return self._repo_host

    def getRepos(self):
        return self.repos

    def exitBranchName(self, ctx:DescParser.BranchNameContext):
        self._current_branch = ctx.getText()
        if self._current_branch.__eq__(self._target_branch):
            logging.info(f"set branch {self._current_branch}")
        else:
            raise GitBranchException(f"branch {self._current_branch} does not match to target branch {self._target_branch}")

    def exitSetRepoSource(self, ctx:DescParser.SetRepoSourceContext):
        logging.info(f"set repo host to {self._repo_host}")

    def exitHost(self, ctx:DescParser.SetRepoSourceContext):
        self._repo_host = ctx.getText()

    def enterCloneGitToTmp(self, ctx:DescParser.CloneGitToTmpContext):
        self._repo_data = dict()

    def exitCloneGitToTmp(self, ctx:DescParser.CloneGitToTmpContext):
        repo_obj = {'path': self._initial_repo_path, 'alias': None}

        if self._repo_data is not None and 'path' in self._repo_data.keys():
            if 'alias' in self._repo_data.keys():
                repo_obj['alias'] = self._repo_data['alias']
            repo_obj['path'] = self._repo_data['path']
        elif self._initial_repo_path is None:
            logging.error(f"to use empty (current) repo it must be set in constructor")
            raise OpenGitRepoException('to use empty (current) repo it must be set in constructor')

        self._repo_data = None
        repo_obj['tmp_folder'] = self._git_service.clone(repo_obj['path'], self._repo_host)
        self._git_service.checkout(self._current_branch, repo_obj['tmp_folder'])
        logging.info(f"cloned repo to tmp folder {repo_obj['tmp_folder']} and checkout to {self._current_branch}")
        self.scope_stack.append(repo_obj)

    def exitRepoPath(self, ctx:DescParser.RepoPathContext):
        if len(ctx.getText()) > 0:
            self._repo_data["path"] = ctx.getText()

    def exitRepoAliasName(self, ctx:DescParser.RepoAliasNameContext):
        if len(ctx.getText()) > 0:
            self._repo_data["alias"] = ctx.getText()

    def enterCloseGitRepo(self, ctx:DescParser.CloseGitRepoContext):
        self._repo_data = dict()

    def exitCloseGitRepo(self, ctx:DescParser.CloseGitRepoContext):
        if len(self.scope_stack) > 0:
            last_repo = self.scope_stack.pop()
            self._git_service.removeFolder(last_repo['tmp_folder'])

    def exitPathForDeployTo(self, ctx:DescParser.PathForDeployToContext):
        path_from = ctx.pathForDeploy().getText()
        if path_from is not None:
            self._deploy_data['path'] = path_from


    def exitPathFrom(self, ctx:DescParser.PathFromContext):
        path_from = ctx.pathForDeploy().getText()
        if path_from is not None:
            self._deploy_data['path_from'] = path_from

    def enterExcludePattern(self, ctx:DescParser.ExcludePatternContext):
        self._exclude_pattern = list()

    def enterDeployPattern(self, ctx:DescParser.DeployPatternContext):
        self._deploy_pattern = list()

    def exitPattern(self, ctx:DescParser.PatternContext):
        if self._exclude_pattern is not None:
            self._exclude_pattern.append(ctx.getText())
        elif self._deploy_pattern is not None:
            self._deploy_pattern.append(ctx.getText())

    def exitExcludePattern(self, ctx:DescParser.ExcludePatternContext):
        self._deploy_data['excluded'] = self._exclude_pattern
        self._exclude_pattern = None

    def exitDeployPattern(self, ctx:DescParser.DeployPatternContext):
        self._deploy_data['pattern'] = self._deploy_pattern
        self._deploy_pattern = None

    def enterDeployTo(self, ctx:DescParser.DeployToContext):
        self._deploy_data = {}

    def exitDeployTo(self, ctx:DescParser.DeployToContext):

        excluded = self._deploy_data['excluded'] if 'excluded' in self._deploy_data.keys() else None
        pattern = self._deploy_data['pattern'] if 'pattern' in self._deploy_data.keys() else None

        self._deploy_service = DeployService(exclude=excluded, pattern=pattern )
        current_repo_data = self.scope_stack[len(self.scope_stack)-1]
        path_from = current_repo_data['tmp_folder'] if 'path_from' not in self._deploy_data.keys() \
            else f"{current_repo_data['tmp_folder']}/{self._deploy_data['path_from']}"
        self._deploy_service.deploy(path_from, self._deploy_data['path'])
