import logging

from interpreter.DescParser import DescParser
from interpreter.Init import Init
from interpreter.exceptions.OpenGitRepoException import OpenGitRepoException


class InitStage(Init):

    def enterCloneGitToTmp(self, ctx: DescParser.CloneGitToTmpContext):
        self._repo_data = dict()

    def exitCloneGitToTmp(self, ctx: DescParser.CloneGitToTmpContext):
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

    def exitRepoPath(self, ctx: DescParser.RepoPathContext):
        if len(ctx.getText()) > 0:
            self._repo_data["path"] = ctx.getText()

    def exitRepoAliasName(self, ctx: DescParser.RepoAliasNameContext):
        if len(ctx.getText()) > 0:
            self._repo_data["alias"] = ctx.getText()