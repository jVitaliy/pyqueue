import logging

from interpreter.DescParser import DescParser
from interpreter.DeployingStage import DeployingStage


class CleaningStage(DeployingStage):

    def enterCloseGitRepo(self, ctx: DescParser.CloseGitRepoContext):
        pass
        # self._repo_data = dict()

    def exitCloseGitRepo(self, ctx: DescParser.CloseGitRepoContext):
        if self._current_branch is not None and len(self.scope_stack) > 0:
            last_repo = self.scope_stack.pop()
            self._git_service.removeFolder(last_repo['tmp_folder'])
            logging.info(f"folder {last_repo['tmp_folder']} has been removed")
