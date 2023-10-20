from interpreter.DescParser import DescParser
from interpreter.DeployingStage import DeployingStage


class CleaningStage(DeployingStage):

    def enterCloseGitRepo(self, ctx: DescParser.CloseGitRepoContext):
        self._repo_data = dict()

    def exitCloseGitRepo(self, ctx: DescParser.CloseGitRepoContext):
        if len(self.scope_stack) > 0:
            last_repo = self.scope_stack.pop()
            self._git_service.removeFolder(last_repo['tmp_folder'])
