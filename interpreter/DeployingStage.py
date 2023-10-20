from interpreter.ConfiguringStage import ConfiguringStage
from interpreter.DescParser import DescParser
from interpreter.services.DeployService import DeployService


class DeployingStage(ConfiguringStage):
    def exitPathForDeployTo(self, ctx: DescParser.PathForDeployToContext):
        path_from = ctx.pathForDeploy().getText()
        if path_from is not None:
            self._deploy_data['path'] = path_from

    def exitPathFrom(self, ctx: DescParser.PathFromContext):
        path_from = ctx.pathForDeploy().getText()
        if path_from is not None:
            self._deploy_data['path_from'] = path_from

    def enterExcludePattern(self, ctx: DescParser.ExcludePatternContext):
        self._exclude_pattern = list()

    def enterDeployPattern(self, ctx: DescParser.DeployPatternContext):
        self._deploy_pattern = list()

    def exitPattern(self, ctx: DescParser.PatternContext):
        if self._exclude_pattern is not None:
            self._exclude_pattern.append(ctx.getText())
        elif self._deploy_pattern is not None:
            self._deploy_pattern.append(ctx.getText())

    def exitExcludePattern(self, ctx: DescParser.ExcludePatternContext):
        self._deploy_data['excluded'] = self._exclude_pattern
        self._exclude_pattern = None

    def exitDeployPattern(self, ctx: DescParser.DeployPatternContext):
        self._deploy_data['pattern'] = self._deploy_pattern
        self._deploy_pattern = None

    def enterDeployTo(self, ctx: DescParser.DeployToContext):
        self._deploy_data = {}

    def exitDeployTo(self, ctx: DescParser.DeployToContext):

        excluded = self._deploy_data['excluded'] if 'excluded' in self._deploy_data.keys() else None
        pattern = self._deploy_data['pattern'] if 'pattern' in self._deploy_data.keys() else None

        # self._deploy_service = DeployService()
        current_repo_data = self.scope_stack[len(self.scope_stack) - 1]
        path_from = current_repo_data['tmp_folder'] if 'path_from' not in self._deploy_data.keys() \
            else f"{current_repo_data['tmp_folder']}/{self._deploy_data['path_from']}"
        self._deploy_service.deploy(path_from, self._deploy_data['path'], exclude=excluded, pattern=pattern)
