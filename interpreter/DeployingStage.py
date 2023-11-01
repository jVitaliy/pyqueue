from interpreter.ConfiguringStage import ConfiguringStage
from interpreter.DescParser import DescParser
from interpreter.services.DeployParameters import DeployParameters


class DeployingStage(ConfiguringStage):
    def exitPathForDeployTo(self, ctx: DescParser.PathForDeployToContext):
        if self._current_branch is None:
            return

        path_from = ctx.pathForDeploy().getText()
        if path_from is not None:
            self._deploy_data['path'] = path_from

    def exitPathFrom(self, ctx: DescParser.PathFromContext):
        if self._current_branch is None:
            return

        path_from = ctx.pathForDeploy().getText()
        if path_from is not None:
            self._deploy_data['path_from'] = path_from

    def enterExcludePattern(self, ctx: DescParser.ExcludePatternContext):
        if self._current_branch is None:
            return

        self._exclude_pattern = list()

    def enterDeployPattern(self, ctx: DescParser.DeployPatternContext):
        if self._current_branch is None:
            return

        self._deploy_pattern = list()

    def exitPattern(self, ctx: DescParser.PatternContext):
        if self._exclude_pattern is not None:
            self._exclude_pattern.append(ctx.getText())
        elif self._deploy_pattern is not None:
            self._deploy_pattern.append(ctx.getText())

    def exitExcludePattern(self, ctx: DescParser.ExcludePatternContext):
        if self._current_branch is None:
            return
        self._deploy_data['excluded'] = self._exclude_pattern
        self._exclude_pattern = None

    def exitDeployPattern(self, ctx: DescParser.DeployPatternContext):
        if self._current_branch is None:
            return

        self._deploy_data['pattern'] = self._deploy_pattern
        self._deploy_pattern = None

    def enterDeployTo(self, ctx: DescParser.DeployToContext):
        if self._current_branch is None:
            return

        self._deploy_data = {}

    def exitDeployTo(self, ctx: DescParser.DeployToContext):
        if self._current_branch is None:
            return
        deploy_params = self.extract_deploy_data(ctx, self._deploy_data, self.scope_stack[len(self.scope_stack) - 1])
        self._deploy_service.deploy(deploy_params)

    def enterDeployToRemote(self, ctx: DescParser.DeployToRemoteContext):
        if self._current_branch is None:
            return
        self._deploy_data = {}

    def exitDeployToRemote(self, ctx: DescParser.DeployToRemoteContext):
        if self._current_branch is None:
            return

        deploy_params = self.extract_deploy_data(ctx, self._deploy_data, self.scope_stack[len(self.scope_stack) - 1])
        self._deploy_service.deploy_to_remote(self._variables[ctx.variableName().getText()], deploy_params)

    def enterDeployArchivedToRemote(self, ctx: DescParser.DeployArchivedToRemoteContext):
        if self._current_branch is None:
            return
        self._deploy_data = {}

    def exitDeployArchivedToRemote(self, ctx: DescParser.DeployArchivedToRemoteContext):
        if self._current_branch is None:
            return

        deploy_params = self.extract_deploy_data(ctx, self._deploy_data, self.scope_stack[len(self.scope_stack) - 1])
        self._deploy_service.deploy_archived_to_remote(self._variables[ctx.variableName().getText()], deploy_params)

    def extract_deploy_data(self, ctx, deploy_data, current_repo_data):
        excluded = deploy_data['excluded'] if 'excluded' in deploy_data.keys() else None
        pattern = deploy_data['pattern'] if 'pattern' in deploy_data.keys() else None

        # self._deploy_service = DeployService()
        # current_repo_data = self.scope_stack[len(self.scope_stack) - 1]
        project_name = current_repo_data["project_name"]
        path_from = f"{current_repo_data['tmp_folder']}/{project_name}" \
            if 'path_from' not in deploy_data.keys() \
            else f"{current_repo_data['tmp_folder']}/{project_name}/{deploy_data['path_from']}"
        is_merge = False if ctx.MERGE() is None else True
        # data = dict()
        deploy_parameters = DeployParameters(src_path=path_from, dest_path=deploy_data['path'],
                                             exclude=excluded, pattern=pattern, is_merge=is_merge,
                                             project_name=project_name)
        return deploy_parameters
