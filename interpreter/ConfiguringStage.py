from interpreter.DescParser import DescParser
from interpreter.PostBuildStage import PostBuildStage


class ConfiguringStage(PostBuildStage):

    def enterApplyConfiguration(self, ctx: DescParser.ApplyConfigurationContext):
        self._deploy_data = dict()

    def exitApplyConfiguration(self, ctx: DescParser.ApplyConfigurationContext):
        if self._current_branch is None:
            return
        # print(self._deploy_data)
        excluded = self._deploy_data['excluded'] if 'excluded' in self._deploy_data.keys() else None
        pattern = self._deploy_data['pattern'] if 'pattern' in self._deploy_data.keys() else None
        # print(f"{pattern} / {excluded}")
        current_repo_data = self.scope_stack[len(self.scope_stack) - 1]
        current_project_name = current_repo_data["project_name"]
        if ctx.configurationPath():
            config_path = ctx.configurationPath().confPath().getText()
            path_to = f"{current_repo_data['tmp_folder']}/{current_project_name}/{config_path}"
        else:
            path_to = f"{current_repo_data['tmp_folder']}/{current_project_name}"

        path_from = ctx.pathFrom().pathForDeploy().getText()
        # print(f"{path_to} / {path_from}")
        # ctx.configurationBranch().
        self._config_service.apply(self._repo_host, ctx.repoPath().getText(), ctx.configurationBranch().configBranchName().getText(),
                                   path_from, path_to, exclude=excluded, pattern=pattern, git_service=self._git_service)
        self._deploy_data = None
